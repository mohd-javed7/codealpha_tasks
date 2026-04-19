# A/B Testing Analysis

## 📌 Objective
The objective of this project is to evaluate whether a new version of a webpage (treatment) performs better than the existing version (control) in terms of user conversion.

---

## 📊 Dataset
The dataset contains user-level information including:
- `user_id`
- `timestamp`
- `group` (control or treatment)
- `landing_page` (old_page or new_page)
- `converted` (0 = not converted, 1 = converted)

---

## 🧪 Methodology
The following steps were performed:

1. Data loading and initial inspection  
2. Checking for missing values and duplicates  
3. Data cleaning to ensure consistency  
4. Splitting data into control and treatment groups  
5. Calculating conversion rates  
6. Performing hypothesis testing using a t-test  
7. Visualizing the results using plots  

---

## 📈 Results

- **Control Conversion Rate (A):** 12.03%  
- **Treatment Conversion Rate (B):** 11.89%  

The control group shows a slightly higher conversion rate than the treatment group. However, the difference is extremely small and not visually distinguishable.

---

## 📉 Statistical Analysis

A t-test was conducted to compare the conversion rates:

- **t-statistic:** 1.2369  
- **p-value:** 0.2161  

Since the p-value is greater than 0.05, the difference between the two groups is not statistically significant.

---

## 📊 Visualization

Visualizations were created to compare:
- Conversion rates between groups  
- Total conversions  
- Distribution of conversions  

The graphs show that both groups perform almost identically, supporting the statistical findings.

---

## ✅ Conclusion

There is no sufficient evidence to conclude that the new version (treatment) performs better than the existing version (control).

👉 Therefore, the current version should be retained.

---

## 📂 Project Structure

- notebook.ipynb → Complete analysis notebook  
- ab_data.csv → Dataset  
- README.md → Project documentation  


---

## 🚀 Tools & Libraries Used

- Python  
- Pandas  
- NumPy  
- SciPy  
- Matplotlib  
- Seaborn  
