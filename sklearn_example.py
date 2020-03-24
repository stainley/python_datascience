from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_wine
from sklearn.metrics import accuracy_score

rf_model = RandomForestClassifier(random_state=1)

features, target = load_wine(return_X_y=True)

rf_model.fit(features, target)

preds = rf_model.predict(features)
preds

accc = accuracy_score(target, preds)
accc