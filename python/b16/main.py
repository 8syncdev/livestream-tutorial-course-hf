# from typing import Generic, TypeVar, Optional

# TemplateLinkedList = TypeVar('TemplateLinkedList')

# class Node(Generic[TemplateLinkedList]):

#     def __init__(self, data: Optional[TemplateLinkedList] = None, next_node: Optional['Node'] = None):
#         self.data = data
#         self.next_node = next_node

# class LinkedList(Generic[TemplateLinkedList]):

#     first_node: Optional[Node] = None
#     last_node: Optional[Node] = None

#     def create_node(self, data: TemplateLinkedList, position: Optional[int] = -1):
#         new_node = Node[TemplateLinkedList](data=data)

#         if LinkedList.first_node == None:
#             LinkedList.first_node = new_node
#             LinkedList.last_node = new_node

#         elif position == 0: # Vị trí đầu tiên
#             new_node.next_node = LinkedList.first_node
#             LinkedList.first_node = new_node # di chuyển quản lí ô nhớ đầu tiền về new_node ô nhớ mới
        
#         elif position == self.count() - 1 or position == -1: # thêm vào cuối
#             LinkedList.last_node.next_node = new_node
#             LinkedList.last_node = new_node
        
#         else:
#             temp_node = LinkedList.first_node
#             while position - 1 > 0:
#                 temp_node=temp_node.next_node
            
#             after_node = temp_node.next_node
#             before_node = temp_node

#             new_node.next_node = after_node
#             before_node.next_node = new_node


#     def delete(self, postion: int):
#         if postion == 0:
#             temp_node = LinkedList.first_node
#             LinkedList.first_node = LinkedList.first_node.next_node # dịch chuyển vị trí quản lí ô nhớ first về ô nhớ đứng sau
#             temp_node.next_node = None # Xóa ô nhớ đầu tiên đi temp_node = first

#         elif postion == self.count() - 1 or postion == -1:
#             temp_node = LinkedList.first_node
            
#             while temp_node.next_node.next_node != None:
#                 temp_node = temp_node.next_node

#             LinkedList.last_node = temp_node
#             temp_node.next_node = None

#         else:
#             temp_node = LinkedList.first_node
#             while postion - 1 > 0:
#                 postion -= 1
#                 temp_node = temp_node.next_node
            
#             temp_node.next_node = temp_node.next_node.next_node

    
#     def count(self):
#         temp_node = LinkedList.first_node
#         dem = 0
#         while temp_node != None:
#             dem += 1
#             temp_node = temp_node.next_node
        
#         return dem

#     def print_all_nodes(self):
#         temp_node = LinkedList.first_node

#         while temp_node != None:
#             print(temp_node.data)
#             temp_node = temp_node.next_node


# linked_list = LinkedList[int]()
# linked_list.create_node(data=100)
# linked_list.create_node(data=200)
# linked_list.create_node(data=300)

# # linked_list.create_node(data=1000, position=1)
# linked_list.delete(postion=0)
# linked_list.print_all_nodes()

from typing import Generic, TypeVar, Optional

TemplateDoubleLinkedList = TypeVar('TemplateDoubleLinkedList')

class Node(Generic[TemplateDoubleLinkedList]):

    def __init__(self, data: Optional[TemplateDoubleLinkedList] = None, before_node: Optional['Node'] = None, after_node: Optional['Node'] = None):
        self.data = data
        self.before_node = before_node
        self.after_node = after_node



class DoubleLinkedList(Generic[TemplateDoubleLinkedList]):
    first_node: Optional['Node'] = None
    last_node: Optional['Node'] = None

    def create_node(self, data: TemplateDoubleLinkedList, position: Optional[int] = 0):
        new_node = Node[TemplateDoubleLinkedList](data=data)

        if DoubleLinkedList.first_node == None:
            DoubleLinkedList.first_node = new_node
            DoubleLinkedList.last_node = new_node
        
        elif position == 0:
            new_node.after_node = DoubleLinkedList.first_node
            DoubleLinkedList.first_node.before_node = new_node
            DoubleLinkedList.first_node = new_node


    def print_all_nodes(self):
        temp_node = DoubleLinkedList.first_node

        while temp_node != None:
            print(temp_node.data)
            temp_node=temp_node.after_node


double_linked_list = DoubleLinkedList[int]()
double_linked_list.create_node(data=100)
double_linked_list.create_node(data=200)
double_linked_list.create_node(data=300)

double_linked_list.print_all_nodes()
