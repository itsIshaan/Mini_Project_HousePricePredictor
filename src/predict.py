import numpy as np

from src.train_model import train_model


def predict_house(features):

    # Train model
    model, X_test, y_test, y_pred = train_model()

    # Convert input into NumPy array
    features = np.array(features).reshape(1, -1)

    # Predict price
    prediction = model.predict(features)

    # Dataset target is in units of $100,000
    price = prediction[0] * 100000

    return price


if __name__ == "__main__":

    # Example house
    # Features:
    # MedInc, HouseAge, AveRooms, AveBedrms,
    # Population, AveOccup, Latitude, Longitude

    example_house = [
        5.0,
        20.0,
        6.0,
        1.0,
        1000.0,
        3.0,
        34.0,
        -118.0
    ]

    price = predict_house(example_house)

    print(f"\nPredicted House Price: ${price:,.2f}")