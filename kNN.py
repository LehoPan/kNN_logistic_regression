from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics

# Load in the scaled data and labels
data = []
labels = []
with open('./dataset/scaled.data') as input:
    for line in input:
        line = line.split(',')
        line = list(map(float, line))
        data.append(line)

with open('./dataset/labels.data') as input:
    line = input.readline()
    line = line.split(',')
    line = list(map(float, line))
    labels = line

# Split the data into training and testing sets, random_state is set here so I can have reproducable results
X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=42)

# Create a k-NN classifier
knn = KNeighborsClassifier(n_neighbors=3)

# Train the model
knn.fit(X_train, y_train)

# Make predictions on the test set
y_pred = knn.predict(X_test)

# Evaluate the model
print(f'Accuracy: {metrics.accuracy_score(y_test, y_pred)}')
print(f'Confusion Matrix:\n{metrics.confusion_matrix(y_test, y_pred)}')
print(f'Classification Report:\n{metrics.classification_report(y_test, y_pred)}')