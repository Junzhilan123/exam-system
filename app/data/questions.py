single_choice_questions = [
    {
        "id": 1,
        "question": "（A）是对数据库中全部数据的逻辑结构和特征的描述。",
        "options": ["A.模式", "B.外模式", "C.内模式", "D.视图"],
        "answer": "A"
    },
    {
        "id": 2,
        "question": "（B）是对数据库用户能够看见和使用的局部数据的逻辑结构和特征的描述",
        "options": ["A.模式", "B.外模式", "C.内模式", "D.概念模式"],
        "answer": "B"
    },
    {
        "id": 3,
        "question": "数据库中的记录是按照B+树存储还是按hash方法存储，这一特征在数据库的（）中定义。",
        "options": ["A.模式", "B.外模式", "C.内模式", "D.子模式"],
        "answer": "C"
    },
    {
        "id": 4,
        "question": "概念模型的表示方法有很多种，其中最著名的是（）。",
        "options": ["A.关系模型", "B.E-R模型", "C.层次模型", "D.网状模型"],
        "answer": "B"
    },
    {
        "id": 5,
        "question": "数据库的概念模型（）",
        "options": ["A.独立于计算机硬件，依赖于DBMS", "B.依赖于计算机硬件，独立于DBMS", "C.依赖于计算机硬件和DBMS", "D.独立于计算机硬件和DBMS"],
        "answer": "D"
    },
    {
        "id": 6,
        "question": "下列关系代数操作中复杂度最高的是（）。",
        "options": ["A.投影", "B.连接", "C.选择", "D.交"],
        "answer": "C"
    },
    {
        "id": 7,
        "question": "若关系R和S的元组个数分别为m和n，则R∪S的元组个数为（）。",
        "options": ["A.m+n", "B.小于或等于m+n", "C.大于m", "D.大于n"],
        "answer": "B"
    },
    {
        "id": 8,
        "question": "已知关系R1和R2进行关系运算后得到S，则S是（）",
        "options": ["A.一行记录", "B.一个关系", "C.一个确定值", "D.一个数组"],
        "answer": "B"
    },
    {
        "id": 9,
        "question": "若关系R和S的元组个数分别为m和n，则R-S的元组个数是（）。",
        "options": ["A.m-n", "B.小于m", "C.小于n", "D.小于等于m"],
        "answer": "D"
    },
    {
        "id": 10,
        "question": "下列关系代数操作中最费时的是（）。",
        "options": ["A.投影", "B.笛卡尔积", "C.选择", "D.交"],
        "answer": "B"
    },
    {
        "id": 11,
        "question": "在信息系统的设计中，普遍采用的是基于（）的系统设计方法。",
        "options": ["A.BCNF", "B.3NF", "C.2NF", "D.4NF"],
        "answer": "B"
    },
    {
        "id": 12,
        "question": "在函数依赖范畴内，（）是关系模式能够达到的最高规范化程度。",
        "options": ["A.3NF", "B.4NF", "C.BCNF", "D.5NF"],
        "answer": "C"
    },
    {
        "id": 13,
        "question": "下列说法中错误的是（）",
        "options": ["A.模式分解是关系规范化的基本方法", "B.实际应用中，数据库设计一般应达到3NF", "C.若一个关系模式符合2NF，则它必然也符合3NF", "D.实际应用中常常为了提高查询效率而允许数据库中存在一定的数据冗余"],
        "answer": "C"
    },
    {
        "id": 14,
        "question": "关系数据库中由数据冗余导致的异常不包括（）。",
        "options": ["A.插入异常", "B.删除异常", "C.修改异常", "D.查询异常"],
        "answer": "D"
    },
    {
        "id": 15,
        "question": "设关系模式R(XYZ)，已知存在函数依赖X->Y和Y->Z，则可作为R的候选键的是（）。",
        "options": ["A.X", "B.Y", "C.Z", "D.已知条件无法判断候选键"],
        "answer": "A"
    },
    {
        "id": 16,
        "question": "（）是数据库系统的核心，是位于用户和操作系统之间的一层数据管理软件。",
        "options": ["A.DBMS", "B.DBS", "C.DBA", "D.DDL"],
        "answer": "A"
    },
    {
        "id": 17,
        "question": "数据库管理系统的英文缩写是（）。",
        "options": ["A.DBMS", "B.DBA", "C.DBS", "D.MIS"],
        "answer": "A"
    },
    {
        "id": 18,
        "question": "下列不是关系数据库产品的是（）。",
        "options": ["A.SQL Server", "B.Oracle", "C.MySQL", "D.IMS"],
        "answer": "D"
    },
    {
        "id": 19,
        "question": "DBS指的是（）。",
        "options": ["A.数据库", "B.数据库系统", "C.数据库管理员", "D.数据库管理系统"],
        "answer": "B"
    },
    {
        "id": 20,
        "question": "DBA指的是（）。",
        "options": ["A.数据库", "B.数据库系统", "C.数据库管理员", "D.数据库用户"],
        "answer": "C"
    },
    {
        "id": 21,
        "question": "下列（）是MySQL数据库中的超级管理员用户。",
        "options": ["A.admin", "B.sa", "C.root", "D.administrator"],
        "answer": "C"
    },
    {
        "id": 22,
        "question": "MySQL服务的默认端口号是（）。",
        "options": ["A.3306", "B.1433", "C.8080", "D.1521"],
        "answer": "A"
    },
    {
        "id": 23,
        "question": "关于索引，下列说法错误的是（）。",
        "options": ["A.索引可以加快数据的检索速度", "B.建立索引会牺牲一定的系统性能", "C.在一张表上可以建立多个聚集索引", "D.在一张表上可以建立多个非聚集索引"],
        "answer": "C"
    },
    {
        "id": 24,
        "question": "关于视图，下列说法错误的是（）。",
        "options": ["A.视图是虚拟表", "B.数据可以存放在视图中", "C.在视图上做查询与在基本表上做查询方法是相同的", "D.视图可以建立在多个基本表的基础之上"],
        "answer": "B"
    },
    {
        "id": 25,
        "question": "下面哪种情况下适合建立索引（）。",
        "options": ["A.经常进行插入操作的表", "B.行数较小的表", "C.更新少而数据量大的表", "D.表中存在大量重复值的列"],
        "answer": "C"
    },
    {
        "id": 26,
        "question": "关于存储过程与触发器，下列说法正确的是（）。",
        "options": ["A.存储过程是存储在客户端的SQL程序", "B.触发器是一种特殊的存储过程", "C.触发器可通过其名字被用户直接调用", "D.存储过程是一种特殊的触发器"],
        "answer": "B"
    },
    {
        "id": 27,
        "question": "关于视图，下列说法正确的是（）",
        "options": ["A.建立视图语句的关键部分是查询语句", "B.若导出某视图的数据库表被删除了，该视图不受任何影响", "C.视图一旦建立，就不能被删除", "D.当某一视图被删除后，导出该视图的数据库表将会受到影响"],
        "answer": "A"
    },
    {
        "id": 28,
        "question": "数据库应用程序开发中，需求分析阶段的主要目的是（）。",
        "options": ["A.回答'做什么'的问题", "B.回答'怎么做'的问题", "C.建立逻辑数据模型", "D.建立最佳物理存储结构"],
        "answer": "A"
    },
    {
        "id": 29,
        "question": "在结构化方法中，用数据流程图(DFD)作为描述工具的软件开发阶段是（）",
        "options": ["A.可行性分析", "B.需求分析", "C.概念设计", "D.物理设计"],
        "answer": "B"
    },
    {
        "id": 30,
        "question": "实体与实体的联系，反映在数据上是（）之间的联系",
        "options": ["A.文件", "B.集合", "C.记录", "D.结构"],
        "answer": "C"
    },
    {
        "id": 31,
        "question": "（）是在业务流程分析的基础上，描述实际数据流动和处理过程的图形表示法。",
        "options": ["A.DFD", "B.UML", "C.ER", "D.FLOWCHART"],
        "answer": "A"
    },
    {
        "id": 32,
        "question": "在数据库设计的需求分析阶段，（）是数据库系统中各类数据详细描述的集合，提供了对各类数据描述的集中管理。",
        "options": ["A.DFD", "B.数据字典", "C.实体联系图", "D.数据集"],
        "answer": "B"
    },
    {
        "id": 33,
        "question": "关于主键约束，下列说法正确的是（）。",
        "options": ["A.主键值不为空，也不允许出现重复", "B.主键值不为空，但允许出现重复", "C.主键值允许空，但不允许出现重复", "D.主键值允许空，也允许出现重复"],
        "answer": "A"
    },
    {
        "id": 34,
        "question": "关于参照完整性，下列说法中错误的是（）。",
        "options": ["A.外键属性取值不能为空", "B.关系中不允许引用不存在的实体", "C.可以通过定义外键实现", "D.外键属性取值允许为空"],
        "answer": "A"
    },
    {
        "id": 35,
        "question": "在关系数据库中，'关系中不允许出现相同的元组'的约束可以通过定义（）实现的",
        "options": ["A.超键", "B.主键", "C.外键", "D.check约束"],
        "answer": "B"
    },
    {
        "id": 36,
        "question": "在实际应用中，常常需要在表中定义非空约束。数据库中的空值表示什么（）。",
        "options": ["A.0", "B.默认值", "C.不确定", "D.空格"],
        "answer": "C"
    },
    {
        "id": 37,
        "question": "下列不属于关系数据库中的约束的是（）。",
        "options": ["A.主键约束", "B.外键约束", "C.唯一约束", "D.空值约束"],
        "answer": "D"
    },
    {
        "id": 38,
        "question": "事务必须满足的四个原则是（），一致性，隔离性，持久性。",
        "options": ["A.原子性", "B.完整性", "C.安全性", "D.正确性"],
        "answer": "A"
    },
    {
        "id": 39,
        "question": "事务并发执行时，每个事务不必关心其他事务，如同在单用户环境下执行一样，这个性质称为事务的（）",
        "options": ["A.持久性", "B.一致性", "C.独立性", "D.隔离性"],
        "answer": "D"
    },
    {
        "id": 40,
        "question": "一个事务中所有对DB的操作是一个不可分割的整体，这个性质称为（）。",
        "options": ["A.完整性", "B.一致性", "C.隔离性", "D.原子性"],
        "answer": "D"
    },
    {
        "id": 41,
        "question": "当多个事务同时读取或修改相同的数据库资源时，（）是进行并发控制的主要方法。",
        "options": ["A.锁", "B.互斥", "C.隔离", "D.游标"],
        "answer": "A"
    },
    {
        "id": 42,
        "question": "（）是构成单一逻辑工作单元的操作集合，这些操作或者全部执行，或者全部不执行。",
        "options": ["A.事务", "B.存储过程", "C.数据库对象", "D.触发器"],
        "answer": "A"
    },
    {
        "id": 43,
        "question": "SQL中，下列涉及空值的操作，不正确的是（）。",
        "options": ["A.AGE=NULL", "B.AGE IS NOT NULL", "C.AGE IS NULL", "D.NOT(AGE IS NULL)"],
        "answer": "A"
    },
    {
        "id": 44,
        "question": "在SQL语句中，与X BETWEEN 20 AND 30等价的表达式是（）",
        "options": ["A.X>=20 AND X<30", "B.X>20 AND X<30", "C.X>20 AND X<=30", "D.X>=20 AND X<=30"],
        "answer": "D"
    },
    {
        "id": 45,
        "question": "关于SQL，下列说法正确的是（）。",
        "options": ["A.是过程化语言", "B.是机器语言", "C.是面向对象语言", "D.是非过程化语言"],
        "answer": "D"
    },
    {
        "id": 46,
        "question": "当SELECT语句返回的结果是一个集合时，可以借助（）对其中的单行记录进行处理。",
        "options": ["A.锁", "B.游标", "C.索引", "D.存储过程"],
        "answer": "B"
    },
    {
        "id": 47,
        "question": "在SELECT语句中，能够实现对查询结果排序的操作是（）",
        "options": ["A.COUNT", "B.ORDER BY", "C.GROUP BY", "D.INDEX"],
        "answer": "B"
    },
    {
        "id": 48,
        "question": "分组查询需要用到的操作是（）",
        "options": ["A.COUNT", "B.ORDER BY", "C.GROUP BY", "D.DISTINCT"],
        "answer": "C"
    },
    {
        "id": 49,
        "question": "SQL查询语句中，SELECT子句对应于关系代数中的（）操作",
        "options": ["A.选择", "B.投影", "C.笛卡尔积", "D.自然连接"],
        "answer": "B"
    },
    {
        "id": 50,
        "question": "SQL查询语句中，WHERE子句对应于关系代数中的（）操作",
        "options": ["A.选择", "B.投影", "C.笛卡尔积", "D.自然连接"],
        "answer": "A"
    },
    {
        "id": 51,
        "question": "SQL查询语句中，FROM子句对应于关系代数中的（）操作",
        "options": ["A.选择", "B.投影", "C.笛卡尔积", "D.自然连接"],
        "answer": "C"
    },
    {
        "id": 52,
        "question": "关系代数中的（）操作是对一个关系进行水平分割",
        "options": ["A.选择", "B.投影", "C.笛卡尔积", "D.自然连接"],
        "answer": "A"
    },
    {
        "id": 53,
        "question": "关系代数中的（）操作是对一个关系进行垂直分割。",
        "options": ["A.选择", "B.投影", "C.笛卡尔积", "D.自然连接"],
        "answer": "B"
    },
    {
        "id": 54,
        "question": "设关系R、S和W的属性个数分别为2、3和4，则这三个关系的笛卡尔积的属性个数为（）",
        "options": ["A.9", "B.4", "C.24", "D.2"],
        "answer": "A"
    },
    {
        "id": 55,
        "question": "设关系R、S和W的元组个数分别为2、3和4，则这三个关系的笛卡尔积的元组个数为（）",
        "options": ["A.9", "B.4", "C.24", "D.2"],
        "answer": "C"
    },
    {
        "id": 56,
        "question": "下列哪个数据类型用于存储可变长字符串（）",
        "options": ["A.CHAR", "B.VARCHAR", "C.DECIMAL", "D.TINYINT"],
        "answer": "B"
    },
    {
        "id": 57,
        "question": "下列说法错误的是（）",
        "options": ["A.MySQL支持多种Unicode字符集", "B.MySQL不支持Unicode字符集", "C.Unicode编码有利于支持跨语言跨平台转换", "D.GBK字符集不兼容Unicode"],
        "answer": "B"
    },
    {
        "id": 58,
        "question": "已知课程表包括课程号，课程名和学分三个字段，课程号已被定义为主键，现要求限定课程名的取值不能重复，则应该在课程名字段上定义（）约束。",
        "options": ["A.PRIMARY KEY", "B.UNIQUE", "C.CHECK", "D.FOREIGN KEY"],
        "answer": "B"
    },
    {
        "id": 59,
        "question": "已知商品表包括商品编号，商品名和价格三个字段，商品编号已被定义为主键，现要求限定商品名的取值不能重复，则应该在商品名字段上定义（）约束。",
        "options": ["A.PRIMARY KEY", "B.UNIQUE", "C.CHECK", "D.FOREIGN KEY"],
        "answer": "B"
    },
    {
        "id": 60,
        "question": "将年龄字段限制在某个取值范围，应定义（）约束。",
        "options": ["A.CHECK", "B.UNIQUE", "C.PRIMARY KEY", "D.FOREIGN KEY"],
        "answer": "A"
    },
    {
        "id": 61,
        "question": "将性别字段设置为仅允许'男'和'女'两种取值，应定义（）约束。",
        "options": ["A.CHECK", "B.UNIQUE", "C.PRIMARY KEY", "D.FOREIGN KEY"],
        "answer": "A"
    },
    {
        "id": 62,
        "question": "下列关于ALTER TABLE语句描述错误的是（）。",
        "options": ["A.ALTER TABLE语句可以添加字段", "B.ALTER TABLE语句可以删除字段", "C.ALTER TABLE语句不能修改字段名称", "D.ALTER TABLE语句可以修改字段的数据类型"],
        "answer": "C"
    },
    {
        "id": 63,
        "question": "若要删除数据库中已经存在的表S，可以执行（）。",
        "options": ["A.DELETE TABLE S", "B.DELETE S", "C.DROP TABLE S", "D.DROP S"],
        "answer": "C"
    },
    {
        "id": 64,
        "question": "若要删除数据库中的视图v，可以执行（）。",
        "options": ["A.DELETE VIEW v", "B.DELETE v", "C.DROP VIEW v", "D.DROP v"],
        "answer": "C"
    },
    {
        "id": 65,
        "question": "若要删除数据库tb，可以执行（）。",
        "options": ["A.DELETE DATABASE tb", "B.DELETE tb", "C.DROP DATABASE tb", "D.DROP tb"],
        "answer": "C"
    },
    {
        "id": 66,
        "question": "下列关于数据库索引的说法，错误的是（）",
        "options": ["A.索引可以显著提高查询效率", "B.索引会降低插入、更新、删除数据的性能", "C.一个表只能创建一个索引", "D.主键列默认会自动创建索引"],
        "answer": "C"
    },
    {
        "id": 67,
        "question": "下列关于数据库视图的说法，正确的是（）",
        "options": ["A.视图中实际存储了真实数据", "B.视图可以简化复杂查询，隐藏部分字段", "C.对视图的查询一定比直接查表更快", "D.任何视图都可以随意执行UPDATE操作"],
        "answer": "B"
    },
    {
        "id": 68,
        "question": "下列操作中，无法直接通过视图实现的是（）",
        "options": ["A.查询数据", "B.限制用户只能查看部分列", "C.永久存储大量原始数据", "D.基于多张表创建一个虚拟表"],
        "answer": "C"
    },
    {
        "id": 69,
        "question": "下列关于存储过程的描述，错误的是（）",
        "options": ["A.存储过程编译后可重复执行，提高效率", "B.存储过程可以封装多条SQL语句", "C.存储过程必须每次执行都重新编译", "D.存储过程可以接收输入参数"],
        "answer": "C"
    },
    {
        "id": 70,
        "question": "使用存储过程的主要优点不包括（）",
        "options": ["A.减少网络传输", "B.简化复杂业务逻辑调用", "C.永久保存业务数据", "D.提高代码复用性"],
        "answer": "C"
    },
    {
        "id": 71,
        "question": "下列关于触发器的描述，正确的是（）",
        "options": ["A.触发器需要手动调用才能执行", "B.触发器由增、删、改操作自动触发", "C.触发器只能作用于查询语句", "D.触发器会永久存储业务数据"],
        "answer": "B"
    },
    {
        "id": 72,
        "question": "下列操作中，通常不能触发触发器的是（）",
        "options": ["A.INSERT", "B.UPDATE", "C.DELETE", "D.SELECT"],
        "answer": "D"
    },
    {
        "id": 73,
        "question": "满足第一范式（1NF）的核心要求是（）",
        "options": ["A.消除非主属性对主键的部分函数依赖", "B.每个属性都是不可再分的原子值", "C.消除非主属性对主键的传递函数依赖", "D.消除多值依赖"],
        "answer": "B"
    },
    {
        "id": 74,
        "question": "下列关于第三范式（3NF）的说法，正确的是（）",
        "options": ["A.允许存在部分依赖", "B.不允许非主属性之间存在传递依赖", "C.必须先满足BCNF才能满足3NF", "D.字段可以包含多个值用逗号分隔"],
        "answer": "B"
    },
    {
        "id": 75,
        "question": "满足第二范式（2NF）的前提是已经满足第一范式，并且在此基础上必须满足（）",
        "options": ["A.消除非主属性对主键的部分函数依赖", "B.消除非主属性对主键的传递函数依赖", "C.所有字段都是不可再分的原子值", "D.消除多值依赖"],
        "answer": "A"
    }
]

true_false_questions = [
    {
        "id": 1,
        "question": "数据库管理系统是为数据库的建立、使用和维护而配置的应用软件。",
        "answer": "F"
    },
    {
        "id": 2,
        "question": "数据库管理系统是为数据库的建立、使用和维护而配置的系统软件。",
        "answer": "T"
    },
    {
        "id": 3,
        "question": "内模式描述数据库用户能够看见和使用的局部数据的逻辑结构和特征。",
        "answer": "F"
    },
    {
        "id": 4,
        "question": "外模式描述数据库用户能够看见和使用的局部数据的逻辑结构和特征。",
        "answer": "T"
    },
    {
        "id": 5,
        "question": "数据库的概念模型独立于计算机硬件和DBMS。",
        "answer": "T"
    },
    {
        "id": 6,
        "question": "数据库的概念模型与DBMS相关。",
        "answer": "F"
    },
    {
        "id": 7,
        "question": "ER图是在业务流程分析的基础上，描述实际数据流动和处理过程的图形表示法。",
        "answer": "F"
    },
    {
        "id": 8,
        "question": "ER图用于构建数据库的概念模型。",
        "answer": "T"
    },
    {
        "id": 9,
        "question": "在信息系统的设计中，普遍采用的是基于2NF的系统设计方法。",
        "answer": "F"
    },
    {
        "id": 10,
        "question": "在信息系统的设计中，普遍采用的是基于3NF的系统设计方法。",
        "answer": "T"
    },
    {
        "id": 11,
        "question": "第三范式（3NF）要求消除传递函数依赖。",
        "answer": "T"
    },
    {
        "id": 12,
        "question": "第二范式(2NF)需要消除非主属性对主键的传递依赖。",
        "answer": "F"
    },
    {
        "id": 13,
        "question": "为了节约存储空间，关系型数据库中不允许存在数据冗余。",
        "answer": "F"
    },
    {
        "id": 14,
        "question": "关系型数据库中允许存在一定的数据冗余，适当冗余可以提升查询效率。",
        "answer": "T"
    },
    {
        "id": 15,
        "question": "DBS指的是数据库管理系统。",
        "answer": "F"
    },
    {
        "id": 16,
        "question": "DBMS指的是数据库管理系统。",
        "answer": "T"
    },
    {
        "id": 17,
        "question": "数据库管理员的英文缩写是DBA。",
        "answer": "T"
    },
    {
        "id": 18,
        "question": "数据库管理员的英文缩写是ADMIN。",
        "answer": "F"
    },
    {
        "id": 19,
        "question": "MySQL服务的默认端口号是8080。",
        "answer": "F"
    },
    {
        "id": 20,
        "question": "MySQL服务的默认端口号是3306。",
        "answer": "T"
    },
    {
        "id": 21,
        "question": "经常进行增删改操作的表不适合建立索引。",
        "answer": "T"
    },
    {
        "id": 22,
        "question": "经常进行增删改操作的表适合建立索引。",
        "answer": "F"
    },
    {
        "id": 23,
        "question": "存储过程是存储在客户端的SQL程序。",
        "answer": "F"
    },
    {
        "id": 24,
        "question": "存储过程是存储在数据库服务器端的SQL程序，可被重复调用执行。",
        "answer": "T"
    },
    {
        "id": 25,
        "question": "触发器可通过其名字被用户直接调用。",
        "answer": "F"
    },
    {
        "id": 26,
        "question": "触发器能够被插入、删除和修改操作触发执行。",
        "answer": "T"
    },
    {
        "id": 27,
        "question": "数据库需求分析的目的是建立数据的概念模型。",
        "answer": "F"
    },
    {
        "id": 28,
        "question": "视图是虚拟表，因此不会实际存储数据。",
        "answer": "T"
    },
    {
        "id": 29,
        "question": "视图可以独立于基本表单独存在。",
        "answer": "F"
    },
    {
        "id": 30,
        "question": "索引可以加快查询速度，也能提升增删改效率。",
        "answer": "F"
    },
    {
        "id": 31,
        "question": "一张表只能创建一个唯一索引。",
        "answer": "F"
    },
    {
        "id": 32,
        "question": "一张表可以创建多个唯一索引。",
        "answer": "T"
    },
    {
        "id": 33,
        "question": "数据库三大完整性包括实体完整性、参照完整性、用户自定义完整性。",
        "answer": "T"
    },
    {
        "id": 34,
        "question": "主键值不为空，也不允许出现重复值。",
        "answer": "T"
    },
    {
        "id": 35,
        "question": "外键可以实现参照完整性。",
        "answer": "T"
    },
    {
        "id": 36,
        "question": "将年龄字段限制在某个取值范围，应定义UNIQUE约束。",
        "answer": "F"
    },
    {
        "id": 37,
        "question": "将年龄字段限制在某个取值范围，应定义CHECK约束。",
        "answer": "T"
    },
    {
        "id": 38,
        "question": "UNIQUE约束用于在非主键列限定取值的唯一性。",
        "answer": "T"
    },
    {
        "id": 39,
        "question": "主键约束和唯一约束都不允许字段重复。",
        "answer": "T"
    },
    {
        "id": 40,
        "question": "选择是对一个关系进行水平分割。",
        "answer": "T"
    },
    {
        "id": 41,
        "question": "投影是对一个关系进行垂直分割。",
        "answer": "T"
    },
    {
        "id": 42,
        "question": "自然连接会自动判断两个表中所有同名的列，然后在这些列上做等值连接，最后结果中只保留一列。",
        "answer": "T"
    },
    {
        "id": 43,
        "question": "笛卡尔积是两张表无条件连接的结果。",
        "answer": "T"
    },
    {
        "id": 44,
        "question": "数据库中的空值表示空字符。",
        "answer": "F"
    },
    {
        "id": 45,
        "question": "数据库中的空值表示0。",
        "answer": "F"
    },
    {
        "id": 46,
        "question": "CHAR用于存储可变长字符串。",
        "answer": "F"
    },
    {
        "id": 47,
        "question": "CHAR用于存储固定长度字符串。",
        "answer": "T"
    },
    {
        "id": 48,
        "question": "事务的四大特性简称为ACID。",
        "answer": "T"
    },
    {
        "id": 49,
        "question": "事务必须满足原子性。",
        "answer": "T"
    },
    {
        "id": 50,
        "question": "一个事务中所有对DB的操作是一个不可分割的整体，这个性质称为原子性。",
        "answer": "T"
    },
    {
        "id": 51,
        "question": "当多个事务同时读取或修改相同的数据库资源时，可以采用封锁进行并发控制。",
        "answer": "T"
    },
    {
        "id": 52,
        "question": "SQL语言是一种非过程性语言。",
        "answer": "T"
    },
    {
        "id": 53,
        "question": "当SELECT语句返回的结果是一个集合时，可以借助游标对其中的单行记录进行处理。",
        "answer": "T"
    },
    {
        "id": 54,
        "question": "SELECT子句对应于关系代数中的选择操作。",
        "answer": "F"
    },
    {
        "id": 55,
        "question": "FROM子句对应于关系代数中的笛卡尔积操作。",
        "answer": "T"
    },
    {
        "id": 56,
        "question": "WHERE子句对应于关系代数中的投影操作。",
        "answer": "F"
    },
    {
        "id": 57,
        "question": "删除数据库中已存在的表t，应执行delete t。",
        "answer": "F"
    },
    {
        "id": 58,
        "question": "删除数据库中已存在的视图t，应执行delete t。",
        "answer": "F"
    },
    {
        "id": 59,
        "question": "DELETE语句删除表数据，DROP语句删除整张数据表。",
        "answer": "T"
    },
    {
        "id": 60,
        "question": "SQL语言分为数据定义、数据操纵、数据控制等部分。",
        "answer": "T"
    },
    {
        "id": 61,
        "question": "SQL语言中的数据控制用于对表数据进行增删改查操作。",
        "answer": "F"
    },
    {
        "id": 62,
        "question": "SQL语言中的数据操纵用于对表数据进行增删改查操作。",
        "answer": "T"
    },
    {
        "id": 63,
        "question": "DISTINCT关键字用于去除查询结果重复数据。",
        "answer": "T"
    },
    {
        "id": 64,
        "question": "UNIQUE关键字用于去除查询结果重复数据。",
        "answer": "F"
    },
    {
        "id": 65,
        "question": "GROUP BY用于对查询结果进行分组统计。",
        "answer": "T"
    },
    {
        "id": 66,
        "question": "聚合函数SUM、AVG会自动忽略NULL值。",
        "answer": "T"
    },
    {
        "id": 67,
        "question": "聚合函数COUNT会自动忽略NULL值。",
        "answer": "F"
    },
    {
        "id": 68,
        "question": "DROP TABLE仅删除表中数据，不删除表结构。",
        "answer": "F"
    },
    {
        "id": 69,
        "question": "ORDER BY默认排序为降序（DESC）。",
        "answer": "F"
    },
    {
        "id": 70,
        "question": "ORDER BY默认排序为升序（ASC）。",
        "answer": "T"
    }
]

design_questions = [
    {
        "id": 1,
        "question": "一个运动会管理系统数据库中有如下信息：运动员（运动员编号，姓名，性别）、比赛（比赛编号，名称，时间）、裁判员（裁判员编号，姓名）。其中约定：一个运动员可参加多场比赛，一场比赛可有多个运动员参加，运动员参加比赛产生成绩；一场比赛有一个裁判员，一个裁判员可主持多场比赛。请根据以上描述设计ER图。",
        "answer": "ER图中包括三个实体：比赛实体包括比赛编号、名称、时间三个属性，比赛编号为标识；运动员实体包括运动员编号、姓名、性别三个属性，运动员编号为标识；裁判员实体包括裁判员编号、姓名两个属性，裁判员编号为标识。实体之间的联系包括：裁判员和比赛实体之间存在1：N联系；比赛和运动员实体之间存在M：N联系，且该联系拥有一个成绩属性。",
        "analysis": "本题考查ER图设计。首先识别三个实体：运动员、比赛、裁判员。运动员和比赛之间是多对多关系（M:N），因为一个运动员可以参加多场比赛，一场比赛可以有多个运动员参加。这种M:N关系需要单独设计为一个关系模式，并包含成绩属性。裁判员和比赛之间是一对多关系（1:N），因为一个裁判员可以主持多场比赛，但一场比赛只有一个裁判员。"
    },
    {
        "id": 2,
        "question": "一个仓库管理数据库中有如下信息：仓库：仓库号，地址，电话；零件：零件号，零件名称，规格，单价；管理员：工号，姓名，性别。其中约定：一种零件可存放在多个仓库中，一个仓库可存放多种零件，零件存放在仓库中有库存量。一个仓库有多名管理员，一个管理员仅可以管理一个仓库。请根据以上描述设计ER图。",
        "answer": "ER图中包括三个实体：仓库实体包括仓库号、地址、电话三个属性，仓库号为标识；零件实体包括零件号、零件名称、规格、单价四个属性，零件号为标识；管理员实体包括工号、姓名、性别三个属性，工号为标识。实体之间的联系包括：仓库和管理员实体之间存在1：N联系；仓库和零件实体之间存在M：N联系，且该联系拥有一个库存量属性。",
        "analysis": "本题考查ER图设计。仓库和零件之间是M:N关系，需要转换为独立的关系模式（库存表），包含仓库号、零件号和库存量。仓库和管理员之间是1:N关系，管理员属于某个仓库，通过外键关联。"
    },
    {
        "id": 3,
        "question": "设有关系模式R（工号，姓名，性别，部门号，部门名，部门负责人），若规定：一个职工属于一个部门，一个部门有多名职工，一个部门仅有一个负责人，每个负责人仅能负责一个部门。（1）R最高符合第几范式，说明理由；（2）若R不是3NF，将其分解为3NF，并指定其中的主键和外键。",
        "answer": "（1）R最高符合2NF。由于R的主键是单一属性工号，因此必然是2NF。又由于工号->部门号，且部门号->部门名，因此工号->部门名是一个传递函数依赖，则R不符合3NF。（2）R1(工号，姓名，性别，部门号)，其中工号为主键，部门号为外键；R2（部门号，部门名，部门负责人），其中部门号为主键。",
        "analysis": "本题考查关系规范化。2NF要求消除非主属性对主键的部分函数依赖，由于主键是单一属性工号，自然满足2NF。3NF要求消除非主属性对主键的传递函数依赖，这里部门名通过部门号传递依赖于工号，所以不符合3NF。分解时需要将部门相关信息分离到独立的关系模式中。"
    },
    {
        "id": 4,
        "question": "设有关系模式R（学号，姓名，性别，图书号，图书名，出版社，借阅时间），若规定，一个学生可以借阅多本图书，一本图书一次仅能借给一个学生。（1）R最高符合第几范式，说明理由；（2）若R不是3NF，将其分解为3NF，并指定其中的主键和外键。",
        "answer": "（1）R最高符合1NF。由于R的主键是（学号，图书号，借阅时间）。由于（学号，图书号，借阅时间）->姓名，并且学号->姓名，因此R中存在主键到非主属性的部分函数依赖，所以R不符合2NF。（2）R1（学号，姓名，性别），其中学号为主键；R2（图书号，图书名，出版社），其中图书号为主键；R3（学号，图书号，借阅时间），其中（学号，图书号，借阅时间）为联合主键，且存在两个外键：学号，图书号。",
        "analysis": "本题考查关系规范化。主键是（学号，图书号，借阅时间）的组合键，但姓名只依赖于学号，这是部分函数依赖，违反了2NF。分解时需要将学生信息、图书信息和借阅关系分别存储在不同的关系模式中。"
    },
    {
        "id": 5,
        "question": "根据以下ER图设计数据库表，要求给出表名、字段名、主键和外键的设计。运动员（运动员编号，姓名，性别）、裁判（裁判员编号，姓名）、比赛（比赛编号，名称，时间）、参加（比赛编号，运动员编号，成绩）",
        "answer": "运动员（运动员编号，姓名，性别）运动员编号为主键；裁判（裁判员编号，姓名）裁判员编号为主键；比赛（比赛编号，名称，时间，裁判员编号）比赛编号为主键，裁判员编号为外键（引用裁判表的主键）；参加（比赛编号，运动员编号，成绩）比赛编号和运动员编号为联合主键。比赛编号为外键（引用比赛表主键），运动员编号为外键（引用运动员表主键）。",
        "analysis": "本题考查ER图到关系模式的转换。实体直接转换为关系，1:N联系通过外键实现（比赛表中的裁判员编号），M:N联系转换为独立关系（参加表），包含双方主键作为联合主键，并添加联系属性（成绩）。"
    }
]

sql_questions = [
    {
        "id": 1,
        "question": "已知MySQL服务器上的商品销售数据库（sales）中包括三张表：员工信息表employee（eid，ename，age，sex，tel）；商品信息表goods（gid，gname，type，price）；销售信息表eg（eid，gid，quantity，saledate）。写出创建sales数据库的SQL语句。",
        "answer": "CREATE DATABASE sales;",
        "analysis": "本题考查DDL语句中的数据库创建。使用CREATE DATABASE语句创建数据库，数据库名称为sales。创建后需要使用USE sales;切换到该数据库才能创建表。"
    },
    {
        "id": 2,
        "question": "向商品信息表goods中插入一条记录（商品编号为'BX001'，商品名称为'蓝牙耳机'，商品类别为'数码配件'，价格为299.00），写出SQL语句。",
        "answer": "INSERT INTO goods VALUES ('BX001', '蓝牙耳机', '数码配件', 299.00);",
        "analysis": "本题考查DML语句中的INSERT操作。INSERT INTO语句用于向表中插入新记录，VALUES子句中的值需要与表结构的字段顺序一致。字符型数据需要用单引号括起来。"
    },
    {
        "id": 3,
        "question": "删除工号为'1001'的员工的记录，写出SQL语句。",
        "answer": "DELETE FROM employee WHERE eid = '1001';",
        "analysis": "本题考查DML语句中的DELETE操作。DELETE FROM语句用于删除表中的记录，WHERE子句指定删除条件。执行删除操作时要特别小心，没有WHERE条件会删除表中所有记录。"
    },
    {
        "id": 4,
        "question": "将工号为'1001'的员工的电话修改为'13856789012'，写出SQL语句。",
        "answer": "UPDATE employee SET tel = '13856789012' WHERE eid = '1001';",
        "analysis": "本题考查DML语句中的UPDATE操作。UPDATE语句用于修改表中已有的记录，SET子句指定要修改的字段和新值，WHERE子句指定修改条件。没有WHERE条件会修改表中所有记录。"
    },
    {
        "id": 5,
        "question": "查询年龄在40到50岁之间（含40,50）的员工信息，按年龄由小到大排序；写出SQL语句。",
        "answer": "SELECT * FROM employee WHERE age BETWEEN 40 AND 50 ORDER BY age ASC;",
        "analysis": "本题考查SELECT查询语句。BETWEEN...AND用于查询范围内的值，包含边界值。ORDER BY用于排序，ASC表示升序（默认），DESC表示降序。"
    },
    {
        "id": 6,
        "question": "查询所有姓李的员工的工号，姓名以及电话；写出SQL语句。",
        "answer": "SELECT eid, ename, tel FROM employee WHERE ename LIKE '李%';",
        "analysis": "本题考查LIKE模糊查询。'%'是通配符，表示任意长度的任意字符。'李%'表示以'李'开头的任意字符串。如果要查询包含'李'的姓名，可以使用'%李%'。"
    },
    {
        "id": 7,
        "question": "创建存储过程，统计各类别商品的平均价格；写出SQL语句。",
        "answer": "DELIMITER $$\nCREATE PROCEDURE myproc()\nBEGIN\n    SELECT type, AVG(price) FROM goods GROUP BY type;\nEND $$\nDELIMITER ;",
        "analysis": "本题考查存储过程的创建。DELIMITER用于临时改变语句结束符，避免与存储过程中的分号冲突。AVG()是聚合函数用于计算平均值，GROUP BY用于按类别分组统计。"
    },
    {
        "id": 8,
        "question": "查询员工李华销售出的商品的总数量；写出SQL语句。",
        "answer": "SELECT SUM(quantity) FROM employee, eg WHERE employee.eid = eg.eid AND ename = '李华';",
        "analysis": "本题考查多表连接查询和聚合函数。需要将employee表和eg表通过eid进行连接，使用SUM()函数计算总销量。也可以使用JOIN语法：SELECT SUM(quantity) FROM employee JOIN eg ON employee.eid = eg.eid WHERE ename = '李华';"
    },
    {
        "id": 9,
        "question": "查询在2017年10月1日销售业绩为0的员工的工号和姓名；写出SQL语句。",
        "answer": "SELECT eid, ename FROM employee WHERE eid NOT IN (SELECT eid FROM eg WHERE saledate = '2017-10-01');",
        "analysis": "本题考查子查询和NOT IN操作符。首先通过子查询找出当天有销售记录的员工，然后使用NOT IN找出不在这个集合中的员工，即当天没有销售的员工。"
    },
    {
        "id": 10,
        "question": "利用关系代数表达式查询所有工号为1001的员工所销售商品的名称以及销售时间。（关系代数操作用文字描述即可）",
        "answer": "goods表与eg表做自然连接操作，然后基于条件eid='1001'进行选择操作，最后在gname和saledate属性做投影操作。",
        "analysis": "本题考查关系代数操作。自然连接会自动匹配相同名称的属性（gid），选择操作筛选出工号为1001的记录，投影操作只保留需要的列（gname和saledate）。关系代数表达式：π(gname, saledate)(σ(eid='1001')(goods ⨯ eg)) 或使用自然连接：π(gname, saledate)(σ(eid='1001')(goods ⨯ eg))"
    }
]

def get_exam_questions(subject_code="CS201"):
    import random
    
    if subject_code == "CS201":
        selected_single = random.sample(single_choice_questions, 10)
        selected_truefalse = random.sample(true_false_questions, 15)
        selected_design = random.sample(design_questions, 2)
        selected_sql = random.sample(sql_questions, 3)
        
        return {
            "single_choice": selected_single,
            "true_false": selected_truefalse,
            "design": selected_design,
            "sql": selected_sql
        }
    else:
        sample_questions = [
            {
                "id": 1,
                "question": "以下关于" + subject_code + "的说法，正确的是？",
                "options": ["A. 选项A", "B. 选项B", "C. 选项C", "D. 选项D"],
                "answer": "A"
            },
            {
                "id": 2,
                "question": "在" + subject_code + "中，以下哪个是正确的概念？",
                "options": ["A. 概念A", "B. 概念B", "C. 概念C", "D. 概念D"],
                "answer": "B"
            },
            {
                "id": 3,
                "question": "关于" + subject_code + "的基本原理，描述正确的是？",
                "options": ["A. 原理A", "B. 原理B", "C. 原理C", "D. 原理D"],
                "answer": "C"
            },
            {
                "id": 4,
                "question": "在" + subject_code + "中，常用的算法有哪些？",
                "options": ["A. 算法A", "B. 算法B", "C. 算法C", "D. 以上都是"],
                "answer": "D"
            },
            {
                "id": 5,
                "question": "以下哪个不是" + subject_code + "的核心概念？",
                "options": ["A. 概念A", "B. 概念B", "C. 概念C", "D. 概念D"],
                "answer": "D"
            }
        ]
        
        tf_questions = [
            {"id": 1, "question": subject_code + "是计算机科学的重要基础课程。", "answer": "T"},
            {"id": 2, "question": subject_code + "主要研究数据的存储和管理。", "answer": "T"},
            {"id": 3, "question": subject_code + "与编程无关。", "answer": "F"}
        ]
        
        design_questions_sample = [
            {
                "id": 1,
                "question": "请简述" + subject_code + "的核心知识点及其应用场景。",
                "answer": "核心知识点包括：（1）基础概念；（2）核心原理；（3）实践应用。应用场景包括多个领域。",
                "analysis": "本题考查对" + subject_code + "整体知识体系的理解。"
            }
        ]
        
        return {
            "single_choice": sample_questions,
            "true_false": tf_questions,
            "design": design_questions_sample[:2],
            "sql": design_questions_sample[:1]
        }
