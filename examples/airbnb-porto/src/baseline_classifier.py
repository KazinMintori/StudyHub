"""StudyHub Porto Airbnb Educational Pipeline - Baseline Classifier Module.

Implements a rule-based sentiment, aspect, and language classification baseline
in Python standard library using PT/EN lexicons and heuristic keyword matching.
Explicitly documented as a weak baseline for pedagogical comparison.
"""

from __future__ import annotations

import re
from typing import Any, Dict, List, Set

# Lexicons
PT_POSITIVE_WORDS = {
    "bom", "boa", "bons", "boas", "ótimo", "ótima", "ótimos", "ótimas",
    "excelente", "excelentes", "perfeito", "perfeita", "maravilhoso", "maravilhosa",
    "adorei", "adoramos", "recomendo", "recomendamos", "limpo", "limpa",
    "agradável", "incrível", "fantástico", "fantástica", "gostei", "tranquilo",
    "confortável", "acolhedor", "acolhedora", "simpatia", "amável",
}

PT_NEGATIVE_WORDS = {
    "mau", "má", "ruim", "péssimo", "péssima", "sujo", "suja", "sujeira",
    "barulho", "barulhento", "barulhenta", "horrível", "terrível", "pior",
    "desagradável", "problema", "problemas", "decepcionante", "frio", "quente",
    "quebrado", "estragado", "mofo", "cheiro", "fedorento", "escuro", "estreito",
}

EN_POSITIVE_WORDS = {
    "great", "good", "excellent", "wonderful", "perfect", "lovely", "clean",
    "comfortable", "amazing", "recommend", "recommended", "super", "nice",
    "friendly", "helpful", "convenient", "fantastic", "spotless", "quiet",
    "beautiful", "enjoyed", "loved", "easy", "pleasant", "best",
}

EN_NEGATIVE_WORDS = {
    "bad", "terrible", "horrible", "dirty", "noisy", "loud", "poor",
    "broken", "worst", "uncomfortable", "smell", "cold", "disappointing",
    "disappointment", "small", "issue", "issues", "problem", "problems",
    "rude", "unresponsive", "waste", "avoid",
}

# Stopwords for language identification
PT_STOPWORDS = {
    "o", "a", "os", "as", "um", "uma", "de", "do", "da", "dos", "das",
    "em", "no", "na", "nos", "nas", "para", "com", "por", "que", "é",
    "não", "se", "como", "mas", "muito", "mais", "foi", "estava", "tudo",
}

EN_STOPWORDS = {
    "the", "a", "an", "and", "or", "in", "on", "at", "to", "for",
    "with", "is", "was", "are", "were", "it", "this", "that", "we",
    "our", "very", "had", "from", "by", "as", "but", "not",
}

# Aspect Keywords
ASPECT_KEYWORDS = {
    "location": {
        "metro", "trindade", "ribeira", "centro", "downtown", "center", "location",
        "localização", "walking", "walk", "close", "perto", "beach", "station",
    },
    "cleanliness": {
        "clean", "limpo", "limpa", "limpeza", "spotless", "dirty", "sujo", "suja",
        "smell", "mofo", "dust", "poeira",
    },
    "host": {
        "host", "anfitrião", "anfitriã", "communication", "comunicação", "checkin",
        "check-in", "friendly", "helpful", "simpatia", "welcome", "recepção",
    },
    "amenities": {
        "wifi", "internet", "shower", "chuveiro", "bed", "cama", "kitchen", "cozinha",
        "ac", "heating", "aquecimento", "towels", "toalhas",
    },
    "noise": {
        "noise", "noisy", "loud", "barulho", "barulhento", "quiet", "silencioso",
        "tranquilo", "calm", "rua", "street",
    },
}


def tokenize(text: str) -> List[str]:
    """Tokenize lowercase text into words."""
    return re.findall(r"\b\w+\b", text.lower())


def detect_heuristic_language(words: List[str]) -> str:
    """Classify language heuristically based on stopword overlap."""
    pt_matches = sum(1 for w in words if w in PT_STOPWORDS)
    en_matches = sum(1 for w in words if w in EN_STOPWORDS)

    if pt_matches > en_matches and pt_matches >= 2:
        return "pt"
    if en_matches > pt_matches and en_matches >= 2:
        return "en"
    return "other"


def classify_review_baseline(review_id: str, comments: str) -> Dict[str, Any]:
    """Classify review sentiment, aspects, and language using rule-based heuristics."""
    words = tokenize(comments)
    word_set = set(words)

    # 1. Language detection
    lang = detect_heuristic_language(words)

    # 2. Sentiment scoring
    pos_score = sum(1 for w in words if w in PT_POSITIVE_WORDS or w in EN_POSITIVE_WORDS)
    neg_score = sum(1 for w in words if w in PT_NEGATIVE_WORDS or w in EN_NEGATIVE_WORDS)

    if pos_score >= neg_score + 2:
        sentiment = "positive"
    elif neg_score >= pos_score + 1:
        sentiment = "negative"
    elif pos_score > 0 and neg_score > 0:
        sentiment = "mixed"
    elif pos_score > 0:
        sentiment = "positive"
    elif neg_score > 0:
        sentiment = "negative"
    else:
        # Default neutral/mixed if no lexicon match
        sentiment = "mixed"

    # 3. Aspect extraction & polarity
    detected_aspects: List[Dict[str, str]] = []
    for aspect_name, keywords in ASPECT_KEYWORDS.items():
        if any(kw in word_set for kw in keywords):
            # Assign polarity aligned with overall or local sentiment
            pol = "criticized" if sentiment == "negative" else "praised"
            detected_aspects.append({"aspect": aspect_name, "polarity": pol})

    return {
        "review_id": review_id,
        "sentiment": sentiment,
        "aspects": detected_aspects,
        "language": lang,
        "model": "rule_based_baseline_lexicon",
    }
