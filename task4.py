##vowels

def count_vowels(string):
    string = string.lower()
    total_vowels = 0
    vowel_counts = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    
    for char in string:
        if char in 'aeiou':
            total_vowels += 1
            vowel_counts[char] += 1
    
    return total_vowels, vowel_counts

# Given string
given_string = "Guvi Geeks Network Privated Limited"

# Calculate total vowels and individual counts
total_vowels, individual_counts = count_vowels(given_string)

print("Total vowels:", total_vowels)
print("Count of each individual vowel:")
for vowel, count in individual_counts.items():
    print(f"{vowel}: {count}")



#pyramid
max_num = 20
num_rows = int((2 * max_num - 1) ** 0.5)
current_num = 1
for i in range(1, num_rows + 1):
    print(" " * (num_rows - i), end="")
   
    for j in range(1, i * 2):
        if current_num > max_num:
            break
        print(current_num, end=" ")
        current_num += 1
    
    print()



#remove the vowels from string 

def remove_vowels(input_string):
    vowels = "aeiou"
    return "".join(char for char in input_string if char not in vowels)

input_str = "hi this ajith kumar from guvi"
result = remove_vowels(input_str)
print("String with vowels removed:", result)


#function in unique characters

def count_unique_characters(input_string):
    unique_chars = set(input_string)
    
    return len(unique_chars)

example_string = "ajith,kumar !"
unique_count = count_unique_characters(example_string)
print("Number of unique characters:", unique_count)

#function takes string and returns true r false
 
def is_palindrome(s):
    s = s.replace(" ", "").lower() 
    return s == s[::-1]

input_string = ("appa")
result = is_palindrome(input_string)

if result:
    print(f'"{input_string}" is a palindrome.')
else:
    print(f'"{input_string}" is not a palindrome.')

    

#longest common substrings

def longest_common_substring(str1, str2):
    
    long1 = len(str1)
    long2 = len(str2)
    longest_length = 0
    end_index = 0
    
    table = [[0] * (long2 + 1) for _ in range(long1 + 1)]
    
    for i in range(long1 + 1):
        for j in range(long2 + 1):
            if i == 0 or j == 0:
                table[i][j] = 0
            elif str1[i - 1] == str2[j - 1]:
                table[i][j] = table[i - 1][j - 1] + 1
                if table[i][j] > longest_length:
                    longest_length = table[i][j]
                    end_index = i - 1
            else:
                table[i][j] = 0
    
    
    longest_substring = str1[end_index - longest_length + 1: end_index + 1]
    return longest_substring

string1 = "12345"
string2 = "123456789"
result = longest_common_substring(string1, string2)

print(f"The longest common substring is: '{result}'")



#most frequent character

def most_frequent_character(input_string):
   
    char_unique = {}

    for char in input_string:
        if char.isalpha():  
            char = char.lower()  
            char_unique[char] = char_unique.get(char, 0) + 1

    most_frequent_char = max(char_unique, key=char_unique.get)

    return most_frequent_char

input_str = "Ajee_popZ!"
result = most_frequent_character(input_str)

print(f"The most frequent character is: '{result}'")



#anagram

def are_anagram(str1, str2):
    str1 = str1.replace(" ", "")
    str2 = str2.replace(" ", "")

    return sorted(str1) == sorted(str2)

string1 = "heart"
string2 = "earth"
result = are_anagram(string1, string2)

if result:
    print(f'"{string1}" and "{string2}" are anagram')
else:
    print(f'"{string1}" and "{string2}" are not anagram')

    

#number of words in it

def count_words(input_string):
    words = input_string.split()

    return len(words)

input_str = 'this is ajith kumar'
result = count_words(input_str)

print(f'The number of words in the string is: {result}')