# Write your MySQL query statement below


SELECT A.firstName, A.lastName, S.city, S.state FROM PERSON A
LEFT JOIN ADDRESS S ON 
A.personId = S.personId