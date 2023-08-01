'''1 Write a program to print a string formed with the first 2 and the last 2 characters of the given string.
Assume the size of given string is always greater than or equal to 4.'''
s = "packages"
print(s [:2], s [-2:])

'''2  Write a program to check if aword is present in the given string.For example, if the word 'orange' is present in the "This is orange juice".'''
s = "This is orange juice"
n = "orange"
if n in s:
    print(f"{n} is present in s")
else:
    print(f"{n} is present in s")

'''3 Write a program that will print whether the number is a single digit number or double digit number or big number.
If given number is one digit number, print "Single digit number".'''
s = int(input("Enter the number:"))
if s < 10:
    print("The num is single digit")
elif s < 100:
    print("the number is double digit")
else:
    print("big number")

'''4 Write a program that takes a list and splits into smaller lists of given size. For example,
if lst = [1, 2, 3, 4, 5, 6], size = 2, it should return [[1, 2], [3,4], [5,6]] and
if lst = [1,2,3,4,5,6,7,8,9], size = 4 then it should return [[1,2,3,4],[5,6,7,8],[9]].'''
lst = [1,2,3,4,5,6,7,8,9]
print(lst [:2], lst [2 : 4], lst [4 : 6])
print(lst [:4], lst [4 : 8], lst [-1:])

'''5 Write a program to print a list with all duplicates in the given list.
#For example, if lst=[1, 3, 2, 1, 2, 5, 6] it should return [1, 2].'''

lst=[1, 3, 2, 1, 2, 5, 6]
dup = []
for i in set(lst):
    if lst.count(i) > 1:
        dup.append(i)
print(dup)

'''6 Write a program to find and group anagrams in a given list of words.
Two words are called anagrams if one word can be formed by rearranging letters of another.
For example 'eat', 'ate' and 'tea' are anagrams.
Assume the list given is ['eat', 'ate', 'done', 'tea', 'soup', 'node']
then it should return [['eat', 'ate', 'tea], ['done', 'node'], ['soup']]'''
s = ['eat', 'ate', 'done', 'tea', 'soup', 'node']
l = ([s [0], s [1], s [3]])
n = ([s [2], s[5]])
m = ([s [-2]])
print([l, n, m])


'''8  Write a program to display the elements of list thrice if it is a number and display the element terminated with ‘#’
# if it is not a number. For example, if the content of
# list is [‘41’, ‘DHRUVA’, ‘GURU’, ‘13’, ‘ZARA’]The output should be 414141 DHRUVA# GURU# 131313 ZARA#'''


my_list = ['41', 'DHRUVA', 'GURU', '13', 'ZARA']

output = ''
for item in my_list:
    if item.isdigit():
        output += item * 3

    else:
        output += item + '#'

print([output])
