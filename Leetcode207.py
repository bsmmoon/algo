# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def __repr__(self):
        output = []
        curr = self
        while curr:
            output.append(curr.val)
            curr = curr.next
        return str(output)

def makeLinkedList(arr):
    if not arr: return

    head = ListNode(arr.pop(0))
    curr = head
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return head

# Constraints:
# 1 <= numCourses <= 10^5
# 0 <= prerequisites.length <= 5000
# prerequisites[i].length == 2
# 0 <= ai, bi < numCourses
# All the pairs prerequisites[i] are unique.

# Observation
# Tis is a cycle detection problem
# A course without prerequisite can be taken freely

# Approach 1. DFS
# construct nodes with edges O(M), space O(N+M)
# duplicate indicates cycle
# once a course's dfs return True, memoise it!

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        if not prerequisites: return True
        
        courses = {}
        for course, prereq in prerequisites:
            if course not in courses: courses[course] = set()
            courses.get(course, set()).add(prereq)
            
        self.checked = set()
        for course in courses:
            if not self.dfs(courses, course, set()): return False
        return True
        
    def dfs(self, courses, course, visited):
        if course in visited: return False
        if course in self.checked: return True
        
        visited.add(course)
        for prereq in courses.get(course, ()):
            if not self.dfs(courses, prereq, visited): return False
        visited.remove(course)
        
        self.checked.add(course)
        return True
                
class Test:
    def __init__(self, input, output):
        self.input = input
        self.output = output

tests = [
    Test((2, [[1,0]]), True),
    Test((3, [[1,0]]), True),
    Test((2, [[1,0],[0,1]]), False),
    Test((3, [[1,0],[1,2],[0,1]]), False),
    Test((3, [[1,0],[2,1],[0,2]]), False),
    Test((1, []), True),
    Test((100, []), True),
    Test((20, [[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]]), False),
    Test((1, [[5,5]]), False)
]

solver = Solution()
for test in tests:
    output = solver.canFinish(*test.input)
    print("{} {}".format(output, test.output))
