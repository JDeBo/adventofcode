from day_1_inputs import input1

def calc_groups(input_list: str):
    splits = input_list.split('\n\n')
    dub_splits = [x.split('\n') for x in splits]
    dub_splits[0] = dub_splits[0][1:]
    int_splits = [[int(a) for a in x] for x in dub_splits]
    sum_splits = [sum(x) for x in int_splits]
    sum_splits.sort(reverse=True)
    print(sum_splits[0])
    print(sum(sum_splits[:3]))

calc_groups(input1)
# print(input1)