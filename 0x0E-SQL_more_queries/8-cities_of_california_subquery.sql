-- Lists all the cities with value "California" in the database "hbtn_0d_usa"
SELECT cities.id, name
FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY cities.id ASC;
