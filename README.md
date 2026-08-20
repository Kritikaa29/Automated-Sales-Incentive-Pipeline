# Automated Sales Analytics & Incentive Pipeline

## 📌 Project Overview
This project demonstrates an end-to-end data engineering and analytics workflow. It is designed to track regional sales performance, analyze large datasets, and automate employee ranking calculations for incentive compensation. The project is split into two phases: a business prototype and a scalable cloud ETL architecture.

## 🛠️ Tech Stack
* **Data Engineering:** Python, Pandas, SQLAlchemy
* **Cloud Database:** PostgreSQL (Supabase)
* **Data Visualization & Prototyping:** Microsoft Excel (Pivot Tables, Dynamic Dashboards)
* **Query Language:** Advanced SQL (CTEs, Window Functions)

## 🚀 Phase 1: Business Prototyping (Excel)
Before scaling to the cloud, the initial data model was built to understand business requirements:
* Processed raw sales data and structured it for analysis.
* Engineered a dynamic KPI dashboard using Pivot Tables and Slicers.
* Visualized total revenue, regional performance, and transaction volumes for quick business decision-making.

## ☁️ Phase 2: Scalable Cloud Architecture (Python & PostgreSQL)
To handle massive data loads and automate reporting, the pipeline was upgraded to a cloud environment:
* **ETL Pipeline:** Architected a Python script to generate, compress, and ingest 10,000+ transaction records directly into a live Supabase PostgreSQL database.
* **Advanced Analytics:** Wrote automated SQL views using Common Table Expressions (CTEs) and Window Functions (`DENSE_RANK`, `SUM() OVER`).
* **Incentive Calculation:** Dynamically ranked sales representatives based on revenue and calculated regional market share to automate commission data.

## 📂 Repository Files
* `data_generator.py` - The Python ETL script for generating and migrating data to the cloud.
* `advanced_analytics.sql` - The PostgreSQL script containing the CTEs and Window Functions.
* `sales_dashboard.xlsx` - The initial Phase 1 Excel dashboard prototype.
* *Note: Database connection strings have been secured and hidden for privacy.*
