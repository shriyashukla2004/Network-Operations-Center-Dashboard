from sklearn.ensemble import IsolationForest
import numpy as np

X = np.array([[0.03],[0.04],[0.05],[0.50],[0.60]])

model = IsolationForest()

model.fit(X)

print(model.predict(X))