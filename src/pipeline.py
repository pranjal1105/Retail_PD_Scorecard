# src/pipeline.py

from .data_preprocessing import split_data, handle_missing
from .model import train_logistic
from .validation import calculate_auc


def run_pipeline(df, target):
    X_train, X_test, y_train, y_test = split_data(df, target)

    X_train = handle_missing(X_train)
    X_test = handle_missing(X_test)

    model = train_logistic(X_train, y_train)

    train_pred = model.predict()
    auc = calculate_auc(y_train, train_pred)

    return model, auc