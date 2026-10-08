# Energy Demand & Carbon Insights Dashboard

A portfolio project analysing UK electricity demand, carbon intensity and generation mix using Python, SQL and Power BI.

## Objective
Identify peak-demand periods, seasonal patterns, regional differences and opportunities for smarter energy management.

## Data source
- UK Carbon Intensity API: https://api.carbonintensity.org.uk/
- The project is designed to work with historical half-hourly/hourly electricity and carbon-intensity data. Raw third-party data is not committed to this repository.

## Workflow
API / CSV → Python cleaning → exploratory analysis → feature engineering → SQL analysis → Power BI dashboard

## Key KPIs
- Peak demand
- Average demand
- Minimum demand
- Average carbon intensity
- Renewable generation percentage
- Peak-demand hours
- Weekday vs weekend demand

## Dashboard design
1. **Executive Overview** – KPI cards, demand trend, generation mix and regional summary.
2. **Demand Analysis** – hourly, daily and seasonal demand patterns, peak-period analysis and weekday/weekend comparison.
3. **Carbon & Generation** – carbon-intensity trends, renewable vs fossil generation and low-carbon periods.

## Repository structure
```text
energy-demand-carbon-insights/
├── python/
│   ├── 01_data_ingestion_cleaning.py
│   └── 02_eda_analysis.py
├── sql/
│   └── analysis_queries.sql
├── powerbi/
│   └── dashboard_design.md
├── data/
│   └── README.md
├── requirements.txt
└── README.md
```

## Notes
This is a personal/academic portfolio project. Any analytical finding should be validated from the downloaded dataset rather than assumed in advance. The dashboard and code are intended to demonstrate data ingestion, analytics, visualisation and energy-sector problem solving.
