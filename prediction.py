import joblib
def predict(data):
    clf = joblib.load(r"C:\Users\rakes\Downloads\diabetes+130-us+hospitals+for+years+1999-2008 (1)\diabetic_data.csv")
    return clf.predict(data)
