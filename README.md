# hk_ipo_prediction

Predict first day performance of Hong Kong IPO stocks: A pipeline example of machine learning projects.


### Procedures:

1. Crawl, Parse and Clean Hong Kong IPO data from AAStocks.com using selenium webdriver and phantomjs (around 400 data points).

2. Use pandas for data cleaning and feature engineering, including feature selection and handling big values, missing values and categorical values (one hot encoding)

3. Use xgboost for regression model to predict first day performance. Generated feature importance plot is very interesting (blame matplotlib for not showing Chinese characters properly...)

![Feature Importance Plot](https://raw.githubusercontent.com/crownpku/hk_ipo_prediction/master/img/feature_importance.png)