# Build a function that counts the vowels in a word

def countVowels(word):
    count = 0

    for ch in word:
        if ch in "aeiouAEIOU":
            count = count + 1

    print(count)


word = input("Enter a word: ")
countVowels(word)