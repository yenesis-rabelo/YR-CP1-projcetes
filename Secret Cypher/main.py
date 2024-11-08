#Yenesis Rabelo Secret Cypher Assignment 

def shift_cipher(text, shift):
    result = []  # to store the shifted characters
    
    # looping through each character
    for char in text:
        if char.isalpha():  # checking if the character is an alphabet letter

            # determining the start 
            start = ord('a') if char.islower() else ord('A')
            
            # shifting the character
            shifted_char = chr(start + (ord(char) - start + shift) % 26)
            result.append(shifted_char)
        else:
            # non-alphabetical characters stay the same
            result.append(char)
    
    # joining them into one
    return ''.join(result)

# an example of usage:
if __name__ == "__main__":

    text = input("Enter a string to encode: ")
    shift = int(input("Enter a shift value: "))
    
    secret_code = shift_cipher(text, shift)
    print("Secret Code:", secret_code)
