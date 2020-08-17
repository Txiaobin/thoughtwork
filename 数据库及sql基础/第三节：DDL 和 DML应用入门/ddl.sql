-- **数据库级别：**  
--  显示所有数据库  
show databases;
--  进入某个数据库  
use tempsql
--  创建一个数据库  
create databse tempsql;
--  创建指定字符集的数据库  
create database tempsql1 character set utf8;
--  显示数据库的创建信息   
show create database tempsql1;
--  修改数据库的编码  
alter database tempsql1 character set gb2312;
--  删除一个数据库   
drop database tempsql1;
-- **表级别**
--  修改表名
rename table student to new_student;
--  修改字段的数据类型
alter table new_student modify name varchar(50);
--  修改字段名
alter table new_student change name new_name;
--  添加字段
alter table new_student add class int; 
--  删除字段
alter table new_student drop class;
--  修改表的存储引擎
alter table new_student engine=MyISAM;
--  删除表的外键约束
alter table new_student drop foreign key fk_name;
--  删除一张表
drop table new_student; 