# Decision Tree Classification using ID3 Algorithm

## 🧠 Overview

This project demonstrates the implementation of the **ID3 decision tree algorithm** using entropy and information gain. A small real-time student performance dataset is used to predict whether a student will **Pass** or **Fail** based on academic attributes.

The implementation uses `scikit-learn`'s `DecisionTreeClassifier` with **entropy** as the splitting criterion, which closely represents the ID3 algorithm.

---

## 📂 Dataset Description

A manually created categorical dataset representing student performance:

### Features

* **Attendance**: High / Low
* **Study_Hours**: Yes / No
* **Internal_Marks**: Good / Poor

### Target

* **Result**: Pass / Fail

---

## ⚙️ Algorithm (ID3)

1. Start
2. Read the training dataset
3. Calculate the entropy of the target attribute
4. For each attribute:

   * Calculate entropy for each attribute value
   * Compute Information Gain
5. Select the attribute with maximum Information Gain
6. Make it the root node of the decision tree
7. Split the dataset based on the selected attribute
8. Repeat steps recursively for each subset
9. Stop when:

   * All samples belong to the same class, or
   * No attributes are left for splitting
10. Assign the majority class as a leaf node
11. End

---

## 🛠️ Technologies & Libraries

* Python 3.x
* pandas
* scikit-learn

---

## 🚀 How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/ramasamy-24-t/Machine-Learning
   ```

2. Navigate to the project directory:

   ```bash
   cd Id3 Decision
   ```

3. Install required dependencies:

   ```bash
   pip install pandas scikit-learn
   ```

4. Run the Python script:

   ```bash
   python id3_decision_tree.py
   ```

---

## 🧪 Sample Input (New Student)

```text
Attendance: High
Study Hours: Yes
Internal Marks: Poor
```

Encoded as:

```python
[1, 1, 0]
```

---

## 📊 Output

```text
Prediction: Pass
```

---

## ✅ Conclusion

* ID3 selects attributes using **Information Gain**
* Entropy helps measure impurity in the dataset
* Decision trees are easy to interpret and effective for categorical data
* The model successfully predicts student results based on academic attributes

---

## 📚 References

* [https://scikit-learn.org/stable/modules/tree.html](https://scikit-learn.org/stable/modules/tree.html)
* Quinlan, J. R. (1986). *Induction of Decision Trees*

---

## 👤 Author

Ram

---

⭐ If you find this project useful, consider starring the repository!
