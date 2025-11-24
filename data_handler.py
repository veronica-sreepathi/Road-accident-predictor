import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np

def generate_and_preprocess_data(data_size=1000, test_size=0.3, random_state=42):
    """
    Generates synthetic accident data, performs preprocessing (One-Hot Encoding),
    and splits the data into training and testing sets.
    """
    # 1. Generate Synthetic Data
    data = {
        'Time_of_Day': np.random.choice(['Morning', 'Afternoon', 'Evening', 'Night'], size=data_size),
        'Weather_Condition': np.random.choice(['Clear', 'Rainy', 'Foggy', 'Snowy'], size=data_size),
        'Road_Surface': np.random.choice(['Dry', 'Wet', 'Icy'], size=data_size),
        'Speed_Limit': np.random.randint(20, 70, size=data_size),
        'Accident_Severity': np.random.choice([0, 1, 2], size=data_size, p=[0.6, 0.3, 0.1])
    }
    df = pd.DataFrame(data)

    # 2. Define features (X) and target (y)
    X = df.drop('Accident_Severity', axis=1)
    y = df['Accident_Severity']

    # 3. One-Hot Encoding for categorical features
    X = pd.get_dummies(X, columns=['Time_of_Day', 'Weather_Condition', 'Road_Surface'], drop_first=True)

    # 4. Split the data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y
    )

    return X_train, X_test, y_train, y_test

def preprocess_new_data(new_data, X_train_cols):
    """
    Applies the same One-Hot Encoding to a single new data point and aligns columns.
    """
    new_data_encoded = pd.get_dummies(new_data, columns=['Time_of_Day', 'Weather_Condition', 'Road_Surface'], drop_first=True)

    # Align columns to match the training data
    missing_cols = set(X_train_cols) - set(new_data_encoded.columns)
    for col in missing_cols:
        new_data_encoded[col] = 0

    new_data_encoded = new_data_encoded[X_train_cols]
    return new_data_encoded