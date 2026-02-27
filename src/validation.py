# src/validation.py

from sklearn.metrics import roc_auc_score


def calculate_auc(y_true, y_pred):
    return roc_auc_score(y_true, y_pred)


def ks_statistic(y_true, y_prob):
    import pandas as pd
    df = pd.DataFrame({"y": y_true, "prob": y_prob})
    df = df.sort_values("prob", ascending=False)
    df["cum_good"] = (1 - df["y"]).cumsum() / (1 - df["y"]).sum()
    df["cum_bad"] = df["y"].cumsum() / df["y"].sum()
    return max(abs(df["cum_good"] - df["cum_bad"]))