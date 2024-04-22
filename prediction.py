import joblib
def predict(data):
    clf = joblib.load("Diabetes.csv")
    return clf.predict(data)
