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


def reverse_list(linked_list):
  rev_list = linked_list

  curr_node = rev_list.head
  prev_node = None
  next_node = None

  while(curr_node):
    next_node = curr_node.next
    curr_node.next = prev_node

    prev_node = curr_node
    curr_node = next_node
  rev_list.head = prev_node

  return rev_list


def main():
  # initialize the linked list
  node = Node(1)
  my_list = LinkedList(node)
  rev_list = reverse_list(my_list)
  rev_list.print_list()
  my_list.head.next = Node(2)
  rev_list = reverse_list(my_list)
  rev_list.print_list()
  my_list.head.next.next = Node(3)
  my_list.print_list()

  rev_list = reverse_list(my_list)
  rev_list.print_list()

main()

