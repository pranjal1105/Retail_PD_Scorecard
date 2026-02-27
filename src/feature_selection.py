# src/feature_selection.py

def select_by_iv(iv_dict, threshold):
    return [k for k, v in iv_dict.items() if v >= threshold]