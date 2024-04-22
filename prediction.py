import joblib
def predict(data):
    clf = joblib.load("Diabetes.sav")
    return clf.predict(data)
