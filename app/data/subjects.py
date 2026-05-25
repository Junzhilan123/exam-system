subjects = [
    {
        "id": 1,
        "code": "CS201",
        "name": "数据库原理及应用",
        "description": "数据库基础、关系代数、SQL、规范化理论",
        "icon": "📊",
        "color": "purple"
    },
    {
        "id": 2,
        "code": "CS202",
        "name": "数据结构",
        "description": "链表、树、图、排序算法、查找算法",
        "icon": "🌳",
        "color": "green"
    },
    {
        "id": 3,
        "code": "CS203",
        "name": "操作系统",
        "description": "进程管理、内存管理、文件系统、设备管理",
        "icon": "⚙️",
        "color": "blue"
    },
    {
        "id": 4,
        "code": "CS204",
        "name": "计算机网络",
        "description": "TCP/IP、HTTP、网络协议、网络安全",
        "icon": "🌐",
        "color": "orange"
    },
    {
        "id": 5,
        "code": "CS205",
        "name": "数据采集与处理",
        "description": "网络爬虫、HTML/CSS、正则表达式、多线程",
        "icon": "🕷️",
        "color": "teal"
    }
]

def get_subject_by_code(code):
    for subject in subjects:
        if subject['code'] == code:
            return subject
    return None

def get_all_subjects():
    return subjects
