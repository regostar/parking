Please view  SQUADSTACK.docx  for analysis and detailed explanation
 
# STEPS TO RUN 

## 1.	Install Postgresql server and create database of name - parking. (can have your custom name)

Download it from https://www.postgresql.org/download/
To install on Mac, 
https://www.enterprisedb.com/postgresql-tutorial-resources-training?cid=438

sudo -u postgres psql

### Create database
create database parking;
### Create database user
create user myuser with encrypted password 'supersecurepassword123#';
### set permissions
grant all privileges on database parking to myuser;

Note:- it is your choice on where to install postgres, can install on docker too, if postgres is already installed then please just create a new database and user.

## 2.	Install Pgadmin4
This is a database visualization tool, where we can also execute queries.
https://www.pgadmin.org/download/
Must be straightforward installation

## 3.	Unzip the project or download from github and clone to master branch
 

## 4.	Install virtual environment

>> python3 -m venv venv
>> source venv/bin/activate
>> pip install –upgrade pip
>> pip install -r requirements.txt


## 5.	Set settings for database in base.py
Create a .env file for storing database secrets :- 
>> nano .env
And enter :- 
DATABASE=postgresql://username:password@localhost:5432/database_name
Please change the port or host if you are using a different one.

## 6.	Simply run :- 
>> python parking.py
>> 

## 7. To test run :- 
>> pytest
