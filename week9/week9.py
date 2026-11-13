# def is_odd(n):
#     return n % 2 == 1
#
# print(is_odd(12))
# from distutils.command.install import key


# def is_lapyear(year):
#     if year %400 == 0:
#         return True
#     elif year %100 == 0:
#         return False
#     elif year %40:
#         return True
#     else:
#         return False
#
# print(is_lapyear(2100))

# def print_triangular_numbers(n):
#     total = 0
#     for i in range(1, n+1):
#         total += i
#         print(i,total)
# print_triangular_numbers(20)

# def is_prime(n):
#     if n<2:
#         return False
#     if n==2 or n==3:
#         return True
#     if n%2==0:
#         return False
#     for i in range(3,int(n**0.5)+1,2):
#         if n%i==0:
#             return False
#     return True
#
# print(is_prime(1001))

# def reverse(s):
#     result = ""
#     for ch in s:
#         result =result + ch
#     return result
#
# print(reverse("mustafa"))
#
# def reverse_slice(s):
#     return s[::-1]
# print(reverse_slice("mustafa"))


# def reverse_string(s):
#     return s[::-1]
#
# print(reverse_string("benim"))
# print(reverse_string("adım"))
# print(reverse_string("mustafa"))

# def remove_all_occurrences(sub,s):
#     return s.replace(sub,"y")
#
# print(remove_all_occurrences("ll","hello"))

# def substitute(message,key):
#     alphabet="abcçdefgğhıijklmnoöpqrsştuüvyz"
#     result = ""
#     for ch in message:
#         index = alphabet.find(ch.lower())
#         if index == -1:
#             result += ch
#         elif ch.isupper():
#             result = result + key[index].upper()
#         else:
#             result = result + key[index].lower()
#     return result
#
# key="ertyuıopğüasdfghjklşizcvbnmöç"
#
# print(substitute("naber müdür",key))

def remove_dups(s):
    result =""
    for ch  in s:
        if ch not in result:
            result = result + ch

    return result

print(remove_dups("hello world"))

