input_words = []
indexesTaken = []
rhyme_patterns = []

def main():
    t = int(input())
    for i in range(1, t + 1):
        n = int(input())
        input_words = []
        indexesTaken = []
        rhyme_patterns = []
        for n in range(n):
            input_words.append(input())

        for index, word in enumerate(input_words):
            findMatch(index, word, input_words, indexesTaken)
        print("Case #{0}: {1}".format(i, len(indexesTaken)))


def findMatch(index, word, word_array, indexes_taken):
    maxIndex = 0
    maxMatch = 0
    matches = ''
    if (index in indexes_taken):
        return
    for i, other_word in enumerate(word_array):
        if (i in indexes_taken or i == index):
            continue
        len1 = len(word)
        len2 = len(other_word)
        tempMatches = ''
        match = 0
        for j in range(1, min(len1, len2) + 1):
            first_char = word[len1-j]
            second_char = other_word[len2-j]
            if (first_char == second_char):
                match = j
                tempMatches += first_char
            else:
                break
        if (match > maxMatch):
            maxIndex = i
            maxMatch = match
            matches = tempMatches
    if (maxMatch > 0 and matches not in rhyme_patterns):
        rhyme_patterns.append(matches)
        indexes_taken.extend([index, maxIndex])

if __name__ == "__main__":
    main()