-- Ranks country origins of bands
-- column names must be origin nb_fans
SELECT origin, SUM(nb_fans) AS nb_fans FROM metal_bands GROUP BY origin ORDER BY nb_fans DESC;
