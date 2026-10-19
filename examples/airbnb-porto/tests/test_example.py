import csv
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from src.core import blank_manual_template, kpis, number, price, rows
from src.review_analysis import cache_key, class_metrics, evaluate, multilabel_metrics, validate


class ExampleTests(unittest.TestCase):
    def test_price_uses_explicit_separators_and_rejects_nonfinite(self):
        self.assertEqual(price('$1,234.50'), 1234.5)
        self.assertEqual(price('1.234,50 €', ',', '.'), 1234.5)
        self.assertIsNone(price('1,2,3'))
        self.assertIsNone(price('NaN'))
        self.assertIsNone(number('inf'))
        self.assertIsNone(number('2.5', True))

    def test_missing_price_only_changes_price_denominator(self):
        listing = lambda i, p: {'snapshot_date': '2026-06-23', 'id': i, 'neighbourhood_cleansed': 'A', 'room_type': 'Entire home/apt', 'price_advertised_eur': p, 'minimum_nights': 2, 'number_of_reviews': 0}
        config = {'snapshots': ['2026-06-23'], 'latest_snapshot': '2026-06-23', 'calendar_window_days': 30}
        result = {r['kpi_id']: r for r in kpis([listing('0001', None), listing('0002', 100)], [], config) if r['neighbourhood'] == 'all'}
        self.assertEqual(result['listing_count']['value'], 2)
        self.assertEqual(result['median_advertised_price_latest']['value'], 100)
        self.assertEqual(result['median_advertised_price_latest']['denominator'], 1)
        self.assertEqual(result['mean_available_next30']['value'], '')

    def test_partial_calendar_is_not_extrapolated_or_filled_with_zero(self):
        listing = {'snapshot_date': '2026-06-23', 'id': 'x', 'neighbourhood_cleansed': 'A', 'room_type': 'Private room', 'price_advertised_eur': 100, 'minimum_nights': 1, 'number_of_reviews': 3}
        days = [{'snapshot_date': '2026-06-23', 'listing_id': 'x', 'available': 't', 'valid': True}, {'snapshot_date': '2026-06-23', 'listing_id': 'x', 'available': 'f', 'valid': True}, {'snapshot_date': '2026-06-23', 'listing_id': 'x', 'available': 'bogus', 'valid': False}]
        config = {'snapshots': ['2026-06-23'], 'latest_snapshot': '2026-06-23', 'calendar_window_days': 30}
        value = next(r for r in kpis([listing], days, config) if r['neighbourhood'] == 'all' and r['kpi_id'] == 'mean_available_next30')
        self.assertEqual(value['value'], 50)
        self.assertIn('observed valid days=2', value['notes'])

    def test_manual_template_is_blank_and_never_overwrites_annotations(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder)/'manual.csv'
            sample = [{'review_id': '0007', 'listing_id': '0001', 'comments': 'Example text'}]
            config = {'dev_sample_size': 0, 'test_sample_size': 1}
            blank_manual_template(sample, path, config)
            initial = list(rows(path, ['review_id', 'sentiment']))
            self.assertEqual(initial[0]['sentiment'], '')
            text = path.read_text(encoding='utf-8')
            path.write_text(text.replace(',test,,,', ',test,positive,[],en'), encoding='utf-8')
            before = path.read_bytes()
            blank_manual_template(sample, path, config)
            self.assertEqual(before, path.read_bytes())
            with self.assertRaises(ValueError):
                blank_manual_template([dict(sample[0], comments='Changed')], path, config)

    def test_schema_rejects_invalid_aspects_language_and_duplicate_pairs(self):
        good = {'sentiment': 'positive', 'aspects': [], 'language': 'fr'}
        self.assertEqual(validate(good), good)
        for bad in [dict(good, language='other'), dict(good, aspects=[{'aspect': 'fake', 'polarity': 'praised'}]), dict(good, aspects=[{'aspect': 'value', 'polarity': 'praised'}]*2)]:
            with self.assertRaises(ValueError):
                validate(bad)

    def test_cache_changes_with_text_model_and_parameter(self):
        row = {'review_id': '1', 'comments': 'Text'}
        key = cache_key(row, 'model')
        self.assertNotEqual(key, cache_key(dict(row, comments='Other'), 'model'))
        self.assertNotEqual(key, cache_key(row, 'other-model'))
        self.assertNotEqual(key, cache_key(row, 'model', .001))

    def test_missing_prediction_stays_in_accuracy_denominator(self):
        metrics = class_metrics(['positive', 'negative'], ['positive', None], ['positive', 'negative'])
        self.assertEqual(metrics['accuracy'], .5)
        self.assertEqual(metrics['coverage'], .5)
        self.assertEqual(metrics['macro_f1'], .5)
        empty = class_metrics([], [], ['positive'])
        self.assertIsNone(empty['accuracy'])
        with self.assertRaises(ValueError):
            class_metrics(['fr'], [], ['fr'])

    def test_multilabel_f1_matches_hand_calculation(self):
        one = lambda a: {'aspect': a, 'polarity': 'praised'}
        metric = multilabel_metrics([[one('location'), one('cleanliness')]], [[one('location'), one('noise')]])
        self.assertEqual(metric, {'micro_f1': .5, 'tp': 1, 'fp': 1, 'fn': 1})

    def test_schema_columns_are_checked_before_reading(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder)/'bad.csv'
            path.write_text('unexpected\n1\n', encoding='utf-8')
            with self.assertRaises(ValueError):
                list(rows(path, ['id']))

    def test_human_evaluation_cannot_be_created_from_blank_labels(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder)/'manual.csv'
            sample = [{'review_id': '0007', 'listing_id': '0001', 'comments': 'Example text'}]
            blank_manual_template(sample, path, {'dev_sample_size': 0, 'test_sample_size': 1})
            result = evaluate(path, [], [], sample)
            self.assertIsNone(result['metrics'])
            self.assertEqual(result['completed_test_labels'], 0)


if __name__ == '__main__':
    unittest.main()
