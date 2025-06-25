import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.svm import SVR
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.neural_network import MLPRegressor
from xgboost import XGBRegressor
from lightgbm import LGBMRegressor
from sklearn.ensemble import StackingRegressor
from sklearn.metrics import mean_squared_error


def train_and_save_best_model():
    # Cargar datos
    df = pd.read_csv('Students_Social_Media_Addiction_Preprocessed.csv')

    # Separar características y target
    X = df.drop('Addicted_Score', axis=1)
    y = df['Addicted_Score']

    # Dividir datos
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Modelos base para stacking
    base_models = [
        ('rf', RandomForestRegressor(n_estimators=100)),
        ('xgb', XGBRegressor(n_estimators=100)),
        ('svr', SVR(kernel='rbf'))
    ]

    # Modelo de stacking
    stacking_model = StackingRegressor(
        estimators=base_models,
        final_estimator=LinearRegression()
    )

    # Entrenar modelo
    stacking_model.fit(X_train, y_train)

    # Evaluar modelo
    y_pred = stacking_model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    print(f"Model MSE: {mse:.4f}")

    # Guardar modelo
    joblib.dump(stacking_model, 'ml_model/trained_model.pkl')
    print("Model trained and saved successfully!")

    return stacking_model


if __name__ == "__main__":
    train_and_save_best_model()