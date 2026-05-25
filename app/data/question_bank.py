question_bank = {
    "CS201": {
        "2026SP": {
            "single_choice": [
                {
                    "id": 1,
                    "question": "数据库系统的核心是？",
                    "options": ["A. 数据库", "B. 数据库管理系统", "C. 数据", "D. 软件"],
                    "answer": "B",
                    "analysis": "数据库管理系统（DBMS）是数据库系统的核心，负责管理和维护数据库。"
                },
                {
                    "id": 2,
                    "question": "以下哪个不是关系数据库的特点？",
                    "options": ["A. 数据独立性", "B. 数据冗余", "C. 数据共享", "D. 数据完整性"],
                    "answer": "B",
                    "analysis": "关系数据库通过规范化设计减少数据冗余，而不是增加冗余。"
                },
                {
                    "id": 3,
                    "question": "SQL语言中，用于查询数据的关键字是？",
                    "options": ["A. INSERT", "B. SELECT", "C. UPDATE", "D. DELETE"],
                    "answer": "B",
                    "analysis": "SELECT是SQL中用于查询数据的关键字。"
                },
                {
                    "id": 4,
                    "question": "在关系模式中，主键的特点是？",
                    "options": ["A. 可以为空", "B. 可以重复", "C. 唯一且不为空", "D. 以上都不对"],
                    "answer": "C",
                    "analysis": "主键必须唯一且不能为空，用于唯一标识一条记录。"
                },
                {
                    "id": 5,
                    "question": "以下哪个范式要求消除非主属性对主键的部分依赖？",
                    "options": ["A. 1NF", "B. 2NF", "C. 3NF", "D. BCNF"],
                    "answer": "B",
                    "analysis": "2NF要求在1NF的基础上消除非主属性对主键的部分函数依赖。"
                }
            ],
            "true_false": [
                {
                    "id": 1,
                    "question": "数据库系统的三级模式结构包括外模式、模式和内模式。",
                    "answer": "T",
                    "analysis": "正确。数据库系统通常采用三级模式结构：外模式（用户视图）、模式（概念视图）、内模式（存储视图）。"
                },
                {
                    "id": 2,
                    "question": "SQL语言是一种过程化语言。",
                    "answer": "F",
                    "analysis": "错误。SQL是一种非过程化语言，用户只需要说明'做什么'，不需要说明'怎么做'。"
                },
                {
                    "id": 3,
                    "question": "在关系数据库中，NULL表示空字符串。",
                    "answer": "F",
                    "analysis": "错误。NULL表示未知或不存在的值，与空字符串不同。"
                }
            ],
            "design": [
                {
                    "id": 1,
                    "question": "设计一个图书馆管理系统的ER图，包含：图书（书号、书名、作者、出版社、价格）、读者（读者号、姓名、性别、年龄）、借阅（借阅日期、归还日期）。",
                    "answer": "ER图包含三个实体：图书（书号为主键）、读者（读者号为主键）、借阅（弱实体，包含借阅日期和归还日期）。借阅是图书和读者之间的M:N联系转换而来的关系。",
                    "analysis": "本题考查ER图设计，需要识别实体、属性和联系类型。"
                },
                {
                    "id": 2,
                    "question": "设有关系模式R(学号,姓名,课程号,课程名,成绩)，指出主键并分解为3NF。",
                    "answer": "主键为（学号，课程号）。分解结果：R1(学号,姓名)，R2(课程号,课程名)，R3(学号,课程号,成绩)。",
                    "analysis": "原关系存在传递依赖：学号→姓名，课程号→课程名，需要分解消除传递依赖。"
                }
            ],
            "sql": [
                {
                    "id": 1,
                    "question": "查询所有姓'张'的学生姓名和学号。",
                    "answer": "SELECT 学号, 姓名 FROM 学生 WHERE 姓名 LIKE '张%';",
                    "analysis": "使用LIKE操作符和通配符%进行模糊查询。"
                },
                {
                    "id": 2,
                    "question": "统计每个学生的平均成绩。",
                    "answer": "SELECT 学号, AVG(成绩) AS 平均成绩 FROM 成绩 GROUP BY 学号;",
                    "analysis": "使用GROUP BY分组统计，AVG()函数计算平均值。"
                }
            ]
        },
        "2025FA": {
            "single_choice": [],
            "true_false": [],
            "design": [],
            "sql": []
        }
    },
    "CS202": {
        "2026SP": {
            "single_choice": [
                {
                    "id": 1,
                    "question": "以下哪种数据结构是线性结构？",
                    "options": ["A. 树", "B. 图", "C. 链表", "D. 堆"],
                    "answer": "C",
                    "analysis": "链表是线性结构，树和图是非线性结构。"
                },
                {
                    "id": 2,
                    "question": "栈的特点是？",
                    "options": ["A. 先进先出", "B. 后进先出", "C. 随机访问", "D. 无序存储"],
                    "answer": "B",
                    "analysis": "栈是后进先出（LIFO）的数据结构。"
                }
            ],
            "fill_blank": [
                {
                    "id": 1,
                    "question": "快速排序的平均时间复杂度是______。",
                    "answer": "O(n log n)",
                    "analysis": "快速排序的平均时间复杂度为O(n log n)，最坏情况为O(n²)。"
                }
            ],
            "code": [
                {
                    "id": 1,
                    "question": "编写一个函数，实现单链表的反转。",
                    "answer": "def reverse_list(head):\n    prev = None\n    current = head\n    while current:\n        next_node = current.next\n        current.next = prev\n        prev = current\n        current = next_node\n    return prev",
                    "analysis": "使用迭代方式反转链表，需要三个指针：prev、current、next_node。"
                }
            ]
        }
    },
    "CS203": {
        "2026SP": {
            "single_choice": [
                {
                    "id": 1,
                    "question": "进程和线程的主要区别是？",
                    "options": ["A. 进程是资源分配的基本单位，线程是CPU调度的基本单位", "B. 线程是资源分配的基本单位，进程是CPU调度的基本单位", "C. 两者没有区别", "D. 以上都不对"],
                    "answer": "A",
                    "analysis": "进程是资源分配的基本单位，线程是CPU调度的基本单位。"
                }
            ],
            "short_answer": [
                {
                    "id": 1,
                    "question": "什么是死锁？产生死锁的必要条件有哪些？",
                    "answer": "死锁是指多个进程因竞争资源而造成的一种僵局，若无外力作用，这些进程都将无法向前推进。死锁的四个必要条件：互斥条件、请求与保持条件、不剥夺条件、循环等待条件。",
                    "analysis": "本题考查死锁的概念和产生条件。"
                }
            ]
        }
    },
    "CS204": {
        "2026SP": {
            "single_choice": [
                {
                    "id": 1,
                    "question": "TCP协议工作在OSI模型的哪一层？",
                    "options": ["A. 网络层", "B. 传输层", "C. 应用层", "D. 数据链路层"],
                    "answer": "B",
                    "analysis": "TCP是传输层协议，提供可靠的端到端通信。"
                }
            ],
            "essay": [
                {
                    "id": 1,
                    "question": "论述TCP三次握手的过程及其作用。",
                    "answer": "TCP三次握手过程：1. 客户端发送SYN=1, seq=x；2. 服务器返回SYN=1, ACK=1, seq=y, ack=x+1；3. 客户端发送ACK=1, seq=x+1, ack=y+1。作用：确保双方都具备发送和接收数据的能力，同步序列号。",
                    "analysis": "三次握手是TCP建立连接的必要过程，用于保证连接的可靠性。"
                }
            ]
        }
    },
    "CS205": {
        "2026SP": {
            "single_choice": [],
            "true_false": [{'question': '网络爬虫是一段脚本或程序。', 'answer': 'T'}, {'question': '网络爬虫并不能自动爬取网络上的信息。', 'answer': 'F'}, {'question': 'Python可以轻松地编写爬虫程序。', 'answer': 'T'}, {'question': '通用网络爬虫并不是一切皆可爬取。', 'answer': 'T'}, {'question': '通用网络爬虫不要遵循Robots协议。', 'answer': 'F'}, {'question': '深层网页可以通过静态链接获取。', 'answer': 'F'}, {'question': '表层网页是指传统搜索引擎可以索引的页面。', 'answer': 'T'}, {'question': '聚焦网络爬虫是为解决通用网络爬虫的缺点而产生的。', 'answer': 'T'}, {'question': '积累式网络爬虫在抓取数据的过程中不会进行重复操作。', 'answer': 'F'}, {'question': '增量式网络爬虫的统一更新法会以相同的频率访问全部网页。', 'answer': 'T'}, {'question': '待下载网页是指待抓取URL队列中的网页页面。', 'answer': 'T'}, {'question': '待下载网页是指不在待抓取队列中的网页页面。', 'answer': 'F'}, {'question': '网络爬虫抓取的宽度优先遍历策略构成一个网页集合，然后在该集合内进行PageRank计算，从而形成URL列表。', 'answer': 'F'}, {'question': '网络爬虫会对被访问的服务器造成很大的访问压力。', 'answer': 'T'}, {'question': '服务器无法识别是浏览器访问还是代码访问。', 'answer': 'F'}, {'question': '服务器是可以识别是浏览器访问还是代码访问。', 'answer': 'T'}, {'question': '数据混淆技术的核心思想是使用错误的数据取代正确的数据返回给网络爬虫。', 'answer': 'T'}, {'question': 'Robots协议是一个必须遵守的标准。', 'answer': 'F'}, {'question': 'Robots协议是一个君子协定。', 'answer': 'T'}, {'question': 'Robots协议可以有效地保护网站的隐私。', 'answer': 'F'}, {'question': '网络爬虫是一个典型的多任务处理场景。', 'answer': 'T'}, {'question': 'Python含有大量的第三方库。', 'answer': 'T'}, {'question': 'Flask适合开发重量级的Web应用。', 'answer': 'F'}, {'question': 'Flask框架的结构是可以扩展的。', 'answer': 'T'}, {'question': 'CherryPY框架本身没有内置Web服务器。', 'answer': 'F'}, {'question': 'Pyramid框架执行效率高，开发周期短。', 'answer': 'T'}, {'question': 'HTML是一种编程语言。', 'answer': 'F'}, {'question': 'Internet起源于1969年美国国防部国防高级研究计划署资助建立了一个名为ARPANET（“阿帕网”）的网络。', 'answer': 'T'}, {'question': 'IP地址(IPV4)采用一个64位的二进制数表示。', 'answer': 'F'}, {'question': '在B/S架构下，不同的服务需要安装不同的客户端软件。', 'answer': 'F'}, {'question': '网页是构成网站的基本元素，网站就是由网页组成的。', 'answer': 'T'}, {'question': '欧洲核子研究中心启动了世界上第一个可以正式访问的网站。', 'answer': 'T'}, {'question': 'HTML是标准通用标记语言下的一个应用，也是一种规范和标准。', 'answer': 'T'}, {'question': 'CSS仅可以静态地修饰网页。', 'answer': 'F'}, {'question': 'JavaScript是一种轻量级、解释型的Web开发语言。', 'answer': 'T'}, {'question': 'HTML5语法中，大小写有严格的要求。', 'answer': 'F'}, {'question': '在HTML5语法中，对于单标签需要闭合操作。', 'answer': 'F'}, {'question': '在HTML5语法中，可以只写属性名。', 'answer': 'T'}, {'question': '图片标签是一个空元素。', 'answer': 'T'}, {'question': '超链接标签就是统一资源定位器。', 'answer': 'T'}, {'question': '锚点链接只能在同一个网页内部。', 'answer': 'F'}, {'question': '无序列表中，各个列表项是并列关系。', 'answer': 'T'}, {'question': '列表标签的特点是整齐、规范、有序。', 'answer': 'T'}, {'question': '自定义列表常用于对术语或名词进行解释和描述。', 'answer': 'T'}, {'question': '表格是由行和列组成的结构化数据集。', 'answer': 'T'}, {'question': '表单使得网页与用户之间进行单向对话。', 'answer': 'F'}, {'question': '表单中的提示信息通常包含一些说明性的文字。', 'answer': 'T'}, {'question': '表单中的表单域是容纳表单元素和提示信息的。', 'answer': 'T'}, {'question': 'CSS实现了结构与表现的分离，对代码的维护也更方便。', 'answer': 'T'}, {'question': 'CSS是由W3C创建和维护的。', 'answer': 'T'}, {'question': 'CSS的不同引入方式对于后期代码维护难度的影响是一样的。', 'answer': 'F'}, {'question': 'CSS的内嵌样式一般会添加在<head>标签中。', 'answer': 'T'}, {'question': 'CSS3的导入式会在网页加载前加载CSS3文件。', 'answer': 'F'}, {'question': 'CSS3的链接式和导入式没有区别，可以随意使用。', 'answer': 'F'}, {'question': 'CSS3的引入方式存在优先等级划分。', 'answer': 'T'}, {'question': 'JavaScript是一种轻量级的直译式编程语言。', 'answer': 'T'}, {'question': 'JavaScript程序需要事先编译后才能运行。', 'answer': 'F'}, {'question': '通常在HTML网页中使用JavaScript为页面增加动态效果。', 'answer': 'T'}, {'question': 'urllib模块无须安装，导入即可使用。', 'answer': 'T'}, {'question': 'urlopen( )方法提供了一个异常处理请求。', 'answer': 'F'}, {'question': 'urlopen( )方法中data参数的默认值为1。', 'answer': 'F'}, {'question': 'urlopen( )方法能够发送一个最基本的网络请求。', 'answer': 'T'}, {'question': '设置headers请求头部信息的目的是伪装成服务器。', 'answer': 'F'}, {'question': '设置代理IP的目的是让服务器知道谁在获取它的数据。', 'answer': 'F'}, {'question': '无法通过URLError类的reason属性去了解错误的原因。', 'answer': 'F'}, {'question': 'HTTPError类用于处理HTTP请求所出现的异常。', 'answer': 'T'}, {'question': 'HTTPError类可以捕获所有的异常。', 'answer': 'F'}, {'question': 'urllib3模块无须安装，导入即可使用。', 'answer': 'F'}, {'question': 'urllib3模块中PoolManager对象只能向一个服务器发生请求。', 'answer': 'F'}, {'question': 'urllib3可以自动重试请求。', 'answer': 'T'}, {'question': '大多数的服务器都会检测请求头信息。', 'answer': 'T'}, {'question': 'urllib3模块中request( )方法提供了文件上传方法。', 'answer': 'T'}, {'question': 'requests模块是Python中自带模块。', 'answer': 'F'}, {'question': 'requests模块可以获取二进制文件。', 'answer': 'T'}, {'question': '在正则表达式中，$表示行的开始。', 'answer': 'F'}, {'question': '在正则表达式中，$表示行的结尾。', 'answer': 'T'}, {'question': '在正则表达式中，？表示匹配前面的字符零次或一次。', 'answer': 'T'}, {'question': '在正则表达式中，+表示匹配前面的字符零次或一次。', 'answer': 'F'}, {'question': '在正则表达式中，*表示匹配前面的字符零次或一次。', 'answer': 'F'}, {'question': '在正则表达式中，选择字符|用于包含条件选择的逻辑。', 'answer': 'T'}, {'question': '在正则表达式中，search( )方法用于从字符串的开始处进行匹配。', 'answer': 'F'}, {'question': '在正则表达式中，findall( )方法搜索匹配的字符串，并以字典的形式返回。', 'answer': 'F'}, {'question': '在正则表达式中，.*?用于实现非贪婪匹配。', 'answer': 'T'}, {'question': 'XPath是XML路径语言，可以实现XML文件搜索。', 'answer': 'T'}, {'question': '在XPath中，parse( )方法主要用于实现解析本地HTML文件。', 'answer': 'T'}, {'question': '在XPath中，@符无法直接获取属性所对应的值。', 'answer': 'F'}, {'question': 'BeautifulSoup是一个用于从HTML文件中提取数据的Python库。', 'answer': 'T'}, {'question': 'BeautifulSoup无法从XML文件中提取数据。', 'answer': 'F'}, {'question': 'BeautifulSoup支持许多第三方Python解析器。', 'answer': 'T'}, {'question': '在BeautifulSoup中，find_all( )方法可以获取符合条件的第一个对象。', 'answer': 'F'}, {'question': '在BeautifulSoup中，find( )方法可以获取第一个匹配的节点内容。', 'answer': 'T'}, {'question': '在BeautifulSoup中，提供了CSS选择器来获取节点内容。', 'answer': 'T'}, {'question': 'AJAX技术可以让浏览器与服务器端进行异步交互。', 'answer': 'T'}, {'question': '进程包含线程。', 'answer': 'T'}, {'question': '线程包含进程。', 'answer': 'F'}, {'question': '使用太多线程是非常耗系统资源的。', 'answer': 'T'}, {'question': '一条线程是进程中一个单一顺序的控制流。', 'answer': 'T'}, {'question': '一个进程无法并发多个线程。', 'answer': 'F'}, {'question': '一个进程可以并发多个线程。', 'answer': 'T'}, {'question': 'threading是高级模块，对_thread模块进行了封装。', 'answer': 'T'}, {'question': 'Thread线程类无法定义它的子类。', 'answer': 'F'}, {'question': '在一个进程内的所有线程共享全局变量。', 'answer': 'T'}, {'question': '在一个进程内的所有线程无法共享全局变量。', 'answer': 'F'}, {'question': '互斥锁保证了每次只有一个线程进行写入操作。', 'answer': 'T'}, {'question': '在使用互斥锁时，要避免死锁。', 'answer': 'T'}, {'question': '进程就是程序，与程序是一回事。', 'answer': 'F'}, {'question': '进程是程序的真正运行实例。', 'answer': 'T'}, {'question': '操作系统无法执行多任务。', 'answer': 'F'}, {'question': '操作系统可以执行多任务。', 'answer': 'T'}, {'question': 'Queue本身是一个消息队列程序。', 'answer': 'T'}, {'question': 'MongoDB支持的数据结构十分松散。', 'answer': 'T'}, {'question': 'PySpider是一个健壮的网络爬虫系统。', 'answer': 'T'}, {'question': 'PySpider没有提供WebUI。', 'answer': 'F'}, {'question': 'PySpider的可扩展程度高。', 'answer': 'F'}, {'question': 'Scrapy的可扩展程度高。', 'answer': 'T'}],
            "multiple_choice": [{'question': '网络爬虫是一段（     ）。', 'options': ['A）程序   B）脚本    C）二进制数据   D）算法  E）信息'], 'answer': 'AB'}, {'question': '网络爬虫又被称为（     ）。', 'options': ['A）算法   B）信息    C）网络蜘蛛   D）网络机器人  E）网页追逐者'], 'answer': 'CDE'}, {'question': '网络爬虫爬取到本地的内容可以是（     ）。', 'options': ['A）HTML代码   B）JSON数据    C）二进制数据   D）图片', 'E）视频'], 'answer': 'ABCDE'}, {'question': '常见的网络爬虫有（     ）。', 'options': ['A） 通用网络爬虫   B）聚焦网络爬虫  C）积累式网络爬虫   D）增量式网络爬虫   E）深层网络爬虫'], 'answer': 'ABCDE'}, {'question': '通用网络爬虫对（     ）要求较高。', 'options': ['A） 算法难度   B）爬行速度  C）机器性能   D）存储空间   E）网络速度'], 'answer': 'BD'}, {'question': '通用网络爬虫的工作流程包括（     ）。', 'options': ['A） 抓取网页   B）存储数据  C）内容处理   D）提供检索   E）排名服务'], 'answer': 'ABCDE'}, {'question': 'Web页面按照存在方式可以分为（     ）。', 'options': ['A） 表层网页   B）数据网页  C）深层网页   D）信息网页   E）链接网页'], 'answer': 'AC'}, {'question': '增量式网络爬虫是（     ）的网络爬虫。', 'options': ['A） 抓取特定信息   B）抓取所有信息  C）采用增量式更新   D）抓取新产生的信息   E）发生变化的信息'], 'answer': 'CDE'}, {'question': '增量式网络爬虫为确保本地页面集中存储的页面是最新页面，经常使用的方法有（     ）。', 'options': ['A） 统一更新法   B）个体更新法  C）基于分类的更新法   D）增量更新法   E）基于算法的更新法'], 'answer': 'ABC'}, {'question': '网络爬虫的基本流程包含有（     ）。', 'options': ['A） 发送请求   B）获取响应内容  C）解析内容   D）保存数据   E）算法选择'], 'answer': 'ABCD'}, {'question': '从网络爬虫的角度可将互联网分为（     ）。', 'options': ['A） 已下载未过期网页   B）已下载已过期网页  C）待下载网页   D）可知网页   E）不可知网页'], 'answer': 'ABCDE'}, {'question': '网络抓取过程中，数据异常主要包括（     ）。', 'options': ['A） 数据无法下载   B）数据格式异常  C）数据内容异常   D）数据无法存储   E）数据不可读写'], 'answer': 'BC'}, {'question': '网络爬虫的危害有（     ）。', 'options': ['A） 性能骚扰   B）法律风险  C）隐私侵犯   D）知识产权侵犯   E）商业机密泄露'], 'answer': 'ABCDE'}, {'question': '网络爬虫的反爬技术有（     ）。', 'options': ['A） 验证码技术   B）Ajax技术  C）数据混淆技术   D）User-Agent控制访问   E）IP地址限制'], 'answer': 'ABCDE'}, {'question': '数据采集对象的线上行为数据包括（    ）。', 'options': ['A）页面数据   B）交互数据   C）表单数据   D）会话数据   E）应用日志'], 'answer': 'ABCD'}, {'question': '数据采集对象的内容数据包括（     ）。', 'options': ['A）应用日志   B）电子文档   C）机器数据   D）语音数据   E）社交媒体数据'], 'answer': 'ABCDE'}, {'question': '数据采集应用场景（    ）。', 'options': ['A）知识信息储备   B）搜索技术   C）过滤广告   D）精准营销   E）用户信息分析'], 'answer': 'ABCDE'}, {'question': 'Python语言用于编写网络爬虫的优势有（     ）。', 'options': ['A）接口丰富、简洁 B）简洁的文档处理功能  C）多种网络爬虫框架  D）多线程、多进程模型成熟  E）语言高级'], 'answer': 'ABCD'}, {'question': 'Python语言可以提供完善的基础代码块，涵盖（     ）等。', 'options': ['A）网络  B）文件  C）GUI   D）数据库  E）文本'], 'answer': 'ABCDE'}, {'question': '基于Python语言的Web开发框架有（     ）。', 'options': ['A）Django  B）CherryPy   C）Flask   D）Pyramid  E）TurboGear'], 'answer': 'ABCDE'}, {'question': 'Django框架开发遵循MVC模式，包括（     ）三部分。', 'options': ['A）数据  B）算法   C）模型   D）视图  E）控制'], 'answer': 'CDE'}, {'question': 'Pyramid框架包含了（     ）的特性。', 'options': ['A）Python  B）Perl   C）Ruby   D）Java   E）C++'], 'answer': 'ABC'}, {'question': 'Web服务器的工作原理包含四个步骤（     ）的特性。', 'options': ['A）建立连接  B）请求过程   C）应答过程   D）关闭连接   E）删除连接'], 'answer': 'ABCD'}, {'question': 'HTTP协议的常用请求方法有（     ）。', 'options': ['A）GET  B）POST   C）PUT   D）DELETE   E）HEAD'], 'answer': 'ABCDE'}, {'question': 'HTTP状态码有（     ）。', 'options': ['A）1**  B）2**   C）3**   D）4**   E）5**'], 'answer': 'ABCDE'}, {'question': '万维网的核心部分是有3个标准构成，其为（     ）。', 'options': ['A）数据库  B）统一资源标识符  C）超文本传输协议  D）客户端  E）超文本标记语言'], 'answer': 'BCE'}, {'question': '网页主要有（     ）3个部分组成。', 'options': ['A）数据库  B）服务器  C）结构  D）表现  E）行为'], 'answer': 'CDE'}, {'question': '标题标签有（     ）。', 'options': ['A）<h1>  B）<h2>  C）<h3>  D）<h4>  E）<h6>'], 'answer': 'ABCDE'}, {'question': '图片标签具有的属性有（     ）。', 'options': ['A）src属性  B）title属性  C）alt属性  D）width属性  E）height属性'], 'answer': 'ABCDE'}, {'question': '超链接具有的伪类是（     ）。', 'options': ['A）href  B）link   C）visited  D）hover  E）active'], 'answer': 'BCDE'}, {'question': '网页中的列表有（     ）。', 'options': ['A）有序列表  B）无序列表   C）自定义列表  D）混合列表  E）数字列表'], 'answer': 'ABC'}, {'question': '一个完整的表单通常由（     ）3部分组成。', 'options': ['A）数据库  B）表单元素  C）提示信息  D）表单域  E）浏览器'], 'answer': 'BCD'}, {'question': '表单中常用的表单元素有（     ）。', 'options': ['A）<input>  B）<select>  C）<textarea>  D）<label>  E）<a>'], 'answer': 'ABCD'}, {'question': '<form>标签中method属性定义表单数据提交方式，常用有（     ）2种方法。', 'options': ['A）get  B）active  C）link  D）post  E）hover'], 'answer': 'AD'}, {'question': 'CSS3有3种引入方式，即（     ）。', 'options': ['A）行内样式  B）内嵌样式  C）外链样式  D）直接样式  E）间接样式'], 'answer': 'ABC'}, {'question': 'CSS3的外链样式有（     ）2种方法。', 'options': ['A）混合式  B）间接式  C）链接式  D）直接式  E）导入式'], 'answer': 'CE'}, {'question': 'CSS3的选择器有（     ）等。', 'options': ['A）标签选择器  B）ID选择器  C）类选择器  D）通用选择器  E）后代选择器'], 'answer': 'ABCDE'}, {'question': 'JavaScript的主要特点有（     ）。', 'options': ['A）脚本语言   B）简单性   C）弱类型   D）跨平台   E）大小写敏感'], 'answer': 'ABCDE'}, {'question': 'Python3中，urllib模块包含（     ）等子模块。', 'options': ['A）urllib.requests  B）urllib.error  C）urllib.parse  D）urllib.robotparser  E）urllib.time'], 'answer': 'ABCD'}, {'question': 'urlopen( )方法的参数有（     ）。', 'options': ['A）url  B）data  C）timeout  D）context  E）cafile'], 'answer': 'ABCDE'}, {'question': '生成urllib.request.Request对象时，可以提供的参数有（     ）。', 'options': ['A）url  B）data  C）headers  D）method  E）origin_reg_host'], 'answer': 'ABCDE'}, {'question': 'urllib模块的urllib.error子模块包含（     ）。', 'options': ['A）URLError类 B）Time类  C）Parse类  D）HTTPError类  E）Data类'], 'answer': 'AD'}, {'question': 'urllib3模块提供的特性有（     ）。', 'options': ['A）线程安全 B）连接池  C）客户端SSL验证  D）支持gzip编码  E）支持HTTP代理'], 'answer': 'ABCDE'}, {'question': 'urllib3模块的request( )方法的参数有（     ）。', 'options': ['A）error  B）method  C）url  D）fields  E）headers'], 'answer': 'BCDE'}, {'question': 'urllib3模块的request( )方法提供了文件上传方法，相应参数为（     ）。', 'options': ['A）fields  B）method  C）body  D）cookie  E）headers'], 'answer': 'AC'}, {'question': 'requests模块提供的特性有（     ）。', 'options': ['A）国际化域名 B）自动内容解码  C）浏览器式的SSL认证  D）自动解压  E）文件分块上传'], 'answer': 'ABCDE'}, {'question': '在正则表达式中，行定位符有（     ）。', 'options': ['A）@  B）^  C）$  D）!  E）%'], 'answer': 'BC'}, {'question': '在正则表达式中，属于元字符的是（     ）。', 'options': ['A）@  B）^  C）$  D）!  E）.'], 'answer': 'BCE'}, {'question': '在正则表达式中，属于常用限定符的是（     ）。', 'options': ['A）?  B）+  C）*  D）!  E）@'], 'answer': 'ABC'}, {'question': '在正则表达式中，进行字符串匹配的常用方法有（     ）。', 'options': ['A）get( )  B）match( )  C）search( )  D）findall( )   E）have( )'], 'answer': 'BCD'}, {'question': '在XPath中，常用路径表达式有（     ）。', 'options': ['A）/  B）//  C）.  D）..   E）nodename'], 'answer': 'ABCDE'}, {'question': '在XPath中，提供的运算符有（     ）。', 'options': ['A）+  B）-  C）*  D）div   E）='], 'answer': 'ABCDE'}, {'question': '在BeautifulSoup中，常用的方法有（     ）。', 'options': ['A）find( )  B）find_all( )  C）find_parent( )  D）find_next( )   E）find_previous( )'], 'answer': 'ABCDE'}, {'question': 'Python的标准库提供了两个线程模块：（     ）。', 'options': ['A）_thread  B）threading  C）_process  D）processing  E）operating'], 'answer': 'AB'}, {'question': 'threading模块提供了一个Thread类来代表一个线程对象，Thread类的参数有（     ）。', 'options': ['A）group  B）target  C）name  D）args  E）kwargs'], 'answer': 'ABCDE'}, {'question': '互斥锁为资源引入了一个状态：（     ）。', 'options': ['A）独立  B）非独立  C）中立  D）锁定  E）非锁定'], 'answer': 'DE'}, {'question': '对于threading模块Lock类，其有（     ）两种方法处理锁定。', 'options': ['A）acquire( )  B）lock( )   C）unlock( )  D）release( )  E）order( )'], 'answer': 'AD'}, {'question': 'Python中有（     ）来创建进程。', 'options': ['A）_thread  B）multiprocessing  C） Pool  D） processing  E）operating'], 'answer': 'BC'}, {'question': 'multiprocessing模块提供了一个Process类来代表一个进程对象，Process类的参数有（     ）。', 'options': ['A）group  B）target  C）name  D）args  E）kwargs'], 'answer': 'ABCDE'}, {'question': '一个Process类的常用方法有（     ）。', 'options': ['A）start( )  B）run( )  C）is_alive( )  D）join( )  E）terminate( )'], 'answer': 'ABCDE'}, {'question': '一个Process类的常用属性有（     ）。', 'options': ['A）group  B）name  C）pid  D）key  E）keys'], 'answer': 'BC'}, {'question': '每一个进程都拥有自己的（     ）。', 'options': ['A）程序  B）地址空间  C）内存  D）数据栈  E）辅助数据'], 'answer': 'BCDE'}, {'question': 'Ajax是（     ）的组合。', 'options': ['A）CSS  B）HTTP  C）JavaScript   D）XML  E）HTML'], 'answer': 'CD'}, {'question': 'Scrapy框架的组成部分有（     ）。', 'options': ['A）引擎  B）调度器  C）下载器   D）网络爬虫  E）项目管道'], 'answer': 'ABCDE'}, {'question': 'PySpider的架构主要有（     ）。', 'options': ['A）引擎  B）调度器  C）抓取器   D）处理器  E）项目管道'], 'answer': 'BCD'}],
            "design": [],
            "sql": []
        }
    }
}

def get_questions_by_subject_semester(subject_code, semester_code):
    if subject_code in question_bank and semester_code in question_bank[subject_code]:
        return question_bank[subject_code][semester_code]
    return {}

def get_all_questions_for_subject(subject_code):
    if subject_code in question_bank:
        all_questions = {}
        for semester in question_bank[subject_code].values():
            for q_type, questions in semester.items():
                if q_type not in all_questions:
                    all_questions[q_type] = []
                all_questions[q_type].extend(questions)
        return all_questions
    return {}

def reload_bank():
    global question_bank
    from app.data.bank_storage import load_bank
    question_bank = load_bank(_DEFAULT_QUESTION_BANK)

def add_question(subject_code, semester_code, question_type, question):
    if subject_code not in question_bank:
        question_bank[subject_code] = {}
    if semester_code not in question_bank[subject_code]:
        question_bank[subject_code][semester_code] = {}
    if question_type not in question_bank[subject_code][semester_code]:
        question_bank[subject_code][semester_code][question_type] = []
    
    max_id = max((q['id'] for q in question_bank[subject_code][semester_code][question_type] if isinstance(q.get('id'), int)), default=0)
    question['id'] = max_id + 1
    question_bank[subject_code][semester_code][question_type].append(question)

    from app.data.bank_storage import save_bank
    save_bank(question_bank)
    return question['id']


_DEFAULT_QUESTION_BANK = question_bank
from app.data.bank_storage import load_bank
question_bank = load_bank(_DEFAULT_QUESTION_BANK)
