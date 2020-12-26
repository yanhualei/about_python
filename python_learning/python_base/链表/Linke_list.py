# 节点类
class Node(object):
    # 初始化，需要传入节点的数据
    def __init__(self, data):
        self.data = data
        self.next = None

    # 返回节点的数据
    def get_data(self):
        return self.data

    # 更新节点的数据
    def set_data(self, new_data):
        self.data = new_data

    # 返回后继节点
    def get_next(self):
        return self.next

    # 变更后继节点
    def set_next(self, new_next: object):
        self.next = new_next


# 有序链表类
class Ordered_linked_list(Node):
    # 初始化，头结点为空
    def __init__(self):
        self.head = None

    # 添加节点
    def add(self, data):
        checking = self.head  # 从头结点开始查询
        previous = None  # 记录前一个节点，头结点的前一个节点为None
        while checking != None:
            if checking.get_data() > data:  # 查找到可以插入的位置，跳出循环
                break
            previous = checking  # 更新前一个节点
            checking = checking.get_next()  # 查询下一个节点

        new_node = Node(data)  # 创建新节点
        if previous == None:  # 插入在头结点位置
            new_node.set_next() = self.head
            self.head = new_node
        else:  # 插入在中间或者尾部
            previous.set_next(new_node)
            new_node.set_next(checking)


    # 包含查询，传入值，返回该值在链表中是否存在
    def search(self, data):
        checking = self.head  # 从头结点开始查询
        while checking != None:
            if checking.get_data() == data:  # 查找到，返回True
                return True
            elif checking.get_data() > data:  # 过了需要查询的值
                return False
            checking = checking.get_next()  # 查询下一个节点
        return False  # 遍历到最后也未能找到，返回False


    # 删除节点，将第一个具有传入值的节点从链表中删除
    def remove(self, data):
        checking = self.head  # 从头结点开始查询
        previous = None  # 记录前一个节点，头结点的前一个节点为None

        while checking != None:
            if checking.get_data() == data:  # 查找到，跳出查找循环
                break
            previous = checking  # 更新前一个节点
            checking = checking.get_next()  # 查询下一个节点

        if previous == None:  # 如果头结点便是查找的节点
            self.head = checking.get_next()

        else: # 查找的节点不在头结点，即，存在前驱节点
            previous.set_next(checking.get_next())


    # 判断链表是否为空
    def isEmpty(self):
        return self.head == None


    # 返回链表长度
    def size(self):
        count = 0
        counting = self.head  # 从头结点开始计数
        while counting != None:
            count += 1
            counting = counting.get_next()
        return count

