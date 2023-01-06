# Telco Customer Churn

# Project Description

The Telco company has been losing customers and does not know why.  Using the account information for each customer. I will compare different services that each customer pays for. A service or customer data could potentially increase or decrease the chance that a customer will churn.

# Project Goal

* Find drivers of churn
* User drivers to create ML models

# Initial Thoughts

My initial hypothesis is that drivers of churn will be descriptions of customers that isolate them in groups with higher likelihood of leaving the company.

# The Plan

* Aquire data from SQL database
 
* Prepare data
   * Left Join additional customer info to `customers` table
   * Drop redundant columns in dataframe using Pandas
 
* Explore data in search of drivers of upsets
   * Answer the following initial questions
       * How often does churn occur?
       * Does gender & total charge affect churn?
       * Does join date affect churn?
       * Does total addons affect churn?
       * Does total deviation from average of `total_charges` affect churn?
       * Does having tech support and  being a senior citizen effect churn?
       * Does being a senior citizen affect churn?
       * Is tenure important driving churn?
       * Is paperless_billing, payment_type related?
       * Does having `dependents` & `multiple_lines` correlate to churn?

* Develop a Model to predict churn
   * Use drivers identified in _**explore**_ to build predictive models of different types
   * Evaluate models on train and validate data
   * Select the best model based on highest accuracy
   * Evaluate the best model on test data
 
* Draw conclusions

# Data Dictionary
| Feature | Definition |
|:--------|:-----------|
|customer_id| unique indentifier |
|gender| customer gender |
|senior_citizen| customer age status |
|dependents| customer total number of dependents |
|tenure| customer length of contract |
|phone_service| customer phone service status |
|multiple_lines| customer additional phone lines |
|online_security| does customer have online security |
|online_backup| does customer have online backup |
|device_protection| does customer have device protection |
|tech_support| does customer have tech suport |
|streaming_tv| does customer have streaming tv addon service |
|streaming_movies| does customer have streaming movies addon service |
|paperless_billing| does customer have paperless billing feature |
|monthly_charges| what customer pays every month |
|total_charges| sum of all monthly charges in tenure |
|churn| If customer left the company `churn` = 1, otherwise = 0 |
|internet_service_type| does customer have internet service |
|payment_type| customer form of payment for service |
|contract_type| does customer have monthly or annual contract |
| addon_sum | total count of additional service besides phone and internet|

# Steps to Reproduce
1) Clone this repo.
2) Acquire the data from Codeup SQL Database
3) Put the data in the file containing the cloned repo.
4) Run notebook.

# Takeaways and Conclusions
* churn makes up 26.54% of the data 
* by guessing not churn for every customer one could achieve an accuracy of 73.46%
* 73.46% was the baseline accuracy
* Total churn = 1869 out of 7043 customers.
<br>

* Out of the Random Forest, KNN, and Logistic Regression models Random Forest performed higher than baseline on train and validate
* The Logistic Regression model performed slightly better on validate data but was worse than baseline on either one.

# Recommendations
* For loop chi square all categorical features against churn, and sort each feature by accuracy
* Explore further numerical features
* Look for other ways to calculate "Total Charges" Such as standard deviation from the mean and compare against churn
