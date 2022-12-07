import utils
from day_6_inputs import input, test_input_1, test_input_2, test_input_3

beg = input.strip('\n')
n = 14
def solver(stuff_here):
    listy_dude = list(enumerate(stuff_here))
    solution = []
    for x in listy_dude:
        start, value = x
        comps = [x[1] for x in listy_dude[start:start+n]]
        if len(set(comps)) == len(comps):
            solution.append(x)
            break
    print(solution[0][0]+n)


if __name__ == "__main__":
    solver(beg)