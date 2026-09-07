# 📊 Vendor Performance Analysis

> **An end-to-end data analytics project to evaluate vendor performance, profitability, inventory efficiency, pricing strategy, and sales contribution using Python, SQL, and Power BI.**

---

## 📌 Project Overview

Vendor and inventory management play a critical role in maintaining profitability and operational efficiency in the retail and wholesale industry.

This project analyzes vendor-level sales, purchasing, pricing, inventory, and profitability data to identify:

- High- and low-performing vendors
- Brands requiring pricing or promotional adjustments
- Vendor concentration and supply-chain dependency
- Impact of bulk purchasing on unit costs
- Slow-moving inventory and capital tied up in stock
- Differences in profitability between high- and low-performing vendors

The analysis combines **Python-based data processing and exploratory analysis** with an interactive **Power BI dashboard** to transform raw transactional data into actionable business insights.

---
### 📊 Dashboard Preview

<p align="center">
  <img src="Power%20BI/vendor_performance_dashboard.png" alt="Vendor Performance Dashboard" width="100%">
</p>

## 🎯 Business Objectives

The primary objectives of this project are:

1. Identify underperforming brands that may require promotional or pricing adjustments.
2. Determine the top vendors contributing to sales and gross profit.
3. Analyze the relationship between bulk purchasing and unit purchase costs.
4. Identify vendors with low inventory turnover and high unsold inventory.
5. Compare profitability between high-performing and low-performing vendors.
6. Statistically validate whether the difference in vendor profitability is significant.
7. Develop actionable recommendations to improve profitability and inventory efficiency.

---

## 🛠️ Tools & Technologies

| Technology | Purpose |
|---|---|
| 🐍 **Python** | Data processing and analysis |
| 🐼 **Pandas** | Data cleaning, transformation & analysis |
| 🔢 **NumPy** | Numerical computation |
| 📊 **Matplotlib** | Data visualization |
| 🎨 **Seaborn** | Statistical visualization |
| 🗄️ **SQL** | Data querying and aggregation |
| 📓 **Jupyter Notebook** | Exploratory analysis & documentation |
| 📈 **Power BI** | Interactive dashboard & business reporting |
| 🔧 **Git & GitHub** | Version control and project sharing |

---

# 🔄 Project Workflow

```text
                    ┌─────────────────────┐
                    │    Raw Datasets     │
                    │ Sales / Purchases   │
                    │ Inventory / Pricing │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Data Validation &    │
                    │ Cleaning             │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Data Ingestion &     │
                    │ Transformation       │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Exploratory Data     │
                    │ Analysis (EDA)       │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Vendor Performance   │
                    │ Analysis             │
                    └──────────┬──────────┘
                               │
                 ┌─────────────┴─────────────┐
                 ▼                           ▼
        ┌─────────────────┐        ┌─────────────────┐
        │ Processed Data  │        │ Business        │
        │ & Summary CSV   │        │ Insights        │
        └────────┬────────┘        └────────┬────────┘
                 │                           │
                 ▼                           ▼
        ┌─────────────────┐        ┌─────────────────┐
        │    Power BI     │        │ Final Business  │
        │    Dashboard    │        │     Report      │
        └─────────────────┘        └─────────────────┘
