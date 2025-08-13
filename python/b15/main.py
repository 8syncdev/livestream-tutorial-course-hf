from typing import Generic, TypeVar, Optional

TemplateLinkedList = TypeVar('TemplateLinkedList')

class Node(Generic[TemplateLinkedList]):

    def __init__(self, data: Optional[TemplateLinkedList] = None, next_node: Optional['Node'] = None):
        self.data = data
        self.next_node = next_node

class LinkedList(Generic[TemplateLinkedList]):

    first_node: Optional[Node] = None
    last_node: Optional[Node] = None

    def create_node(self, data: TemplateLinkedList, position: Optional[int] = -1):
        new_node = Node[TemplateLinkedList](data=data)

        if LinkedList.first_node == None:
            LinkedList.first_node = new_node
            LinkedList.last_node = new_node

        elif position == 0: # Vị trí đầu tiên
            new_node.next_node = LinkedList.first_node
            LinkedList.first_node = new_node # di chuyển quản lí ô nhớ đầu tiền về new_node ô nhớ mới
        
        elif position == self.count() - 1 or position == -1: # thêm vào cuối
            LinkedList.last_node.next_node = new_node
            LinkedList.last_node = new_node
        
        else:
            temp_node = LinkedList.first_node
            while position - 1 > 0:
                temp_node=temp_node.next_node
            
            after_node = temp_node.next_node
            before_node = temp_node

            new_node.next_node = after_node
            before_node.next_node = new_node
    
    def count(self):
        temp_node = LinkedList.first_node
        dem = 0
        while temp_node != None:
            dem += 1
            temp_node = temp_node.next_node
        
        return dem

    def print_all_nodes(self):
        temp_node = LinkedList.first_node

        while temp_node != None:
            print(temp_node.data)
            temp_node = temp_node.next_node


linked_list = LinkedList[int]()
linked_list.create_node(data=100)
linked_list.create_node(data=200)
linked_list.create_node(data=300)

linked_list.create_node(data=1000, position=1)
linked_list.print_all_nodes()