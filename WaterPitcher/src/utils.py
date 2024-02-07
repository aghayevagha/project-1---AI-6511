def heuristic( target, current):
        return abs(target - current)

def check_target(target, current):
    return current == target


def print_path(path):
    for p in path:
        print( 'pitcers:' , p.pitchers,' current : ', p.current, ' heuristic ', p.h)

'''def testing(c, t):
    capacities=c
    target=t
    initial_state = PitcherState([0] * (len(capacities) + 1), None, 0, target)
    steps = a_star_search(initial_state)
    return steps
'''

def read_input_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        capacities = list(map(int, lines[0].strip().split(',')))
        target = int(lines[1].strip())
    return capacities, target