import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split


def load_and_prepare_data():
    # Load California Housing dataset
    housing = fetch_california_housing()

    # Create DataFrame
    df = pd.DataFrame(
        housing.data,
        columns=housing.feature_names
    )

    # Add target column
    df["Price"] = housing.target

    # Separate features and target
    X = df.drop("Price", axis=1)
    y = df["Price"]

    # Split dataset into training and testing data
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    return X_train, X_test, y_train, y_test, df