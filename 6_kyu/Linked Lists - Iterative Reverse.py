https://www.codewars.com/kata/55e72695870aae78c4000026
class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None


def reverse(head):
    reverse = None
    temp = head
    while temp:
        reverse = push(reverse, temp.data)
        temp = temp.next
    if head:
        head.data = reverse.data
        head.next = reverse.next
