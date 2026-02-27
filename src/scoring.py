# src/scoring.py

import numpy as np
from .config import BASE_SCORE, PDO, BASE_ODDS


def calculate_factor_offset():
    factor = PDO / np.log(2)
    offset = BASE_SCORE - factor * np.log(BASE_ODDS)
    return factor, offset


def generate_score(log_odds):
    factor, offset = calculate_factor_offset()
    return offset + factor * log_odds