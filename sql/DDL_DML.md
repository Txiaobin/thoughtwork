show databases;
create databse tempsql;
create database tempsql1 character set utf8;
show create database tempsql1;
alter database tempsql1 character set gb2312;
drop database tempsql1;
use tempsql

CREATE TABLE `student` (
	`id` VARCHAR ( 20 ) NOT NULL PRIMARY KEY,
	`name` VARCHAR ( 30 ) NOT NULL,
	`age` INT ( 10 ) NOT NULL,
	`sex` VARCHAR ( 10 ) NOT NULL 
) ENGINE = INNODB DEFAULT charset = utf8;

rename table student to new_student;
alter table new_student modify name varchar(50);
alter table new_student change name new_name;
alter table new_student add class int; 
alter table new_student drop class;
alter table new_student engine=MyISAM;
alter table new_student drop foreign key fk_name;
drop table new_student; 

CREATE TABLE `student` (
	`id` VARCHAR ( 20 ) NOT NULL PRIMARY KEY,
	`name` VARCHAR ( 30 ) NOT NULL,
	`age` INT ( 10 ) NOT NULL,
	`sex` VARCHAR ( 10 ) NOT NULL 
) ENGINE = INNODB DEFAULT charset = utf8;

insert into student values( "001", "张三", 18, "男" );
update student set sex='女' where sex='男';
delete from student where sex='男';
select * id from student