# src/model.py

import statsmodels.api as sm


def train_logistic(X, y):
    X_const = sm.add_constant(X)
    model = sm.Logit(y, X_const).fit(disp=False)
    return model


def get_coefficients(model):
    return model.params