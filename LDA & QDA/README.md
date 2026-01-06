# LDA and QDA Classification using Iris Dataset

## 🧠 Overview

This project demonstrates how LDA and QDA can be applied to a real-world dataset (Iris dataset) to classify flower species based on sepal and petal measurements. It includes:

* Training and testing of both classifiers
* Accuracy comparison
* Prediction for a new (real-time–like) flower measurement

---

## 📂 Dataset

* **Dataset**: Iris Dataset (built-in from `sklearn.datasets`)
* **Features**:

  * Sepal length
  * Sepal width
  * Petal length
  * Petal width
* **Classes**:

  * Setosa
  * Versicolor
  * Virginica

---

## ⚙️ Algorithms Used

### 1. Linear Discriminant Analysis (LDA)

* Assumes all classes share the same covariance matrix
* Produces linear decision boundaries
* Efficient and works well when class distributions are similar

### 2. Quadratic Discriminant Analysis (QDA)

* Allows each class to have its own covariance matrix
* Produces quadratic decision boundaries
* More flexible but computationally heavier than LDA

---

## 🛠️ Technologies & Libraries

* Python 3.x
* scikit-learn
* NumPy (indirect dependency)

---

## 🚀 How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/ramasamy-24-t/Machine-Learning
   ```

2. Navigate to the project directory:

   ```bash
   cd LDA & QDA
   ```

3. Install required dependencies:

   ```bash
   pip install scikit-learn
   ```

4. Run the Python script:

   ```bash
   python lda_qda_iris.py
   ```

---

## 📊 Output

* Accuracy of LDA model
* Accuracy of QDA model
* Predicted flower species for a new input sample using both models

---

## 🧪 Sample Input

```text
[5.8, 2.7, 5.1, 1.9]
```

---

## ✅ Conclusion

* LDA is simpler and faster when assumptions are met
* QDA provides better flexibility for complex class distributions
* Both models perform well on the Iris dataset

---

## 📚 References

* [https://scikit-learn.org/stable/modules/lda_qda.html](https://scikit-learn.org/stable/modules/lda_qda.html)
* Fisher, R. A. (1936). *The use of multiple measurements in taxonomic problems*

---

## 👤 Author

Ram

---

⭐ If you find this useful, feel free to star the repository!