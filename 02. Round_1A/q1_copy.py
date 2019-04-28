def main():
    t = int(input())
    for _ in range(t,t+1):
        n = int(input())
        input_words = []
        getInput(input_words, n)

def getInput(input_words, n):
    for _ in range(n):
        input_words.append(input())
    print(input_words)

if __name__ == "__main__":
    main()