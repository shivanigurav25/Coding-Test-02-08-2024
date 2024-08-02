#Write a Python function to count the occurrences of a specific element in a list


def count_occurrences(lst, element):
    count = 0
    for item in lst:
        if item == element:
            count += 1
    return count

# Example usage
my_list = ["apple", "banana", "apple", "cherry", "apple"]
element = "apple"
print("The number of Apple count occurences is :" ,count_occurrences(my_list, element))


#Output
#The number of Apple count occurences is : 3




