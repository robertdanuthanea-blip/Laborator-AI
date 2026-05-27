from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

#ex1

iris = load_iris()
x=iris.data
y=iris.target   

print("Formua setului de date: ", x.shape)

print("\nDenumirilie atributelor:")
print(iris.feature_names)

print("\nClasele:")
print(iris.target_names)

#ex2

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
print("\nDimensiunea setului de antrenare: ", x_train.shape)
print("\nDimensiunea setului de testare: ", x_test.shape)
print(y_test.shape)
print(y_train.shape)
print(x)
print(y)

#ex3

scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)
print(x_train_scaled[:5])
print(x_test_scaled)

#ex4

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(x_train_scaled, y_train)
accuracy = knn.score(x_test_scaled, y_test)
print("\nAcuratetea modelului KNN: ", accuracy)