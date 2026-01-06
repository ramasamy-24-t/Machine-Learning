from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.metrics import accuracy_score

iris = load_iris()
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

lda = LinearDiscriminantAnalysis()
lda.fit(X_train, y_train)

y_pred_lda = lda.predict(X_test)
print("LDA Accuracy:", accuracy_score(y_test, y_pred_lda))

new_flower = [[5.8, 2.7, 5.1, 1.9]]
prediction_lda = lda.predict(new_flower)
print("Predicted Flower (LDA):", iris.target_names[prediction_lda][0])

qda = QuadraticDiscriminantAnalysis()
qda.fit(X_train, y_train)

y_pred_qda = qda.predict(X_test)
print("QDA Accuracy:", accuracy_score(y_test, y_pred_qda))

prediction_qda = qda.predict(new_flower)
print("Predicted Flower (QDA):", iris.target_names[prediction_qda][0])
