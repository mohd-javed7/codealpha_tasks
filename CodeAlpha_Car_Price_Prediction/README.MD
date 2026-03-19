## Model Comparison and Final Conclusion

Two regression models were trained and evaluated to predict the selling price of used cars: **Linear Regression** and **Random Forest Regressor**.

| Model | MAE | RMSE | R² |
|------|------|------|------|
| Linear Regression | 1.47 | 2.52 | **0.75** |
| Random Forest | 1.35 | 3.15 | 0.61 |

The **Linear Regression model achieved a higher R² score of 0.75**, meaning it was able to explain approximately **75% of the variance in car selling prices**, while the Random Forest model explained about **61%**.

Correlation analysis revealed that **Present_Price has a very strong positive correlation with Selling_Price (0.87)**, indicating that the resale value of a car is heavily influenced by its original showroom price. Because this relationship is largely linear, Linear Regression was able to capture it more effectively than the Random Forest model.

Other factors such as **fuel type, transmission type, seller type, and vehicle age** also contributed to price prediction but had a comparatively smaller influence.

Although Random Forest is capable of modeling complex non-linear relationships, it did not outperform Linear Regression in this case. This is likely due to the **relatively small dataset size and the predominantly linear relationship between the key features and the target variable**.

Based on the evaluation results, **Linear Regression was selected as the final model for predicting car selling prices**.

This project demonstrates how machine learning can be applied to estimate vehicle resale values and highlights the key factors that influence car pricing in the used car market.