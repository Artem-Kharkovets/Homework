# s1 = Количество общих уникальных элементов в двух списках
# s2 = Даны два списка. Найти количество элементов,
#     которые находятся в обоих списках. Использовать множество.
# s4 = количество общих элементов

s1 = """
    Number of common unique elements in two lists"""
s2 = """
Two lists are given. Find the number of elements that are in 
both lists. Use a lot.\n"""
l1 = [1, 2, 2, 'three']
l2 = [9, 8, 2, 'three']
s3 = "\nResult:"
s4 = "number of common elements"

print(s1.upper())
print(s2)
print("l1 =", l1)
print("l2 =", l2)

l11 = set(l1)
l22 = set(l2)

a = l11 & l22
b = len(a)

print(s3, s4, b)
