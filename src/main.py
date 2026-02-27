# main.py

import pandas as pd
from src.pipeline import run_pipeline

df = pd.read_csv("data/application_data.csv")

model, auc = run_pipeline(df, "TARGET")

print(f"AUC: {auc:.4f}")