# ds=[1,2,3,4]
# for item in ds:
#     print(id(item))

from typing import Generic, TypeVar, Optional

TemplateLinkedList = TypeVar("TemplateLinkedList")

# TemplateLinkedList.func = lambda x: x

# print(TemplateLinkedList.func())


class Node(Generic[TemplateLinkedList]):

    def __init__(self, data: TemplateLinkedList, next: Optional['Node'] = None):
        self.data = data
        self.next = next


class LinkedList(Generic[TemplateLinkedList]):
    first: Optional[Node] = None
    last: Optional[Node] = None

    def create_node(self, data: TemplateLinkedList, position: Optional[int] = 0):
        new_node = Node[TemplateLinkedList](data=data)

        if LinkedList.first == None and LinkedList.last == None:
            LinkedList.first = LinkedList.last = new_node

        elif position == 0:
            new_node.next = LinkedList.first
            LinkedList.first = new_node

        elif position == -1:
            LinkedList.last.next = new_node
            LinkedList.last = new_node

        else:
            temp_node = LinkedList.first

            while position - 1 > 0:
                temp_node = temp_node.next
            
            new_node.next = temp_node.next
            temp_node.next = new_node


    def print_all_nodes(self):
        temp_node = LinkedList.first

        while temp_node != None:
            print(temp_node.data)
            temp_node=temp_node.next

linked_list = LinkedList[int]()

linked_list.create_node(data=100)
linked_list.create_node(data=200, position=-1)
linked_list.create_node(data=300, position=-1)

linked_list.create_node(data=1000, position=1)

linked_list.print_all_nodes()



