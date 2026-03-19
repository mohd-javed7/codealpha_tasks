import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, root_mean_squared_error, r2_score


df = pd.read_csv("cleaned_data.csv")

X = df.drop('Selling_Price',axis=1)
Y = df['Selling_Price']

X_train, X_test, Y_train, Y_test = train_test_split(
    X,Y, test_size=0.2, random_state=42
)

RF = RandomForestRegressor(
    n_estimators=500,
    max_depth=10,
    min_samples_split=5,
    min_samples_leaf=2,
    random_state=42
)

RF.fit(X_train,Y_train)
y_pred_rf = RF.predict(X_test)

print("MAE: ",mean_absolute_error(Y_test,y_pred_rf))
print("RMSE: ",root_mean_squared_error(Y_test,y_pred_rf))
print("R2 score: ",r2_score(Y_test,y_pred_rf))