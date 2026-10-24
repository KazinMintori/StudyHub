"""Run source-audited Chapter5 calculations instead of the superseded draft data."""
from pathlib import Path
import runpy
runpy.run_path(str(Path(__file__).with_name('verify_chapter05_theory_parent.py')),run_name='__main__')
