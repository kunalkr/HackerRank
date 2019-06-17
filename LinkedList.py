class Node:
  def __init__(self, val):
    self.val = val
    self.next = None


class LinkedList:
  def __init__(self, head):
    "Constructor to initialize the list"
    self.head = head


  def print_list(self):
    "Prints contents of entire list"
    node = self.head

    while(node):
      print(node.val, end=' ')
      node = node.next
    print("")


def main():
  # initialize the linked list
  node = Node(1)
  my_list = LinkedList(node)
  my_list.print_list()

  my_list.head.next = Node(2)
  my_list.print_list()

main()
