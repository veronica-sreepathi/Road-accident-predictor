from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib # Useful for saving and loading models

def train_model(X_train, y_train, random_state=42):
    """
    Initializes and trains a Random Forest Classifier.
    """
    model = RandomForestClassifier(
        n_estimators=100, 
        random_state=random_state, 
        class_weight='balanced' 
    )
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    """
    Evaluates the model and prints the results.
    """
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred, zero_division=0)
    
    print(f"\n## Model Evaluation Results 📈")
    print(f"Accuracy: {accuracy:.4f}")
    print("\nClassification Report:\n")
    print(report)

def save_model(model, filename='accident_predictor_model.joblib'):
    """
    Saves the trained model to a file using joblib.
    """
    joblib.dump(model, filename)
    print(f"\nModel successfully saved to {filename}")

def load_model(filename='accident_predictor_model.joblib'):
    """
    Loads a saved model from a file.
    """
    return joblib.load(filename)
