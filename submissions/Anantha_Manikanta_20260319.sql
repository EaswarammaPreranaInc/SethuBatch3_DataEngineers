# 1. Write a Query to display employees information whose name contains only 5 characters

		select *
        from emp
        where ename like '_____';

# 2. Write a query to display employees information whose names does not contains A.

		select *
		from emp
		where ename not like '%A%';
			

# 3. Write a query to display employees information who are all working as CLERK and their salary in range from 1000 to 2000.
		select *
		from emp
		where job='CLERK'
        AND (sal>=1000 AND sal<=2000);
		
  
# 4. Write a query to display employees information who is not getting comm.

		select *
		from emp
		where comm = 0;

# 5. Write a query to display employees information whose annual salary is greater than 30000.
   
		select *
		from emp
		where sal*12 > 30000;
      
# 6. Create College Details as a parent table with the following details College Code, College Name, Principal Name, College_Address
    
			create table college_details ( College_Code number constraint College_Code_PK primary key, 
			  College_Name VARCHAR2(50), 
              Principal_Name VARCHAR2(50),
              College_Address VARCHAR2(50)             
            );
	
# 7. Create STUDENT details as a child table and link with Parent table college with the following columns.
   
#	SLNO NUMBER    --- Should have Primary Key 
#	SNAME VARCHAR2(30),
#	DOB DATE,		-- Should have NOT NULL Constraint 
#	Fname VARCHAR2(30)
#	College_Code VARCHAR2(30),
#	FEES NUMBER   -- Should have CHECK Constraint 
    
		create table student_details
        ( SLNO NUMBER constraint SLNO_PK primary key,
          SNAME VARCHAR2(30),
          DOB DATE constraint DOB_NN not null,
          Fname VARCHAR2(30),
          College_Code number constraint College_Code_FK references college_details (College_Code),
          FEES NUMBER constraint FEES_chk check (FEES >=54321)
        );
   
   
# 8. query to get constraint details which are having in the table STUDENT. 

		select * from user_constraints where table = upper('student');

# 9. Modify the data in the student table from NULL values to 100 in the SLNO column.

		update student
        set SLNO = 100
        where SLNO is NULL;



# 10. Difference between TRUNCATE, DELETE, DROP.   

	#- To clear data and keep the structure of the table, use TRUNCATE.
    # To delete specific row of the table, use DELETE.
	#- To erase the entire table (data and structure) from db, use drop.
    