# def square_plus_one(a,b):
#     result = a * b + 1
#     return result
#
# print(square_plus_one(2,3))

# def give_zhi_something(a,b):
#     return a + b

# import math
#
# def quadratic(a,b,c):
#      x_1 = (-b + math.sqrt(math.pow(b,2)-(4*a*c)))/2*a
#      x_2 = (-b - math.sqrt(math.pow(b,2)-(4*a*c)))/2*a
#      return x_1, x_2
#
# print(quadratic(1,2,-3))

#session3

#
# def calculate_bmi(weight,height):
#     bmi = 703*(weight/height**2)
#     if bmi >= 30:
#         return 'you are obese.'
#     else:
#         if bmi >= 25:
#             return 'you are overweight.'
#         else:
#             if bmi >= 18.5:
#                 return 'you have a normal weight.'
#             else:
#                 return 'you are underweight.'

# weight = input('Your weight is (in pounds):')
# height = input('Your height is (in inches):')
# weight = float(weight)
# height = float(height)
#
# print(calculate_bmi(weight,height))

#recursion example:

# def fab(n):
#     """"
#     Function will return nth Fabunacci number.
#     """
#     if n==1 or n==2:
#         return 1
#     else:
#         return fab(n-2) + fab(n-1)
#
#  print(fab(1))
#  print(fab(2))
#  print(fab(3))
#  print(fab(4))
#
# for i in range(1, 11):
#     print('The {}th Fabonacci number is {}.'.format(i,fab(i)))


