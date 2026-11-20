# myList=[76,92.3,"hello",True,4,76]
# myList.append("apple")
# myList.append(76)
# myList.insert(3,"cat")
# myList.insert(0,99)
# print(myList)
#
# print(myList.index("hello"))
#
# print(myList.count(76))
#
# myList.remove(76)
# print(myList)
#
# myList.pop(myList.index(True))
# print(myList)

# def sum_of_squares(number_list):
#     total = 0
#     for number in number_list:
#         total += number**2
#     return total
# mylist = [3, 4, 5, 6]
# print(sum_of_squares(mylist))
#
# for number in mylist:
#     if number % 2 == 0:
#       (number**2)
#     else :
#       pass

# myList=['apple','cat','lemon','banana','tiger']
# print(myList)
# for words in myList:
#     if words in myList:
#         len(words)==5
#         print(words)
#     else :
#         pass
#
# def sum_until_even(number_list):
#     sum=0
#     for number in number_list:
#         if number%2==0:
#             break
#         sum += number
#     return sum
#
# myList=[1,3,3,5,7,6,7,8,9]
# print(sum_until_even(myList))

# def count_util_sam(words):
#     count = 0
#     for word in words:
#         count += 1
#         if word == 'sam':
#             break
#         return count
#
# words = ['karl', 'jhon', 'amanda', 'abdurrazak', 'sam', 'sam']
#
# print(count_util_sam(words))

# def replace(s, old, new):
#     pieces = s.split(old)
#     return new.join(pieces)
#
# def test(actual, expected):
#     if actual == expected:
#         print("PASSED")
#
#     else:
#         print("FAILED")
#
# test(replace('Mississippi','i','ı'),'Mıssıssıppı')

# def find_max_value_in_list(num_list):
#     max_value = num_list[0]
#     for num in num_list:
#         if num > max_value:
#             max_value = num
#         return max_value
#
#
# num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(find_max_value_in_list(num_list))