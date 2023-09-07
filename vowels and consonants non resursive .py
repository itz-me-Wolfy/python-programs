def count_vowels_and_consonants(input_string):
    vowels = "AEIOUaeiou"
    num_vowels = 0
    num_consonants = 0

    for char in input_string:
        if char.isalpha():
            if char in vowels:
                num_vowels += 1
            else:
                num_consonants += 1

    return num_vowels, num_consonants

 
input_str = input("Enter a string: ")

vowels, consonants = count_vowels_and_consonants(input_str)

print("Number of vowels:", vowels)
print("Number of consonants:", consonants)
