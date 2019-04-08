testCase = input()

def calc_ans(index):
    input()
    path_a = input()
    path_b = []
    for i in path_a:
        if (i == 'E'):
            path_b.append('S')
        else:
            path_b.append('E')

    print("Case #"+str(index+1)+":",''.join(path_b))

for i in range(int(testCase)):
    calc_ans(i)