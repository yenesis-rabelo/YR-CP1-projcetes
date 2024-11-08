#Yenesis Rabelo Pig Latin Assignment


def pig_latin(word):
    # defining vowels
    vowels = "aeiouAEIOU"
    

    # if the word starts with a vowel
    if word[0] in vowels:
        return word + "way"
    

    # finding the index of the first vowel
    for i in range(len(word)):
        if word[i] in vowels:
        
            return word[i:] + word[:i] + "ay"
    

    # if the the word has no vowel you return the original word with "ay"
    return word + "ay"


# an example of usage:
if __name__ == "__main__":
    word = input("Enter a word to convert to Pig Latin: ")
    pig_latin_word = pig_latin(word)
    print("Pig Latin:", pig_latin_word)