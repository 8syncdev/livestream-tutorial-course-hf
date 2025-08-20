from typing import (
    TypeVar,
    Generic,
    Optional
)

TemplateDoubleLinkedList = TypeVar('TemplateDoubleLinkedList')

class Node(Generic[TemplateDoubleLinkedList]):

    def __init__(self, 
                    data: Optional['Node'] = None,
                    prev: Optional['Node'] = None,
                    next: Optional['Node'] = None
                ):
        self.data = data
        self.prev = prev
        self.next = next

class DoubleLinkedList(Generic[TemplateDoubleLinkedList]):
    first_node: Optional[Node] = None
    last_node: Optional[Node] = None

    def create_node(self, 
                        data: Optional[TemplateDoubleLinkedList] = None, 
                        position: Optional[int] = -1
                    ):
        
        new_node = Node[TemplateDoubleLinkedList](data=data)

        if DoubleLinkedList.first_node == None:
            DoubleLinkedList.first_node = DoubleLinkedList.last_node = new_node
        
        elif position == 0:
            new_node.next = DoubleLinkedList.first_node
            DoubleLinkedList.first_node.prev = new_node
            DoubleLinkedList.first_node = new_node

        elif position == -1:
            DoubleLinkedList.last_node.next = new_node
            new_node.prev = DoubleLinkedList.last_node
            DoubleLinkedList.last_node = new_node

        else:
            temp_node = DoubleLinkedList.first_node

            while position - 1 > 0:
                temp_node = temp_node.next
            
            current_node = temp_node
            next_node = temp_node.next

            current_node.next = new_node
            new_node.next = next_node

            new_node.prev = current_node
            next_node.prev = new_node

    def delete(self, position: Optional[int] = 0):
        
        if position == 0:
            temp_next_node = DoubleLinkedList.first_node.next
            DoubleLinkedList.first_node.next.prev = None
            DoubleLinkedList.first_node.next = None

            DoubleLinkedList.first_node = temp_next_node
    

    def print_all_nodes(self, reverse: Optional[bool] = False):
        temp_node = DoubleLinkedList.first_node if reverse == False else DoubleLinkedList.last_node

        while temp_node != None:
            print(temp_node.data)
            temp_node = temp_node.next if reverse == False else temp_node.prev


double_linked_list = DoubleLinkedList[int]()
double_linked_list.create_node(data=100)
double_linked_list.create_node(data=200)
double_linked_list.create_node(data=300)

double_linked_list.create_node(data=1000, position=0)

double_linked_list.create_node(data=3000, position=1)

double_linked_list.delete()

double_linked_list.print_all_nodes()
