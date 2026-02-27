# src/data_preprocessing.py

import pandas as pd
from sklearn.model_selection import train_test_split
from .config import TRAIN_SIZE, RANDOM_STATE


def split_data(df, target):
    X = df.drop(columns=[target])
    y = df[target]

    return train_test_split(
        X, y,
        train_size=TRAIN_SIZE,
        random_state=RANDOM_STATE,
        stratify=y
    )


def handle_missing(df):
    return df.fillna(df.median(numeric_only=True))