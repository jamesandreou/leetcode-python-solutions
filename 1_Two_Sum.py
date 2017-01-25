# Written by James Andreou
# leetcode.com #1 Two Sum

def twoSum(nums, target):
  # Solve for a + b = target
  # target - a = b
  seen = {}
  for i, a in enumerate(nums):
    b = target - a
    if seen.has_key(b):
      return [seen[b], i]
    else:
      seen[a] = i
  return []

print twoSum([3,4,7,3,1], 6)
print twoSum([1, 1, 3, 4, 6, 2], 3)