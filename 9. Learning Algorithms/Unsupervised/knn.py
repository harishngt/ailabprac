import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier



x = [1,2,2,1,8,9,8,9]
y = [1,2,1,2,8,9,9,8]
classes = [0,0,0,0,1,1,1,1]
plt.scatter(x,y,c=classes)
plt.show()

data = list(zip(x,y))
knn = KNeighborsClassifier(n_neighbors=2)
knn.fit(data,classes)

new_x = 8.5
new_y = 8.5

new_point = [(new_x,new_y)]
prediction = knn.predict(new_point)
print(prediction)

