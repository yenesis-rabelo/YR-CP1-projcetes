#Yenesis Rabelo Palindrome




def check_palindrome(word):
    cleaned_word = ''.join(char.lower() for char in word if char.isalnum())

    if cleaned_word == cleaned_word[::-1]:
     print(f'"{word}" is a palindrome. ')
    else:
       print(f'"{word}" isn\'t a palindrome.')
       test_words = ["mom", "a", "dad", "crab" "bed", "word", "racecar", "step on no pets", "borrow or no", "yes!", "radar", "tom"]
       for word in test_words:
          check_palindrome(word)
