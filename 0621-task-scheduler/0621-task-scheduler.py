from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Count the occurrences of each task
        task_counts = Counter(tasks)
      
        # Find the maximum frequency of any task
        max_freq = max(task_counts.values())
      
        # Count how many tasks have the maximum frequency
        max_freq_tasks_count = sum(freq == max_freq for freq in task_counts.values())
      
        # Calculate the number of idle states needed, which is defined by the formula:
        # (maximum frequency of any task - 1) * (n + 1) which gives the spaces between repetitions of the same task
        idle_time = (max_freq - 1) * (n + 1)
      
        # Add the count of most frequent tasks to idle time to get minimum length of the task schedule
        min_length = idle_time + max_freq_tasks_count
      
        # Return the maximum of the length of tasks (if no idle time is necessary) and calculated minimum length
        return max(len(tasks), min_length)