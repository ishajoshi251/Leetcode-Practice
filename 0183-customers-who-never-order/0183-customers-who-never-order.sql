# Write your MySQL query statement below
select c.name as customers from customers c left join orders o on c.id = o.customerid where o.customerid is Null