class Solution:
    def average(self, salaries: List[int]) -> float:
        maxSalary = float('-inf')
        minSalary = float('inf')
        answer = 0
        count = len(salaries) - 2
        
        for i, salary in enumerate(salaries):
            if salary > maxSalary:
                maxSalary = salary
            if salary < minSalary:
                minSalary = salary
            answer += salary
        return (answer - minSalary - maxSalary) / count
        
