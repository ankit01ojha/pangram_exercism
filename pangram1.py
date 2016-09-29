myPhrase = raw_input("Enter the string")

def is_pangram(phrase):
    c = 0
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    phraseLetters = ""
    for char in phrase:
        for letter in alphabet:
            if char == letter and char not in phraseLetters:
                phraseLetters += char
    for char in phraseLetters:
        for letter in alphabet:
            if char == letter:
                c += 1
    if c == 26:
        print("its a pangram")
        return True
        
    else:
        
        print("not a pangram")

print is_pangram(myPhrase)
