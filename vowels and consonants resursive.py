def count_vowels_consonants(string):
  
    if len(string) == 0:
        return 0, 0
 
    first_char = string[0].lower()

 
    if first_char in "aeiou":
   
        vowels, consonants = count_vowels_consonants(string[1:])
        return vowels + 1, consonants
    elif first_char.isalpha():
          vowels, consonants = count_vowels_consonants(string[1:])
          return vowels, consonants + 1
    else:
          return count_vowels_consonants(string[1:])
 
input_string = input("Enter a string: ")
 
vowel_count, consonant_count = count_vowels_consonants(input_string)
 
print("Vowels:", vowel_count)
print("Consonants:", consonant_count)
