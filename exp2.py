# x = input("Enter the string ")
# y = x[::-1]
# if x==y:
#     print("The string is Palindrome")
# else:
#     print("The string is not Palindrome")
''''''''''''''''''''''''''''''''''''''
# x= "holiday is very good"
# y= "Monday is holiday"
# t=x.split()
# u=y.split()
# def is_symmetrical(string):
#      return string == string[::-1]
# def is_palindrome(string):
#      return is_symmetrical(string)
# input_string = input("Enter a string: ")
# if is_palindrome(input_string):
#     print(input_string," is a palindrome.") 
# else:
#     print(input_string,"is not a palindrome.") 
# if is_symmetrical(input_string):
#     print(input_string,"is symmetrical.") 
# else:
#     print(input_string, "is not symmetrical.")
''''''''''''''''''''''''''''''''''''''''''''''''''

# def find_uncommon_words(str1, str2): 
#     set1 = set(str1.split())
#     set2 = set(str2.split())
#     x = set1.symmetric_difference(set2) 
#     return x
# str1 = input("Enter the first string: ") 
# str2 = input("Enter the second string: ")
# uncommon_words = find_uncommon_words(str1, str2)
# print("The uncommon words are:",uncommon_words)
# ''''''''''''''''''''''''''''''''''''''''''

# def add_str(string): 
#     if len(string) < 3:
#          return string
#     elif string[-3:] == 'ing':
#          return string + 'ly'
#     else:
#         return string + 'ing'

# string = input("Enter a string: ") 
# result = add_str(string)
# print("The result is:",result)

# x= input()
# print(x[len(x):1+len(x)])


# x= input("enter your name")
# y=len(x)
# if y%4==0:
#     print(x[::-1])
# else :
#     print("Exiting")
#x=input()
#y=x[::-1]
#print(y)
# f=open("text.txt","r")
# print(f.read())