import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import joblib
import os

def main():
    data_path = "data/processed/vpn_flows.csv"
    if not os.path.exists(data_path):
        raise FileNotFoundError(f"{data_path} not found. Run extract_features.py first.")

    df = pd.read_csv(data_path)

    # Basic clean-up
    df = df.dropna()

    X = df.drop(columns=["label"])
    y = df["label"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, stratify=y, random_state=42
    )

    clf = RandomForestClassifier(
        n_estimators=200,
        max_depth=None,
        n_jobs=-1,
        random_state=42
    )

    clf.fit(X_train, y_train)

    y_pred = clf.predict(X_test)

    print("Classification report:")
    print(classification_report(y_test, y_pred))

    print("Confusion matrix:")
    print(confusion_matrix(y_test, y_pred))

    # Save model + feature order
    os.makedirs("models", exist_ok=True)
    joblib.dump(clf, "models/vpn_rf.joblib")
    joblib.dump(list(X.columns), "models/feature_order.joblib")
    print("Saved model → models/vpn_rf.joblib")
    print("Saved feature order → models/feature_order.joblib")

if __name__ == "__main__":
    main()
