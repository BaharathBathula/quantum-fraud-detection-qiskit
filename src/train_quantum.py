import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report

from qiskit.circuit.library import ZZFeatureMap
from qiskit_machine_learning.kernels import FidelityQuantumKernel
from qiskit_machine_learning.algorithms import QSVC


def load_data():
    url = "https://storage.googleapis.com/download.tensorflow.org/data/creditcard.csv"
    data = pd.read_csv(url)

    # Small balanced sample for demo
    data = data.groupby("Class", group_keys=False).apply(
        lambda x: x.sample(min(len(x), 15), random_state=42)
    ).reset_index(drop=True)

    X = data.drop("Class", axis=1)
    y = data["Class"]

    X = X.iloc[:, :2]

    scaler = StandardScaler()
    X = scaler.fit_transform(X)

    return train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )


def main():
    X_train, X_test, y_train, y_test = load_data()

    feature_map = ZZFeatureMap(feature_dimension=2, reps=2)
    quantum_kernel = FidelityQuantumKernel(feature_map=feature_map)

    model = QSVC(quantum_kernel=quantum_kernel)
    model.fit(X_train, y_train)

    preds = model.predict(X_test)

    print("Quantum QSVC Accuracy:", accuracy_score(y_test, preds))
    print(classification_report(y_test, preds, zero_division=0))


if __name__ == "__main__":
    main()
