from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt
import numpy as np

# 1. 
iris = load_iris()
X = iris.data
y = iris.target

print(X.shape)
print(iris.feature_names)
print(iris.target_names)

# 2.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(X_train.shape, y_train.shape)
print(X_test.shape, y_test.shape)

# 3. 
scaler = StandardScaler()
print(X_train[:3])

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
print(X_train_scaled[:3])

# 4. 
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train_scaled, y_train)

y_pred = knn.predict(X_test_scaled)
print(accuracy_score(y_test, y_pred))

# 5. 
k_values = range(1, 16)
accuracies = []

for k in k_values:
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(X_train_scaled, y_train)
    accuracies.append(accuracy_score(y_test, model.predict(X_test_scaled)))

plt.plot(k_values, accuracies, marker='o')
plt.show()

# 6. 
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred, target_names=iris.target_names))

# 7. 
X_2D = X[:, [2, 3]]
plt.scatter(X_2D[:, 0], X_2D[:, 1], c=y)
plt.show()

knn_2D = KNeighborsClassifier(n_neighbors=3)
knn_2D.fit(X_2D, y)

val1 = float(input())
val2 = float(input())
nou = np.array([[val1, val2]])
print(iris.target_names[knn_2D.predict(nou)[0]])