from day_4_inputs import input
from utils import begin

starting_list = begin(input)

separate = lambda x : [y.split('-') for y in x.split(',')]
range_out = lambda x : list(range(int(x[0]), int(x[1]) + 1))
test = lambda x : all(section in x[1] for section in x[0])
test2 = lambda x : any(section in x[1] for section in x[0])

y = list(map(separate, starting_list))
z = [[range_out(a) for a in b] for b in y]
[a.sort(key = len) for a in z]
solution = list(map(test, z))
solution2 = list(map(test2, z))

print(solution.count(True))
print(solution2.count(True))
