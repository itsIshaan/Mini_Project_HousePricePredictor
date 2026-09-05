# House Price Predictor

A machine learning project that predicts house prices using the California Housing dataset and a Linear Regression model.

The project also includes a Streamlit web application that allows users to enter house and area details and receive an estimated house price.

---

## 1. Project Overview

The House Price Predictor uses machine learning to estimate house prices based on eight features from the California Housing dataset.

The project follows this workflow:

1. Load the California Housing dataset.
2. Prepare and process the data.
3. Split the dataset into training and testing sets.
4. Train a Linear Regression model.
5. Evaluate the model.
6. Accept user input through a Streamlit web application.
7. Predict and display the estimated house price.

---

## 2. Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit

---

## 3. Dataset

The project uses the California Housing dataset provided through Scikit-learn.

The model uses the following eight features:

| Feature      | Description                              |
| ------------ | ---------------------------------------- |
| `MedInc`     | Median income in the area                |
| `HouseAge`   | Median house age                         |
| `AveRooms`   | Average number of rooms per household    |
| `AveBedrms`  | Average number of bedrooms per household |
| `Population` | Population of the area                   |
| `AveOccup`   | Average number of people per household   |
| `Latitude`   | Latitude of the location                 |
| `Longitude`  | Longitude of the location                |

The target variable is:

```text
Price
```

The target price values are represented in units of **$100,000**.

For example:

```text
Price = 5.0
```

represents:

```text
$500,000
```

### Important

`MedInc` is different from the target `Price`.

For example:

```text
MedInc = 5.0
```

represents approximately:

```text
$50,000 median household income
```

It does **not** mean that the house costs $50,000.

---

## 4. Project Structure

```text
Mini_Project_HousePricePredictor/
│
├── src/
│   ├── data_preprocessing.py
│   ├── predict.py
│   └── train_model.py
│
├── main.py
├── README.md
└── requirements.txt
```

### File Descriptions

#### `main.py`

The main Streamlit application.

This file creates the web interface and allows the user to enter house information and receive a predicted house price.

#### `src/data_preprocessing.py`

Loads the California Housing dataset, creates the DataFrame, separates the features and target, and splits the data into training and testing sets.

#### `src/train_model.py`

Creates and trains the Linear Regression model.

It also calculates:

* MAE
* MSE
* RMSE
* R² Score

#### `src/predict.py`

Uses the trained model to make a prediction based on the eight input features.

#### `requirements.txt`

Contains the Python packages required to run the project.

#### `README.md`

Contains the documentation and instructions for the project.

---

## 5. Requirements

Before running the project, make sure Python is installed on your computer.

You also need:

* Visual Studio Code
* Python
* pip
* Streamlit
* Pandas
* NumPy
* Scikit-learn

The required Python packages are listed in:

```text
requirements.txt
```

---

## 6. Step-by-Step Installation

### Step 1: Open the Project

Open Visual Studio Code.

Open the project folder:

```text
Mini_Project_HousePricePredictor
```

Make sure the VS Code Explorer shows:

```text
src/
main.py
README.md
requirements.txt
```

---

### Step 2: Open the Terminal

In VS Code, select:

```text
Terminal → New Terminal
```

The terminal should be located inside the project folder.

For example:

```text
PS C:\Users\YourName\Documents\VSC\Mini_Project_HousePricePredictor>
```

---

### Step 3: Check Python

Run:

```powershell
python --version
```

You should see a Python version such as:

```text
Python 3.x.x
```

If `python` does not work, try:

```powershell
py --version
```

---

## 7. Install the Required Packages

The project includes a `requirements.txt` file.

Install all required packages using:

```powershell
python -m pip install -r requirements.txt
```

If `python` does not work, try:

```powershell
py -m pip install -r requirements.txt
```

This installs the packages required by the project.

---

## 8. Check Streamlit Installation

After installing the packages, check whether Streamlit is available.

Run:

```powershell
python -m streamlit --version
```

If that does not work, try:

```powershell
py -m streamlit --version
```

You should see something similar to:

```text
Streamlit, version x.x.x
```

---

## 9. Launch the Streamlit Application

Make sure the terminal is inside the main project folder:

```text
Mini_Project_HousePricePredictor
```

Then run:

```powershell
python -m streamlit run main.py
```

Alternatively, if the `streamlit` command is available directly:

```powershell
streamlit run main.py
```

If the `streamlit` command is not recognized, use:

```powershell
python -m streamlit run main.py
```

---

## 10. Open the Website

After launching Streamlit, the terminal will display a local URL.

It will normally look like:

```text
http://localhost:8501
```

Open the URL in a web browser.

The House Price Predictor application should appear.

---

## 11. Using the Application

The application asks the user to enter eight values:

1. Median Income
2. House Age
3. Average Rooms
4. Average Bedrooms
5. Population
6. Average Occupancy
7. Latitude
8. Longitude

After entering the values, click:

```text
Predict House Price
```

The application will calculate and display the estimated house price.

---

## 12. Example Test Data

Use the following values for your first test:

```text
Median Income:       5.0
House Age:           20
Average Rooms:       6.0
Average Bedrooms:    1.0
Population:          1000
Average Occupancy:   3.0
Latitude:            34.0
Longitude:           -118.0
```

Then click:

```text
Predict House Price
```

The application should display an estimated house price.

---

## 13. Additional Test Data

### Test 1 - Higher Income Area

```text
Median Income:       8.0
House Age:           10
Average Rooms:       8.0
Average Bedrooms:    1.5
Population:          1500
Average Occupancy:   2.5
Latitude:            34.1
Longitude:           -118.2
```

### Test 2 - Lower Income Area

```text
Median Income:       2.0
House Age:           30
Average Rooms:       4.5
Average Bedrooms:    1.0
Population:          2000
Average Occupancy:   4.0
Latitude:            34.0
Longitude:           -118.0
```

### Test 3 - Another Example

```text
Median Income:       6.5
House Age:           15
Average Rooms:       7.0
Average Bedrooms:    1.2
Population:          1200
Average Occupancy:   2.8
Latitude:            37.8
Longitude:           -122.4
```

---

## 14. Understanding the Inputs

### Median Income

`MedInc` represents the median income in the area.

For example:

```text
MedInc = 5.0
```

represents approximately:

```text
$50,000
```

median household income.

### House Age

The median age of houses in the area.

Example:

```text
HouseAge = 20
```

means the houses in the area have a median age of approximately 20 years.

### Average Rooms

Average number of rooms per household.

Example:

```text
AveRooms = 6.0
```

### Average Bedrooms

Average number of bedrooms per household.

Example:

```text
AveBedrms = 1.0
```

### Population

Population of the area.

Example:

```text
Population = 1000
```

### Average Occupancy

Average number of people living in a household.

Example:

```text
AveOccup = 3.0
```

### Latitude and Longitude

These represent the geographical location of the area.

Example:

```text
Latitude = 34.0
Longitude = -118.0
```

---

## 15. Machine Learning Model

The project uses:

```text
Linear Regression
```

from Scikit-learn.

The dataset is divided into:

```text
80% Training Data
20% Testing Data
```

The model learns patterns from the training data and is evaluated using the testing data.

---

## 16. Model Evaluation

The project calculates the following evaluation metrics:

### MAE

Mean Absolute Error.

Measures the average absolute difference between actual and predicted values.

### MSE

Mean Squared Error.

Measures the average squared difference between actual and predicted values.

### RMSE

Root Mean Squared Error.

The square root of MSE.

### R² Score

Measures how well the model explains the variation in the target values.

---

## 17. Running Individual Python Files

The project can also be tested without Streamlit.

### Run the Training Program

From the main project folder:

```powershell
python src/train_model.py
```

This trains the Linear Regression model and displays the evaluation metrics.

---

### Run the Prediction Program

From the main project folder:

```powershell
python src/predict.py
```

This uses the example house data in `predict.py` and displays a predicted house price.

---

### Run the Streamlit Application

From the main project folder:

```powershell
python -m streamlit run main.py
```

This launches the graphical web application.

---

## 18. Complete Command Sequence

For a fresh setup, the commands can be run in this order:

```powershell
python --version
```

```powershell
python -m pip install -r requirements.txt
```

```powershell
python -m streamlit --version
```

```powershell
python src/train_model.py
```

```powershell
python src/predict.py
```

Finally:

```powershell
python -m streamlit run main.py
```

---

## 19. Stopping the Streamlit Application

To stop the Streamlit server, return to the VS Code terminal and press:

```text
Ctrl + C
```

---

## 20. Troubleshooting

### `streamlit` is not recognized

If you get:

```text
streamlit : The term 'streamlit' is not recognized...
```

use:

```powershell
python -m streamlit run main.py
```

instead of:

```powershell
streamlit run main.py
```

---

### Python is not recognized

Try:

```powershell
py --version
```

If `py` works, use:

```powershell
py -m pip install -r requirements.txt
```

and:

```powershell
py -m streamlit run main.py
```

---

### Package is missing

If you receive an error such as:

```text
ModuleNotFoundError
```

install the required packages again:

```powershell
python -m pip install -r requirements.txt
```

---

## 21. Future Improvements

Possible improvements include:

* Saving the trained model instead of retraining it for every prediction
* Comparing Linear Regression with other machine learning algorithms
* Improving prediction accuracy
* Adding data visualizations
* Improving the Streamlit user interface
* Adding charts showing the relationship between features and house prices
* Adding more detailed prediction information

---

## 22. Project Purpose

The purpose of this project is to demonstrate:

* Data preprocessing
* Machine learning
* Linear Regression
* Model evaluation
* Making predictions
* Python programming
* Building an interactive web application using Streamlit
