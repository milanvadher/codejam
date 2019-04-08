userInput = input()

def convert(list):   
    res = sum(d * 10**i for i, d in enumerate(list[::-1])) 
    return(res) 

def calculateAns(index):
    _input = input()
    ansArray = []
    ansArray2 = []

    ansArray = [int(x) for x in str(_input)]
    ansArray2 = ansArray[:]

    for i in range(0,len(ansArray)):
        if (ansArray[i] == 4):
            ansArray[i] = 3
            ansArray2[i] = 1
        else:
            ansArray2[i] = 0

    print("Case #"+str(index+1)+":", convert(ansArray), convert(ansArray2))

for i in range(0,int(userInput)):
    calculateAns(i)
