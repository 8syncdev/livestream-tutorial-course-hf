from typing import (
    Generic,
    TypeVar,
    Optional
)

TemplateDoubleLinkedList = TypeVar('TemplateDoubleLinkedList')


class Node(Generic[TemplateDoubleLinkedList]):

    def __init__(self, 
                    data: Optional[TemplateDoubleLinkedList] = None, 
                    front: Optional['Node'] = None,
                    back: Optional['Node'] = None,
                ):
        self.data = data
        self.front = front
        self.back = back


class DoubleLinkedList(Generic[TemplateDoubleLinkedList]):
    first: Optional[Node] = None
    last: Optional[Node] = None

    def create_node(self, data: TemplateDoubleLinkedList, position: Optional[int] = -1):

        new_node = Node[TemplateDoubleLinkedList](data=data)

        if DoubleLinkedList.first == None:
            DoubleLinkedList.first = new_node
            DoubleLinkedList.last = new_node

        elif position == -1:
            DoubleLinkedList.last.back = new_node
            new_node.front = DoubleLinkedList.last
            DoubleLinkedList.last = new_node

        elif position == 0:
            new_node.back = DoubleLinkedList.first
            DoubleLinkedList.first.front = new_node
            DoubleLinkedList.first = new_node



    def print_all_nodes(self, reverse: Optional[bool] = False):
        temp_node = DoubleLinkedList.first if reverse == False else DoubleLinkedList.last

        while temp_node != None:
            print(temp_node.data)
            temp_node = temp_node.back if reverse == False else temp_node.front


double_linked_list = DoubleLinkedList[int]()
double_linked_list.create_node(data=100)
double_linked_list.create_node(data=200)
double_linked_list.create_node(data=300)

double_linked_list.create_node(data=1000, position=0)

double_linked_list.print_all_nodes(reverse=True)

print()
        