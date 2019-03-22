# AFC_east = ['New England Patriots', 'Buffalo Bills', 'Miami Dolphins', 'New York Jets']
# print(len(AFC_east))
# str_team='New England Patriots'
# print(len(str_team)) #=20
# print(str_team[0]) #=N
# print(AFC_east[0]) #=New England Patriots
# print('Miami Dolphins' in AFC_east) #=true
# print(AFC_east[2][6:]) #=Dolphins
# for team in AFC_east:
#     print(team)
# AFC_west = ['Chargers', 'Raiders', 'Broncos', 'Chiefs']
# AFC = AFC_east + AFC_west
# print(AFC)
# print(AFC_east[1:3]) #=Buffafo Bills, Miami Dolphins
# print(AFC[1::2]) #=Buffafo Bills, New York Jets, Raiders, Chiefs
# del AFC[-2] #deletes Broncos
# print(AFC)
# print(AFC_east)
# AFC_east[-1] = 'New York Giants' #changes New York Jets to New York Giants
# print(AFC_east)
#
# L = [
#     ['Apple', 'Google', 'Microsoft'], #item 1
#     ['Java', 'Python', ['Ruby','On Rail'], 'PHP'], #item2
#     ['Adam', 'Bart', 'Lisa']] #item 3

# print(len(L)) #=3
# print(L[0]) #=Apple, Google, Microsoft
# print(len(L[0])) #=3
# print(len(L[1])) #=4
# print(L[0][0])#=Apple
# print(L[1][2][0])#=Ruby

# name='Maddison'
# t = list(name)
# print(t)

str_team = 'New England Patriots'
t = str_team.split() #convert string into separate words
print(t)
#
# team_name = " ".join(t) #convert words back into string
# print(team_name)

#Dictionary
names = ['Bailey', 'Maddison', 'Aob']
scores = [60,90,100]
#
grades = dict()
# grades = {} #tells Python creating a new dictionary
# grades['Bailey'] = 60
# grades['Maddison'] = 90
# grades['Aob'] = 100
# print(grades)
# print(grades['Maddison'])

# grades['Aida'] = [99,98]
# print(grades)
#
# print('Penny' in grades) #not in key of dictionary so returns false
# print(len(grades)) #=4
#
# for name in grades.keys():
#     print(name)
# for score in grades.values():
#     print(score)
# for item in grades.items(): #gives you what is separated by comma
#     print(item)




