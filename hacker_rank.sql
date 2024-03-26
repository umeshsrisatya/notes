/*
Query the two cities in STATION with the shortest and longest CITY names, as well as their respective lengths (i.e.: number of characters in the name).
If there is more than one smallest or largest city, choose the one that comes first when ordered alphabetically.The STATION table is described as follows:
*/
SELECT CITY, LENGTH(CITY) AS LENGTH
FROM STATION
ORDER BY LENGTH ASC, CITY
LIMIT 1;
SELECT CITY, LENGTH(CITY) AS LENGTH
FROM STATION
ORDER BY LENGTH DESC, CITY
LIMIT 1;
