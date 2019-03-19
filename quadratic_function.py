# team = 'New England Patriots'

# print(len(team))
# letter = team[1]
# print(letter)
# print(team[0])
#
# print(team[len(team)-1])
# print(team[-1])

# for letter in team:
#     print(letter)

prefixes = 'JKLMNOPQ'
suffix = 'ack'
for letter in prefixes:
    if letter == 'O' or letter == "Q": #you can also write this: if letter in 'OQ':
        print (letter + 'u' + suffix)
    else:
        print(letter + suffix)
#
# result = 0
# for number in range(1,1001):
#     if number%2 == 0: #this means number is an even #.
#         result = result + number
# print(result)
#
# result = 0
# for number in range(1,1001):
#     if number % 2 == 1: #this means number is an odd #.
#         result = result + number
# print(result)

# team = 'New England Patriots'
# print(team[0:11])
# print(team[:11])
# print(team[12:20])
# print(team[12:])
#
# print(team[::2])
# print(team[::3])
# print(team[::-1])
#
# a = 'level' #word is a palindrome. spelling backwards is same as spelling correct way
# print(a == a[::-1])
#
# name = 'anna'
# def is_palindrome(word):
#     return word == word[::-1]
# print(is_palindrome(name))
#
# word = 'New England Patriots'
# count = 0
# for letter in word:
#     if letter == 'e':
#         count = count + 1
# print(count)

word = 'New England Patriots'
count = 0
for letter in word:
    if letter in 'aeiouAEIOU':
        count = count + 1
print(count)
#
# name = 'Anna'
# new_name = name[:2] + name[-1]
# print(new_name)

team = 'New England Patriots'
new_team = ""
for letter in team:
    if letter != 'a':
        new_team = new_team + letter
print(new_team)
#
# print(team.upper())
# print(team.find('w'))