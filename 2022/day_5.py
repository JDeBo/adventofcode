from day_5_input import input

stacks, moves = tuple(input.strip('\n').split('\n\n'))
print(stacks)
print(moves.split('\n')[:2])

n = 4
awful = [stacks[i:i+n] for i in range(0, len(stacks), n)]
n2 = 9
terrible = [[] for x in range(n2)]

for idx, x in enumerate(awful):
    i = idx % n2
    terrible[i].append(x)

less_terrible = [list(filter(None, [x.strip('\n').strip().strip('[]') for x in y])) for y in terrible]

filter_boi = lambda x : x not in ["move", "from", "to"]
ug_af = [list(filter(filter_boi, x.split())) for x in moves.split('\n')]

def move_items(num_to_move, stack1, stack2):
    num_to_move, stack1, stack2 = tuple([int(x) for x in [num_to_move, stack1, stack2]])
    idx1 = stack1 - 1
    idx2 = stack2 - 1
    movers = less_terrible[idx1][:num_to_move]
    # movers.reverse() # uncomment for part 1 since the boxes get flipped as they're moved
    less_terrible[idx2] = movers + less_terrible[idx2]
    less_terrible[idx1] = less_terrible[idx1][num_to_move:]

[move_items(x[0], x[1], x[2]) for x in ug_af]
solution = ''.join([x[0] for x in less_terrible])
print(less_terrible)
print(solution)