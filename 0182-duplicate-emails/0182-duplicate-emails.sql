# Write your MySQL query statement below
select email as Email from Person as p group by p.email having count(email)>1;