#even numbers and odd numbers

list = [10, 501, 22, 37, 100, 999, 87, 351]

even_numbers = []
odd_numbers = []

for num in list:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)

print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)

#prime number

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

given_list = [10, 501, 22, 37, 100, 999, 87, 351]

prime_numbers = [num for num in given_list if is_prime(num)]
count_prime = len(prime_numbers)

print("Count of prime numbers:", count_prime)
print("Prime numbers:", prime_numbers)


#happy number

def is_happy_number(n):
    visited = set()
    while n != 1 and n not in visited:
        visited.add(n)
        n = sum(int(digit) ** 2 for digit in str(n))
    return n == 1

given_list = [10, 501, 22, 37, 100, 999, 87, 351]

happy_numbers = [num for num in given_list if is_happy_number(num)]
count_happy_numbers = len(happy_numbers)

print("Count of happy numbers:", count_happy_numbers)
print("Happy numbers:", happy_numbers)


# first and last digit of integer

def sum_first_last_digit(number):
    
    number = abs(number)
    last_digit = number % 10
    
    num_digits = len(str(number))
    
    first_digit = number // (10 ** (num_digits - 1))
    
    digit_sum = first_digit + last_digit
    
    return digit_sum

integer = 54879
result = sum_first_last_digit(integer)

print(f"The sum of the first and last digit of {integer} is: {result}")


#minimum and maximum of students

def distribute_mangoes(mangoes, students):
    mangoes.sort()  
    min_difference = float('inf')  
    num_bags = len(mangoes)
    
    if num_bags < students:
        return -1
    
    for i in range(num_bags - students + 1):
        min_difference = min(min_difference, mangoes[i + students - 1] - mangoes[i])
    
    return min_difference


bags = [7, 3, 2, 4, 1,9, 12, 56]
num_students = 3

result = distribute_mangoes(bags, num_students)
print(f"The minimum difference in mangoes distributed is: {result}")

#dupilcates lists

def find_duplicates(list1, list2, list3):
    
    combined_list = list1 + list2 + list3
    element_count = {}
    duplicates = []

    for element in combined_list:
        if element in element_count:
            element_count[element] += 1
        else:
            element_count[element] = 1
    
    for element, count in element_count.items():
        if count > 1:
            duplicates.append(element)

    return duplicates

list1 = [1, 2, 3, 4, 5, 6]
list2 = [2, 3, 4, 7, 8]
list3 = [3, 4, 5, 9, 10]

result = find_duplicates(list1, list2, list3)
print("Duplicates:", result)


#non-repeating elements

def non_repeating_element(nums):
    count_dict = {}
    
    for num in nums:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    for num in nums:
        if count_dict[num] == 1:
            return num
    return None 

numbers = [4, 6, 2, 4, 3, 2, 1, 5, 5]
result = non_repeating_element(numbers)

if result is not None:
    print(f"The first non-repeating element is: {result}")



#minimum elements in a rated and sorted lists

def find_minimum_element(sorted_list):
    if not sorted_list:
        return None  
    return sorted_list[0]  

ratings = [1, 2, 3, 4, 5]
minimum_rating = find_minimum_element(ratings)

if minimum_rating is not None:
    print(f"The minimum rated element is: {minimum_rating}")
else:
    print("no minimum rated elements")


#sort the list value with 59

def triplet_with_sum(nums, target_sum):
    n = len(nums)

    
    nums.sort()
    for i in range(n - 2):
        left = i + 1
        right = n - 1

        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]

            if current_sum == target_sum:
                return [nums[i], nums[left], nums[right]]
            elif current_sum < target_sum:
                left += 1
            else:
                right -= 1

    return None
given_list = [10, 20, 30, 9]
target_value = 59

triplet = triplet_with_sum(given_list, target_value)

if triplet:
    print(f"The triplet with sum {target_value} is: {triplet}")
else: 
    print("No triplet found with the given sum.")




#sum of equal to zero

def zero(nums):
    prefix_sums = set()
    current_sum = 0

    for num in nums:
        current_sum += num
        if current_sum in prefix_sums or current_sum == 0:
            return True

        prefix_sums.add(current_sum)

    return False
given_list = [4, 2, 3, 1, 6,]
result = zero(given_list)

if result:
    print("There is a sublist with a sum equal to zero.")
else:
    print("No sublist with a sum equal to zero.")
