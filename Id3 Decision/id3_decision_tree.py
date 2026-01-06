import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import OrdinalEncoder

def make_data():
    return pd.DataFrame({
        "att": ["High", "High", "Low", "High", "Low", "Low", "High"],
        "study": ["Yes", "No", "Yes", "Yes", "No", "Yes", "No"],
        "marks": ["Good", "Good", "Poor", "Good", "Poor", "Poor", "Good"],
        "out": ["Pass", "Pass", "Fail", "Pass", "Fail", "Fail", "Pass"]
    })

def encode(df):
    enc = OrdinalEncoder()
    arr = enc.fit_transform(df)
    return pd.DataFrame(arr, columns=df.columns)

df = make_data()
enc_df = encode(df)

X = enc_df.iloc[:, :-1]
y = enc_df.iloc[:, -1]

clf = DecisionTreeClassifier(criterion="entropy", max_depth=3)
clf.fit(X, y)

test = [[1, 1, 0]]
res = clf.predict(test)

print("Pass" if res[0] == 1 else "Fail")
