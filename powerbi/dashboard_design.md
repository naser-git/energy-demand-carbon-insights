# Power BI Dashboard Specification

## Page 1 — Executive Overview
- KPI cards: Peak Demand, Average Demand, Average Carbon Intensity, Renewable Share
- Demand trend over time
- Generation mix
- Region slicer

## Page 2 — Demand Analysis
- Average demand by hour
- Weekday vs weekend demand
- Monthly/seasonal trend
- Peak-demand heatmap
- Regional comparison

## Page 3 — Carbon & Generation
- Carbon-intensity trend
- Renewable vs fossil generation
- Low-carbon periods
- Regional carbon-intensity comparison

## Suggested measures

```DAX
Average Demand = AVERAGE(energy_demand[demand_mw])

Peak Demand = MAX(energy_demand[demand_mw])

Average Carbon Intensity = AVERAGE(energy_demand[carbon_intensity])

Renewable Share % =
DIVIDE(
    SUM(energy_demand[renewable_generation_mw]),
    SUM(energy_demand[renewable_generation_mw]) +
    SUM(energy_demand[fossil_generation_mw])
)
```

The measures should be adapted to the final dataset schema used in Power BI.
