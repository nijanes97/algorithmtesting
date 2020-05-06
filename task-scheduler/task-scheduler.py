class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tempset = set(tasks)
        max_count = 0
        max_cmd = ''
        if n == 0:
            return len(tasks)
        while len(tempset) > 0:
            cmd = tempset.pop()
            temp = list(filter(lambda a: a != cmd, tasks))
            if len(tasks) - len(temp) > max_count:
                max_count = len(tasks) - len(temp)
                max_cmd = cmd
        
        
        
        return (max_count + (max_count -1 ) * n) + (len(list(filter(lambda a: a != max_cmd, tasks))) - (max_count - 1))
