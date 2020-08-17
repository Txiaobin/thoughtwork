# 1.查询同时存在1课程和2课程的情况
select t1.id, t1.name, t1.age, t1.sex
from(
select stu.id, stu.name, stu.age, stu.sex
from student as stu
left join student_course as cou
on stu.id = cou.studentId
where cou.courseId = '1') t1
inner join(
select stu.id, stu.name, stu.age, stu.sex
from student as stu
left join student_course as cou
on stu.id = cou.studentId
where cou.courseId = '2') t2
on t1.id = t2.id

# 2.查询同时存在1课程和2课程的情况
select t1.id, t1.name, t1.age, t1.sex
from(
select stu.id, stu.name, stu.age, stu.sex
from student as stu
left join student_course as cou
on stu.id = cou.studentId
where cou.courseId = '1') t1
inner join(
select stu.id, stu.name, stu.age, stu.sex
from student as stu
left join student_course as cou
on stu.id = cou.studentId
where cou.courseId = '2') t2
on t1.id = t2.id

# 3.查询平均成绩大于等于60分的同学的学生编号和学生姓名和平均成绩
select stu.id, stu.name, avg(co.score) avg_score
from student as stu
left join student_course as co
on stu.id = co.studentId
group by 1,2
having avg(co.score) >= 60

# 4.查询在student_course表中不存在成绩的学生信息的SQL语句
select stu.id, stu.name, stu.age, stu.sex
from student as stu
left join student_course as co
on stu.id = co.studentId
group by 1,2,3,4
having avg(co.score) is null

# 5.查询所有有成绩的SQL
select cou.studentId, cou.courseId, cou.score
from student_course as cou
where cou.score is not null

# 6.查询学过编号为1并且也学过编号为2的课程的同学的信息
select t1.id, t1.name, t1.age, t1.sex
from(
select stu.id, stu.name, stu.age, stu.sex
from student as stu
left join student_course as cou
on stu.id = cou.studentId
where cou.courseId = '1') t1
inner join(
select stu.id, stu.name, stu.age, stu.sex
from student as stu
left join student_course as cou
on stu.id = cou.studentId
where cou.courseId = '2') t2
on t1.id = t2.id

# 7.检索1课程分数小于60，按分数降序排列的学生信息
select stu.id, stu.name, stu.age, stu.sex
from student as stu
left join student_course as cou
on stu.id = cou.studentId
where cou.courseId = '1'
and cou.score < 60
order by cou.score desc

# 8.查询每门课程的平均成绩，结果按平均成绩降序排列，平均成绩相同时，按课程编号升序排列
select courseId, avg(score)
from student_course
group by 1
order by 2 desc, 1

# 9.查询课程名称为"数学"，且分数低于60的学生姓名和分数
select stu.name, cou.score
from student_course as cou
inner join course as t
on t.id = convert(cou.courseId, signed)
and t.name = '数学'
inner join student as stu
on cou.studentId = stu.id
where cou.score < 60

