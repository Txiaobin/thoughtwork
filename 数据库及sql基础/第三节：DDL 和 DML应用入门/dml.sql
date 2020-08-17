-- 插入记录  
insert into student values( "001", "张三", 18, "男" );
-- 修改记录  
update student set sex='女' where sex='男';
--  删除记录  
delete from student where sex='男';
-- 查询记录  
select * id from student