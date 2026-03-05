-- Write a script that lists all cities contained in the database hbtn_0d_usa.
SELECT cities.id, cities.name, states.name FROM cities
JOIN states ON cities.state_id = states.id
WHERE states.name = 'California'
ORDER BY id ASC;