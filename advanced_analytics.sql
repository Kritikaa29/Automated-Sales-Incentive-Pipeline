-- 1. Create a View for Dynamic Real-Time Reporting
CREATE OR REPLACE VIEW regional_sales_performance AS

WITH EmployeeAggregates AS (
    -- Step A: Aggregate total sales and transaction count per employee
    SELECT 
        "Emp_ID",
        "Name",
        "Region",
        COUNT(*) AS total_transactions,
        SUM("Revenue") AS total_revenue,
        ROUND(AVG("Revenue")::numeric, 2) AS avg_deal_size
    FROM sales_data
    GROUP BY "Emp_ID", "Name", "Region"
),
RankedEmployees AS (
    -- Step B: Apply Window Functions to rank reps within their region
    SELECT 
        "Emp_ID",
        "Name",
        "Region",
        total_transactions,
        total_revenue,
        avg_deal_size,
        -- Rank reps per region based on revenue
        DENSE_RANK() OVER (
            PARTITION BY "Region" 
            ORDER BY total_revenue DESC
        ) AS regional_rank,
        -- Calculate the regional total dynamically across all rows
        SUM(total_revenue) OVER (
            PARTITION BY "Region"
        ) AS total_regional_pool
    FROM EmployeeAggregates
)
-- Step C: Calculate individual contribution percentage to regional total
SELECT 
    "Region",
    regional_rank,
    "Emp_ID",
    "Name",
    total_transactions,
    total_revenue,
    avg_deal_size,
    ROUND(((total_revenue / total_regional_pool) * 100)::numeric, 2) AS pct_of_regional_revenue
FROM RankedEmployees
ORDER BY "Region", regional_rank ASC;

-- 2. View the resulting analytics table
SELECT * FROM regional_sales_performance;