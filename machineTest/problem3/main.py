
import functools

def getLongestWords(words_file, n=2):
    # Open the words file and read the words into a list
    with open(words_file, 'r') as f:
        words = [word.strip() for word in f.readlines()]

    # A list to store the longest n words
    getLongestWords = []
    # A counter to keep track of the number of words composed of other words
    composed_words = 0
    # funtion to check if workd is Composed
    @functools.lru_cache() # this decorator will avoid redundant computation for the same inputs.
    def isComposed(word):
        for i in range(1,len(word)):
            # print(word[:i] in words,word[:i])
            if word[:i] in words and word[i:] in words:
                return True
            if word[:i] in words:
                if isComposed(word[i:]):return True
        return False
    for word in words:
        if isComposed(word):composed_words+=1

    # Sort the words list in descending order of length and store the first n words in the getLongestWords list
    words.sort(key=lambda x: len(x), reverse=True)
    for word in words[:n]:
        getLongestWords.append(word)

    # Return the getLongestWords list and the composed_words count
    return getLongestWords, composed_words


# test the funtion

if __name__=="__main__":
    filepath = "tmp/words.txt" # make sure to add right path
    n = int(input("Please specify the number of longest words to output (default 2): ") or 2)
    longestWord, composedWords = getLongestWords(filepath,n)

    print(f"Longest {len(longestWord)} words:")
    
    for word in longestWord:print(word)

    print(f"Number of words comprised of other words: \n{composedWords}")
