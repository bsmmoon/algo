# Constraints:
# k == lists.length
# 0 <= k <= 10^4
# 0 <= lists[i].length <= 500
# -10^4 <= lists[i][j] <= 10^4
# lists[i] is sorted in ascending order.
# The sum of lists[i].length won't exceed 10^4.

# BCR: O(sum of lists[i].length) = O(K)
# or if we say sum of lists[i].length = N, O(N)
# 
# Approach 1
# Insert the rest of the lists to the first list
# O(N^2), space: O(N)
#
# Approach 2
# Find the smallest element of all lists O(K)
# Insert the element to a new list O(N)
# Do this until no elements are left O(N)
# O((K*N)*N) = O(KN^2), space: O(N)
# 
# Approach 3
# Find the smallest element of all lists O(K)
# Insert the element to a queue O(1)
# Do this until no elements are left O(N)
# Base on the queue, create a new list O(N)
# O((K+1)*N+N) = O(KN), space: O(N)
#
# Approach 4
# Dump everything into heap O(NlogN)
# Pop all and create a new list O(NlogN)
# O(NlogN), space: O(N)

import heapq

class Solution(object):
    def mergeKLists(self, lists):
        heap = []
        for list in lists:
            while list:
                heapq.heappush(heap, list.val)
                list = list.next
        
        if len(heap) == 0: return
    
        root = ListNode(heapq.heappop(heap))
        curr = root
        while len(heap) > 0:
            curr.next = ListNode(heapq.heappop(heap))
            curr = curr.next
        return root

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Test:
    def __init__(self, input, output):
        self.input = input
        self.output = output

def ll_to_arr(ll):
    if not ll: return []
    
    arr = []
    while ll:
        arr.append(ll.val)
        ll = ll.next
    return arr

def arr_to_ll(arr):
    if len(arr) == 0: return

    root = ListNode(arr[0])
    curr = root
    for e in arr[1:]:
        curr.next = ListNode(e)
        curr = curr.next
    return root

tests = [
    Test([
        arr_to_ll([1,4,5]),
        arr_to_ll([1,3,4]),
        arr_to_ll([2,6])
    ], arr_to_ll([1,1,2,3,4,4,5,6])),
    Test([], []),
    Test([arr_to_ll([])], []),
]

for test in tests:
    print(ll_to_arr(Solution().mergeKLists(test.input)), ll_to_arr(test.output))
    
    
