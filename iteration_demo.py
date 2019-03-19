sum = 0
for i in range(100):
    print('in the {}th iteration, current i is {}, sum is {}'.format(i,i,sum))
    sum = sum + i
    print('\t after adding i, the new sum is {}'.format(sum))

print(sum)

# sum = 0
# for i in range(1,11):
#     print('in the {}th iteration, current i*i is {}, sum is {}'.format(i,i,sum))
#     sum = sum + i*i
#     print('\t after adding square of i, the new sum is {}'.format(sum))
#
# print(sum)

#Calculate the value of your name, if we say 'a' is worth 1 and 'z' is worth 26.

# total_value=0
# name = 'misha'
#
# for letter in name:
#     total_value = total_value + (ord(letter)-96)
# print('The value of name {} is {}.'.format(name, total_value))

def countdown(n):
    while n>0:
        print(n)
        n = n - 1
        import time
        time.sleep(1)
    print('Blastoff!')
countdown(5)