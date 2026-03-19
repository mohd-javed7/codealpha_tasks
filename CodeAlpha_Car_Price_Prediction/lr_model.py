import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, root_mean_squared_error, r2_score

df = pd.read_csv("cleaned_data.csv")

X = df.drop('Selling_Price',axis=1)
Y = df['Selling_Price']

X_train, X_test, Y_train, Y_test = train_test_split(
    X,Y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train,Y_train)
y_pred = model.predict(X_test)

print("MAE: ",mean_absolute_error(Y_test,y_pred))
print("RMSE: ",root_mean_squared_error(Y_test, y_pred))
print("R2 Score: ",r2_score(Y_test,y_pred))