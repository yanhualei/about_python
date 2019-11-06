class Node:
    """节点类"""
    def __init__(self,elem=-1,lchild=None,rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild


class Tree:
    """树类"""
    def __init__(self):
        self.root = Node()
        self.my_tree = []
    def add(self,elem):
        """添加节点"""
        node = Node(elem)
        if self.root.elem == -1:
            self.root = node
            self.my_tree.append(self.root)
            # print(node.elem)
        else:
            tree_node = self.my_tree[0]
            if tree_node.lchild == None:
                tree_node.lchild = node
                self.my_tree.append(tree_node.lchild)
                # print(node.elem)
            else:
                tree_node.rchild = node
                self.my_tree.append(tree_node.rchild)
                self.my_tree.pop(0)
                # print(node.elem)

    def front_digui(self,node):
        """先序递归遍历"""
        if node == None:
            return
        print(node.elem)
        self.front_digui(node.lchild)
        self.front_digui(node.rchild)

    def mid_digui(self,node):
        """中序递归遍历"""
        if node == None:
            return
        self.front_digui(node.lchild)
        print(node.elem)
        self.front_digui(node.rchild)

    def end_digui(self,node):
        """后序递归遍历"""
        if node == None:
            return
        self.front_digui(node.lchild)
        self.front_digui(node.rchild)
        print(node.elem)



if __name__ == '__main__':
    """主函数"""
    tree = Tree()
    elems = range(10)
    for elem in elems:
        tree.add(elem)
    print("------先序递归遍历二叉树------")
    tree.front_digui(tree.root)
    print("------中序递归遍历二叉树------")
    tree.mid_digui(tree.root)
    print("------后序递归遍历二叉树------")
    tree.end_digui(tree.root)



