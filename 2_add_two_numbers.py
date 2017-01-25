# Written by James Andreou
# leetcode.com #2 Add Two Numbers

#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# While this may not be the most optimal, I am doing this to learn python functions!
def addTwoNumbers(l1, l2):
  # Extract into list.
  list1, list2 = [], []
  while l1 is not None:
    list1.append(l1.val)
    l1 = l1.next
  while l2 is not None:
    list2.append(l2.val)
    l2 = l2.next
  # Convert to integers.
  list1.reverse()
  list2.reverse()
  n1 = int(''.join(map(str, list1)))
  n2 = int(''.join(map(str, list2)))
  n3 = n1 + n2
  # Create new linked list
  list3 = map(int, list(str(n3)))
  list3.reverse()
  l3 = ListNode(list3[0])
  tail = l3
  for num in list3[1:]:
    tail.next = ListNode(num)
    tail = tail.next
  return l3
        
l1 = ListNode(4)
l1.next = ListNode(3)
l1.next.next = ListNode(6)

l2 = ListNode(6)
l2.next = ListNode(1)
l2.next.next = ListNode(4)

# 634 + 416 = 1050
print addTwoNumbers(l1, l2)