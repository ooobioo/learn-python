from collections import deque

def round_robin(tasks, time_slice):
    """
    Simulate round robin scheduling.
    :param tasks: List of tuples (task_name, burst_time)
    :param time_slice: Time slice for each round
    :return: List of (task_name, start_time, end_time)
    """

    queue = deque([(name, burst) for name, burst in tasks])
    timeline = []
    current_time = 0

    while queue:
        name, burst = queue.popleft()
        run_time = min(burst, time_slice)
        start_time = current_time
        end_time = current_time + run_time
        timeline.append((name, start_time, end_time))
        current_time = end_time
        if burst > time_slice:
            queue.append((name, burst - time_slice))
    return timeline

# Example usage
if __name__ == "__main__":
    tasks = [("A", 5), ("B", 3), ("C", 7)]
    time_slice = 2
    schedule = round_robin(tasks, time_slice)
    for entry in schedule:
        print(f"Task {entry[0]}: {entry[1]} -> {entry[2]}")