use joinsdb;
select upper(emp_name) from employees_demo;
select lower(emp_name) from employees_demo;
select length(emp_name) from employees_demo;
select substring(emp_name,1,3) from employees_demo;
select substring(emp_name,length(emp_name)-1,length(emp_name)) from employees_demo;
select replace(emp_name,'o','0') from employees_demo;
select trim(emp_name) from employees_demo;
select concat(emp_name,emp_id) from employees_demo;
select reverse(emp_name) from employees_demo;
select concat(upper(substring(emp_name,0,1)),(substring(emp_name,1))) from employees_demo;
select dept_id * 10 from employees_demo;
select round(dept_id) from employees_demo;
select abs(dept_id) from employees_demo where dept_id=105;
select power(dept_id,2) from employees_demo;
select sqrt(dept_id) from employees_demo;
select emp_name from employees_demo where dept_id =102;
select emp_name from employees_demo where dept_id >104;
select emp_name from employees_demo where dept_id between 101 and 104;
select emp_name from employees_demo where emp_name like 'J%';
select emp_name from employees_demo where emp_name like '%a';
select emp_name from employees_demo where emp_name like '%vi%';
select emp_name from employees_demo where dept_id in (101,102,103);
select emp_name from employees_demo where dept_id not in (101,102);
select emp_name from employees_demo where dept_id is null;
select emp_name from employees_demo where length(emp_name) > 5;
select emp_name from employees_demo order by emp_name;
select emp_name from employees_demo order by emp_name desc;
select emp_name from employees_demo order by dept_id,emp_name;
select emp_name from employees_demo order by dept_id desc;
select emp_name from employees_demo order by emp_name limit 5;
select count(*) from employees_demo;
select dept_id,count(*) from employees_demo group by dept_id;
select max(dept_id) from employees_demo;
select min(dept_id) from employees_demo;
select avg(dept_id) from employees_demo;
select dept_id,count(*) from employees_demo group by dept_id having count(*) > 2;
select dept_id,count(*) from employees_demo group by dept_id having count(*) = 1;
select e.emp_name, d.dept_name from employees_demo e join departments_demo d 
on e.dept_id = d.dept_id ;
select * from employees_demo e right join departments_demo d 
on e.dept_id = d.dept_id ;
select e.emp_name from employees_demo e left join departments_demo d 
on e.dept_id = d.dept_id where d.dept_id is null;
select * from projects_demo;
select d.dept_name from departments_demo d left join projects_demo p 
on p.dept_id = d.dept_id where project_name is null; 
select p.project_name,d.dept_name from departments_demo d join projects_demo p 
on p.dept_id = d.dept_id ;
select e.emp_name,p.project_name from projects_demo p 
join employees_demo e on p.dept_id=e.dept_id;
select distinct d.dept_name from projects_demo p 
join employees_demo e on p.dept_id=e.dept_id join departments_demo d on d.dept_id = p.dept_id;
select * from employees_selfjoin;
select e.emp_name, m.emp_name as manager from employees_selfjoin e join employees_selfjoin m 
on e.manager_id=m.emp_id;
select e.emp_name from employees_selfjoin e join employees_selfjoin m 
on e.manager_id=m.emp_id where m.manager_id is null;
select m.emp_name as manager , e.emp_name as team_members from employees_selfjoin e join employees_selfjoin m 
on e.manager_id=m.emp_id;
select e.emp_name from employees_selfjoin e join employees_selfjoin m 
on e.manager_id=m.emp_id where m.emp_name = 'Mary';
select * from employees_demo where emp_name !='John' and 
dept_id = ( select dept_id from employees_demo where emp_name='John');
select dept_name from departments_demo where
dept_id in ( select dept_id from employees_demo );
select emp_name from employees_demo where dept_id in (
select dept_id from projects_demo group by dept_id having count(*) >=1);
select emp_name from employees_demo where dept_id not in (
select dept_id from projects_demo );
select * from projects_demo;
select project_name from projects_demo where dept_id in(
select dept_id from employees_demo );
select dept_name from departments_demo where  dept_id = (
select dept_id from employees_demo group by dept_id order by count(*) desc limit 1);
select emp_name from employees_demo where dept_id in (
select dept_id from projects_demo group by dept_id having count(*) > 1);
