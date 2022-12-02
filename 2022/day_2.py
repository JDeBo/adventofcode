from day_2_inputs import input

their_values = {
    'A' : 1,
    'B' : 2,
    'C' : 3,
}

win = 6
draw = 3
lose = 0

my_values = {
    'X' : 0,
    'Y' : 3,
    'Z' : 6,
}

def score_match(them: str, me: str):
    theirs = their_values[them]
    mine = my_values[me]
    if mine == 0: # Case when lose
        if theirs == 1:
            return 3
        else: 
            return theirs - 1
    elif mine == 3: # Case when draw
        return theirs + mine
    else: # Case when win
        if theirs == 3:
            return 1 + mine
        return theirs + 1 + mine



def solution(input: str):
    base = input.split('\n')
    pairs = [x.split(' ') for x in base[1:-1]]
    results = [score_match(x[0], x[1]) for x in pairs]
    print(f'My score is {sum(results)}')
    # print(pairs[:10], results)

solution(input)
