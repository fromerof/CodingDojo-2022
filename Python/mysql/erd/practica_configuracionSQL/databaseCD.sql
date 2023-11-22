show databases;
create DATABASE databaseCD;
show databases;
use databaseCD;
create table clients(id int not null auto_increment,
first_name varchar(255) not null,
last_name varchar(255) not null,
created_at datetime,
updated_at datetime,
primary key (id));

SELECT * FROM clients;
INSERT INTO clients(first_name,last_name)
VALUES('Felipe',"Romero"),('Jack',"Son");

