-- Displays the average temprature by city in a descending order
SELECT city, AVG(value) AS avg_temprature
FROM temperatures
GROUP BY city
ORDER BY avg_temperature DESC;
