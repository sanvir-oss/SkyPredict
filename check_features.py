

import joblib

features = joblib.load("flight_features (1).pkl")

print("Total features:", len(features))
print(features[:50])



print("\nLast 60 features:")
print(features[-60:])
