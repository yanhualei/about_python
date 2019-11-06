数据库的操作
 	链接数据库
 	1.mysql -uroot -p;
 	2.mysql -uroot -proot;#(root是mysql的登录密码)
	
	3.show databases;查看所有的数据库

	3.show create database test01;查看数据库创建结构
	
	4.select database();查看当前使用的数据库
	
	5.exit/quit/Ctrl+d;退出数据库
	6.drop database test01;删除数据库

	创建数据库
	6.drop database if exists `python-02`;  # 注意："`"是Tab上面的符号，不是单引号，表示的是python-02是一个整体，不包含起来将会报错
	create database python-02;

	8.select version();显示数据库版本
	
	9.select now();显示当前时间
表的相关操作
	show tables; 查看当前数据库中的所有表格
	 --int unsigned: 非负整数
	 --auto_increment: 自增长
	 --primary key: 主键
	 创建表
	1.create table students(  
		id int unsigned not null auto_increment primary key ,
		name varchar(30),
		age tinyint unsigned default 0,
		high decimal(5,2),
		gender enum("男","女","中性","保密") default "保密",
		cls_id int unsigned
		);
	2.create table classes(
		id int unsigned not null auto_increment primary key,
		nema varchar(30) 
		);
	修改表
	修改数据操作
	1.alter table students add id_delete bit default 0;修改表-添加字段--二进制的0默认不显示 
	2.alter table students modify birthday date;修改表-修改字段的类型或约束
	3.alter table students change birthday birth date default "1992-10-22";修改表-修改表的列名、类型和约束

	删除表
	1.alter table students drop high;修改表-删除列
	2.drop table if exists xxxx;修改表-删除表
	
数据的相关操作

	增加数据操作
	1.全值插入：注意对号入座
	insert into students values(0,"老王",19,175.00,"男",001,"1997-02-14");
	  insert into students values(null,"老王",19,175.00,"男",001,"1997-02-14");
	  insert into students values(default,"老王",19,175.00,"男",001,"1997-02-14");
	  --表示的是让id主键自增长

	2.目标插入(其余默认)
	insert into students (name,gender) values ("小乔",2)
	insert into students values ("大乔",2)，("貂蝉",4)，("王昭君",2)
	  	--表示插入数据时可插入自己想要的数据，其他自动填null或者default

	

	更新数据操作
	update students set gender = 3 where name = "貂蝉";
	+----+-----------+------+--------+--------+--------+------------+
	| id | name      | age  | high   | gender | cls_id | birth      |
	+----+-----------+------+--------+--------+--------+------------+
	|  1 | 老王      |   19 | 175.00 | 男     |      1 | NULL       |
	|  2 | 老李      |   22 | 165.00 | 女     |      2 | 1995-10-22 |
	|  3 | 小张      |   19 | 175.00 | 男     |      1 | 1997-02-14 |
	|  4 | 小乔      |    0 |   NULL | 女     |   NULL | 1992-10-22 |
	|  5 | 大乔      |    0 |   NULL | 保密   |   NULL | 1992-10-22 |
	|  6 | 貂蝉      |    0 |   NULL | 中性   |   NULL | 1992-10-22 |
	|  7 | 王昭君    |    0 |   NULL | 女     |   NULL | 1992-10-22 |
	+----+-----------+------+--------+--------+--------+------------+

	删除数据操作
	--物理删除(一般情况下轻易不要使用delete)
	1.delete from students;尽量少使用，公司数据一般都是来之不易，谨慎使用 --清空表格
	2.delete from students where id =3; --删除id=3的这一条数据
    --逻辑删除
    -- 设置一个删除字段id_delete,id_delete=0表示本条数据的逻辑删除
    


	查询数据操作
	1.select * from students; -- *查询
	2.select id,name,gender,age from students --查询目标列
	3.select name as 姓名,gender as 性别 from students where id>2 and id<5;--条件查询和as增加查询结果的可读性
	分页查询limit:对于大量数据来说，避免了全表扫描，从而提高了查询效率
	1.select * from students limit 5,10;查询6-15行数据
	2.select * from students limit 5,-1;查询6-last
	3.select * from students limit 5;查询前五行数据






	





