import pandas as pd
# Import functions from the data and model modules
from data_handler import generate_and_preprocess_data, preprocess_new_data
from model_trainer import train_model, evaluate_model, save_model

def main():
    print("--- 1. Data Loading and Preparation ---")
    X_train, X_test, y_train, y_test = generate_and_preprocess_data()
    print(f"Training features shape: {X_train.shape}")

    print("\n--- 2. Model Training and Evaluation ---")
    model = train_model(X_train, y_train)
    evaluate_model(model, X_test, y_test)
    
    # Optional: Save the trained model for later use
    save_model(model) 

    print("\n--- 3. Example Prediction on a New Scenario ---")
    
    # Define a new data point
    new_data = pd.DataFrame({
        'Time_of_Day': ['Night'], 
        'Weather_Condition': ['Snowy'], 
        'Road_Surface': ['Icy'], 
        'Speed_Limit': [45]
    })
    
    # Preprocess the new data using the helper function
    new_data_encoded = preprocess_new_data(new_data, X_train.columns)
    
    # Make the prediction
    prediction = model.predict(new_data_encoded)
    
    # Map the numerical prediction back to a readable severity level
    severity_map = {0: 'No Injury', 1: 'Minor Injury', 2: 'Serious Injury'}

    print(f"Scenario: Night, Snowy, Icy Road, Speed 45")
    print(f"Predicted Accident Severity: **{severity_map[prediction[0]]}**")

if __name__ == "__main__":
    main()