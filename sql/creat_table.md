# 创建表

``` sql
CREATE TABLE `student` (
	`id` VARCHAR ( 20 ) NOT NULL PRIMARY KEY,
	`name` VARCHAR ( 30 ) NOT NULL,
	`age` INT ( 10 ) NOT NULL,
	`sex` VARCHAR ( 10 ) NOT NULL 
) ENGINE = INNODB DEFAULT charset = utf8;
CREATE TABLE `subject` (
	`id` VARCHAR ( 20 ) NOT NULL PRIMARY KEY,
	`subject` VARCHAR ( 30 ) NOT NULL,
	`teacher` VARCHAR ( 30 ) NOT NULL,
	`description` VARCHAR ( 100 ) NOT NULL 
) ENGINE = INNODB DEFAULT charset = utf8;
CREATE TABLE `score` ( 
	`id` INT ( 10 ) NOT NULL PRIMARY KEY,
	`student_id` VARCHAR ( 20 ),
	`subject_id` VARCHAR ( 20 ),
	`score` VARCHAR ( 20 ),
	FOREIGN KEY(student_id) REFERENCES student(id),
	FOREIGN KEY(subject_id) REFERENCES subject(id)
	) ENGINE = INNODB DEFAULT charset = utf8;
```

# 插入数据

``` sql
INSERT INTO `student` ( id, NAME, age, sex )
VALUES
	( "001", "张三", 18, "男" ),
	( "002", "李四", 20, "女" );
	
INSERT INTO `subject` ( id, SUBJECT, teacher, description )
VALUES
	( "1001", "语文", "王老师", "本次考试比较简单" ),
	( "1002", "数学", "刘老师", "本次考试比较难" );
	
INSERT INTO `score` ( id, student_id, subject_id, score )
VALUES
	( 1, "001", "1001", "80" ),
	( 2, "002", "1002", "60" ),
	( 3, "001", "1001", "70" ),
	( 4, "002", "1002", "60.5" );
```

