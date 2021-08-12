import pymysql
# 获取数据库连接对象
connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='123456', db='test', charset='utf8')
# 获取一个游标
driver = connection.cursor()
# #判断这张表是否存在，若存在，则跳过创建表操作,不存在则建立下表
driver.execute("CREATE TABLE IF NOT EXISTS `t_emp`(`id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键',`name` varchar(20) DEFAULT NULL COMMENT '姓名',`department` varchar(20) DEFAULT NULL COMMENT '部门',`salary` decimal(10,2) DEFAULT NULL COMMENT '工资',`age` int(11) DEFAULT NULL COMMENT '年龄',`sex` varchar(4) DEFAULT NULL COMMENT '性别',PRIMARY KEY (`id`))ENGINE=InnoDB DEFAULT CHARSET=utf8; ")

# 如果该数据库存在就删除
# driver.execute("drop table if exists t_emp ")
# 定义sql语句  建立表
# sql = """ CREATE TABLE `t_emp` (
#   `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键',
#   `name` varchar(20) DEFAULT NULL COMMENT '姓名',
#   `department` varchar(20) DEFAULT NULL COMMENT '部门',
#   `salary` decimal(10,2) DEFAULT NULL COMMENT '工资',
#   `age` int(11) DEFAULT NULL COMMENT '年龄',
#   `sex` varchar(4) DEFAULT NULL COMMENT '性别',
#   PRIMARY KEY (`id`)
# )ENGINE=InnoDB DEFAULT CHARSET=utf8;
# """
# 执行sql
# driver.execute(sql)

# 定义sql语句
sql = """ insert into t_emp(name,department,salary,age,sex)
        values("to222m","开发部",8000,25,"男"), ("tom112","测试",800,2,"男")

 """
# 执行sql
driver.execute(sql)
# 提交到数据库执行
connection.commit()
# 关闭数据连接
connection.close()

