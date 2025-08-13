from typing import Optional, Generic, TypeVar

# TypeVar: cách định nghĩa giá trị biến dùng để lưu dữ liệu
TemplateLinkedList = TypeVar('TemplateLinkedList')

class Node(Generic[TemplateLinkedList]):
    def __init__(self, data: TemplateLinkedList, next_node: Optional['Node'] = None):
        self.data: TemplateLinkedList = data # dữ liệu cần lưu trữ
        self.next_node = next_node # lưu cái ô nhớ tiếp theo

class LinkedList:
    first_node: Optional['Node'] = None

    @staticmethod
    def insert_head(data):
        new_node = Node[int](data=data)
        new_node.next_node = LinkedList.first_node
        LinkedList.first_node = new_node

    @staticmethod
    def print_all_nodes():
        temp = LinkedList.first_node

        while temp != None:
            print(temp.data)
            temp = temp.next_node


node1 = Node[int](data=100)
node2 = Node[int](data=200)
node1.next_node = node2

LinkedList.first_node = node1
LinkedList.insert_head(1000)
LinkedList.insert_head(2000)
LinkedList.print_all_nodes()


