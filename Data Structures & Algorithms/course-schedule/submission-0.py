from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}
        for crs, prereq in prerequisites:
            preMap[crs].append(prereq)
        
        visiting = set()
        def dfs(course):
            
            if course in visiting:
                return False

            if preMap[course] == []: # checking for prereqs
                return True
            
            visiting.add(course)
            for p in preMap[course]:
                if not dfs(p):
                    return False

            visiting.remove(course) 
            preMap[course] = []
            return True
            
        for course in range(numCourses):
            if not dfs(course): 
                return False
        return True
        


            
