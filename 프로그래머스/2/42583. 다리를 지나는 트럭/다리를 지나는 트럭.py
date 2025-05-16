from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque([0] * bridge_length)
    tweights = deque(truck_weights)
    totalw = 0
    time = 0

    while bridge:
        time += 1
        
        out = bridge.popleft()
        totalw -= out

        if tweights:
            if totalw + tweights[0] <= weight:
                new = tweights.popleft()
                bridge.append(new)
                totalw += new
            else:
                bridge.append(0)
    return time
