SELECT
    *
FROM
    customers AS c
    LEFT JOIN internet_service_types AS ist USING (internet_service_type_id)
    LEFT JOIN customer_subscriptions AS csb USING (customer_id)
    LEFT JOIN payment_types AS pt USING (payment_type_id)
    LEFT JOIN contract_types AS ct USING (contract_type_id)
    LEFT JOIN customer_churn AS ccr USING (customer_id)
    LEFT JOIN customer_contracts AS ccn USING (customer_id)
    LEFT JOIN customer_details AS cd USING (customer_id)
    LEFT JOIN customer_payments AS cp USING (customer_id)
    LEFT JOIN customer_signups AS cs USING (customer_id);

