# Write your MySQL query statement below
select p.firstName , p.lastName, a.city, a.state from address as a right join person as p on p.personId=a.personId ;
