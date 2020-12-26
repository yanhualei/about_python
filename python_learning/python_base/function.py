# 二叉树
class Node:  # 节点类
    def __init__(self,elem=-1,lchild=None,rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild


class Tree:  # 树类
    def __init__(self):
        self.my_queue = []
        self.root = Node()


    def add(self,elem):  # 节点的添加方法
        # 添加根节点
        node = Node(elem)
        if self.root.elem == -1:
            self.root = node
            self.my_queue.append(self.root)  # 添加根节点

        else:
            tree_node = self.my_queue[0]
            if tree_node.lchild == None:
                tree_node.lchild = node   # 添加左节点
                self.my_queue.append(tree_node.lchild)
                # self.my_tree.append(tree_node.lchild.elem)
            else:
                tree_node.rchild = node  # 添加右节点
                self.my_queue.append(tree_node.rchild)
                self.my_queue.pop(0)  # 删除根节点，使左节点成为下一个根节点


    def front_digui(self,root):
        if root == None:
            return
        print(root.elem),
        self.front_digui(root.lchild)
        self.front_digui(root.rchild)

    def mid_digui(self,root):
        if root == None:
            return
        self.mid_digui(root.lchild)
        print(root.elem),
        self.mid_digui(root.rchild)

    def later_digui(self,root):
        if root == None:
            return
        self.later_digui(root.lchild)
        self.later_digui(root.rchild)
        print(root.elem),

    def level_queue(self, root):
        """利用队列实现树的层次遍历"""
        if root == None:
            return
        my_queue = []
        my_queue.append(root)
        while my_queue:
            node = my_queue.pop(0)
            print(node.elem)

            if node.lchild != None:
                my_queue.append(node.lchild)
            if node.rchild != None:
                my_queue.append(node.rchild)

    def front_stack(self,root):
        if root == None:
            return
        my_queue = []
        node = root









if __name__ == '__main__':
    elems = [i for i in range(10)]
    tree = Tree()
    for elem in elems:
        tree.add(elem)
    # 树
    # print(tree.my_tree)
    #　先序遍历（根左右：从根节点开始）
    tree.front_digui(tree.root)

    #中序遍历 （左根右：从最深叶子节点开始）
    tree.mid_digui(tree.root)

    # 后序遍历 （左右根：从最深叶子节点开始）
    tree.later_digui(tree.root)

    # 层次遍历
    tree.level_queue(tree.root)











