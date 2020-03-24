from sklearn.datasets import load_breast_cancer

features, target = load_breast_cancer(return_X_y=True)

print(features)

print(target)

from sklearn.ensemble import RandomForestClassifier

seed = 888
rf_model = RandomForestClassifier(random_state=seed)

rf_model.fit(features, target)

preds = rf_model.predict(features)

print(preds)

from sklearn.metrics import accuracy_score

acc = accuracy_score(target, preds)

print(acc)