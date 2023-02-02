#Write a function to find if a given character is a vowel ( should return boolean value )


def is_Vowel(letter):
    if (letter == "A" or letter == "E" or letter == "I" or letter == "O" or letter == "U"):
        return True
    else:
        return False

letter = input("Enter the alphabet : ")
print(is_Vowel(letter.upper()))