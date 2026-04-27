from collections import defaultdict
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_dependency = defaultdict(set)

        for course_deps in prerequisites:
            course = course_deps[0]
            dependency = course_deps[1]
            course_dependency[course].add(dependency)
        
        print(course_dependency)
        cleared_deps = set()

        def dfs(course_id, seen_items: set):
            if course_id in cleared_deps:
                return True
            if course_id in seen_items:
                return False
            
            seen_items.add(course_id)
            course = course_dependency[course_id]
            for dependency in course:
                is_possible = dfs(dependency, seen_items)
                if not is_possible:
                    return False
            
            cleared_deps.add(course_id)    
            return True
        
        for course_deps in prerequisites:
            course = course_deps[0]
            dependency = course_deps[1]
            is_possible = dfs(course, set())
            if not is_possible:
                return False
        
        return True