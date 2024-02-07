from queue import PriorityQueue
from utils import heuristic, check_target, print_path, read_input_file
from state import StateClass

SHOW_PATH = True


def create_states(c_state):
    states = []

    # put water into empty pitchers
    for i in range(len(c_state.pitchers)):
        # Fill jug i
        temp = c_state.pitchers.copy()
        if temp[i] == 0:
            temp[i] = capacities[i]
            states.append(StateClass(temp, c_state.current, c_state, 1, heuristic(target,c_state.current)))

    # empty pitcher into the infinite virtual pitcher
    for i in range(len(c_state.pitchers)):

        temp = c_state.pitchers.copy()
        new_water=c_state.current
        if temp[i] != 0 and new_water+ temp[i] <= target*10:
            new_water += temp[i]
            temp[i] = 0
            states.append(StateClass(temp, new_water, c_state, 1, heuristic(target,new_water)))

    # remove the water from pitchers to outside
    for x in range(len(c_state.pitchers)):
        temp = c_state.pitchers.copy()
        if temp[x] != 0:
        
            temp[x] = 0
            states.append(StateClass(temp, c_state.current, c_state, 1, heuristic(target,c_state.current)))

    #  move water from full one potcher to empty another pitcher
    for y in range(len(c_state.pitchers) -1, -1, -1):
        temp = c_state.pitchers.copy()
        if temp[y] == capacities[y]:
            for x in range(y):
                if temp[x] == 0:
                    temp[x] = capacities[x]
                    temp[y] -= capacities[x]
                    states.append(StateClass(temp, c_state.current, c_state, 1, heuristic(target,c_state.current)))
                    break
    return states

def a_star(initial_state):
    queue = PriorityQueue()
    queue.put((0, initial_state))
    cost_map = {initial_state: 0}

    while not queue.empty():
        _, cs = queue.get()
        if check_target(target,cs.current):
            # Reconstruct path
            print('Possible!')
            path = []
            total = cs.g
            while cs != initial_state:
                path.append(cs)
                cs = cs.parent
                # current_state = came_from[current_state]
                total += cs.g
            path.append(initial_state)
            path.reverse()
            if SHOW_PATH:
                print('Path:')
                print_path(path)
            return total
        
        for next_state in create_states(cs):
            new_cost = cost_map[cs] + next_state.f
            if next_state not in cost_map or new_cost < cost_map[next_state]:
                cost_map[next_state] = new_cost
                queue.put((new_cost, next_state))

    print("Impossible!")
    return -1

def testing(c, t):
    global capacities
    global target
    capacities=c
    target=t
    initial_state = StateClass([0] * (len(capacities)), 0, None, 0, target)
    steps = a_star(initial_state)
    print(steps)
    return steps

def main():
    path = 'inputs/input1.txt'  
    global capacities
    global target
    capacities, target = read_input_file(path)

    # Sort capacities to ensure the order
    capacities = sorted(capacities)

    print('Pitchers:' ,capacities)
    print('Goal:',target)
    initial_state = StateClass([0] * (len(capacities)), 0, None, 0, target)
    steps = a_star(initial_state)
    print(steps)
    return steps


if __name__ == "__main__":
    main()