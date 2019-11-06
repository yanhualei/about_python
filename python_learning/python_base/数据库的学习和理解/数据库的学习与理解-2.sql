drop database if exists jing_dong;--京东如果存在先删除
create database jing_dong charset=utf8; --创建京东数据库
use jing_dong;-- 切换到京东数据库

create table good(
	/*-- id ；
	-- name:产品描述：2018最畅销的.......；
	-- cate_name:类别名字：手表，平板电脑等；
	-- brand_name:品牌：华为，苹果等；
	-- price:价格；
	-- is_show:是否显示；
	-- is_saleoff:显示，但是显示卖完；*/
	id int unsigned not null primary key auto_increment,
	name varchar(200) not null ,
	cate_name varchar(50) not null,
	brand_name varchar(50) not null,
	price decimal(10,3) not null default 0,
	is_show bit not null default 1,
	id_saleoff bit not null default 0
);

--查询超级本的名字和价格
1.select name as 产品描述,price as 价格 from goods where cate_name = "超级本";

--查询产品表中所有的种类，即列出所有产品种类
2.select distinct cate_name from goods;--distinct 去除查询结果中重复的部分
3.select cate_name from goods group by cate_name; --group by 将查询的结果进行分组

--求所有电脑产品的平均价格,并且保留两位小数
4.select round(avg(price),2) as 平均价格 from goods;--round(avg(price),2)平均价格保留两位小数

--显示每种商品的平均价格
5.select cate_name as 商品种类, avg(price) as 平均价格 from goods group by cate_name;

--查询每种类型的商品中 最贵、最便宜、平均价、数量
6.select cate_name，max(price), min(price),avg(price),count(*) from goods group by cate_name;--count(*)统计行数

--查询所有价格大于平均价格的商品，并且按价格降序排序
7.select name,price from goods where 
	price >(select avg(price) from goods)
	order by price desc; -- order by 排序操作

--查询每种类型中最贵的电脑信息
8.select id,name,cate_name,brand_name,price,is_show,id_saleoff from
	(select cate_name,max(price) as price from goods group by cate_name) as new_goods
	left join goods as g  -- 以左边的表格为模板
	on g.cate_name = new_goods.cate_name and g.price = new_goods.price;










