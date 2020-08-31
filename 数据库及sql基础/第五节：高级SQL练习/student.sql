/*
请编写一个MySQL存储过程calc_student_stat计算统计数据并输出到一个新表student_stat中。其中需要统计的数据有：
avg_score: 该科目平均分
score: 学生在该科目下的得分
total_score: 学生总分
score_rate: 该科目得分占总分的比例
除了上述统计字段，student_stat表还包含字段：name teacher subject.
*/

delimiter $$
CREATE PROCEDURE calc_student_stat()
BEGIN
 　 CREATE TABLE IF NOT EXISTS `student_score` as
    SELECT stu.name,
           sum(score) score,
           score / sum(score) score_rate
    from student stu
    inner join score sco
    on stu.id = sco.student_id
    group by 1

    CREATE TABLE IF NOT EXISTS `subject_score` as
    SELECT sub.subject,
           avg(acore) avg_score,
    from subject sub
    inner join score sco
    on sub.id = sco.subject_id
    group by 1

    CREATE TABLE IF NOT EXISTS `student_stat` as
    select stu.name,
           sub.teacher,
           sub.subject,
           stu.score,
           stu.score_rate,
           sub.avg_score
    from score sco
    inner join (
        select stu.name,
               sts.score,
               sts.score_rate
        from student t
        inner join student_score sts
        on stu.name = sts.name) stu
    on stu.id = sco.student_id
    inner join(
        select t.id
               t.subject,
               t.teacher,
               sts.avg_score
        from subject t
        inner join subject_score sts
        on t.subject = sts.subject
    ) sub
    on sub.id = sco.subject_id
END$$
delimiter;