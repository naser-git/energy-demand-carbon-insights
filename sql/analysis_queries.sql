-- Expected table: energy_demand
-- timestamp, region, demand_mw, carbon_intensity,
-- renewable_generation_mw, fossil_generation_mw

-- Average demand by hour
SELECT EXTRACT(HOUR FROM timestamp) AS hour,
       AVG(demand_mw) AS avg_demand_mw
FROM energy_demand
GROUP BY EXTRACT(HOUR FROM timestamp)
ORDER BY hour;

-- Peak-demand observations above 120% of overall average
SELECT timestamp, region, demand_mw
FROM energy_demand
WHERE demand_mw > (SELECT AVG(demand_mw) * 1.20 FROM energy_demand)
ORDER BY demand_mw DESC;

-- Regional comparison
SELECT region,
       AVG(demand_mw) AS avg_demand_mw,
       AVG(carbon_intensity) AS avg_carbon_intensity
FROM energy_demand
GROUP BY region
ORDER BY avg_demand_mw DESC;

-- Renewable generation share
SELECT region,
       100.0 * SUM(renewable_generation_mw)
       / NULLIF(SUM(renewable_generation_mw + fossil_generation_mw), 0)
       AS renewable_share_pct
FROM energy_demand
GROUP BY region;
