# for i in range(0,10):
#     a = int(input('wpisz liczbe numer 1: \n'))
#     b = int(input('wpisz liczbe numer 2: \n'))
#     if a == 5:
#         print('suma liczby 1 oraz 2 wynosi:',a+b)
#         print('roznica liczby 1 oraz 2, wynosi:',a-b)
#     else:
#         print('nie podam ci wyniku poniewaz nie jest to liczba 5!')
#
list_with_numbers = [4,3,76,2,0,54,87,33]
something = ['a','b','c','d','e','f','g','h','i','j']
long = len(something)
# print(long)
def reverse():
    something_reverse = []
    for i in range(1,long+1):
        for_a_moment = something[-i]
        # print(something[-i])
        something_reverse.append(for_a_moment)
    print(something_reverse)
print(something)
reverse()
print(sorted(list_with_numbers))
# print(sorted(something_reverse))

class Idk:
    def __init__(self):
        print('something printed')
    def some(self):
        print('aaaa')
class_test = Idk()
class_test.some()




