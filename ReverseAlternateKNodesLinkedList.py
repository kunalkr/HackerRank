class Node:
  def __init__(self, val):
    self.val = val
    self.next = None


class LinkedList:
  def __init__(self, head):
    "Constructor to initialize the list"
    self.head = head
    self.last = head


  def append(self, data):
    node = Node(data)
    if not self.head:
      self.head = node
    if self.last:
      self.last.next = node
    self.last = node


  def print_list(self):
    "Prints contents of entire list"
    node = self.head

    while(node):
      print(node.val, end=' ')
      node = node.next
    print("")


def reverse_alternate_k_nodes(linked_list, k, b_reverse):
  head_node = linked_list.head
  curr_node = head_node
  prev_node = None
  next_node = None

  while curr_node:
    counter = 0
    start_node = curr_node
    end_node = prev_node
    while(counter < k and curr_node != None):
      next_node = curr_node.next
      if b_reverse:
        curr_node.next = prev_node
      prev_node = curr_node
      curr_node = next_node
      counter += 1

    if b_reverse:
      start_node.next = next_node

      # handle base case
      if start_node == head_node:
        linked_list.head = prev_node
      else:
        end_node.next = prev_node
  
    # toggle the reverse switch
    b_reverse = not b_reverse

  return linked_list


def main():
  # initialize the linked list
  node = Node(1)
  my_list = LinkedList(node)
  for val in range(2,21):
    my_list.append(val)
  my_list.print_list()
  reverse_alternate_k_nodes(my_list, 3, True)
  my_list.print_list()

main()
