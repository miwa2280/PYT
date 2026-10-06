list_data = [334, 'kdfbgf', 334, True, 334]
dict_data = {
    'agedata': 15,
    'moneydata': 14674,
    'hobbiesdata': [],
}
dict_special = {
    'age': None,
    'money': None,
    'hobbies': None,
    'hobbies': None,
    # **dict_data,
} #  | dict_data

# print(dict_special)
# print(dict_special.keys())

# set_data = {44, 44, 'kdjhvjdfh', '565', 99, 44}
# set_data = set()
# set_data = set(list_data)
# set_data = set('gerhghidshgjdsfgjsdfhglhdsgkldfshghdfjklghkjdfhkghdshgjdfjkghkdghjkdjhfks')
# set_data = set(dict_data)
# print(type(set_data))
# print(set_data)

set_1 = {1, 2, 3, 4}
# set_2 = {4, 2, 3, 1}
set_2 = {3, 4, 5, 6}
print(set_1 == set_2)

# 1 обєднання
# union = set_1 | set_2
# union = set_1.union(set_2)
# print(union)

# перетин
# intersection = set_1 & set_2
# intersection = set_1.intersection(set_2)
# print(intersection)

# різниця
# difference = set_1 - set_2
# difference = set_1.difference(set_2)
# print(difference)

# симетрична різниця
# result = set_1 ^ set_2
# result = set_1.symmetric_difference(set_2)
# print(result)

set_1.add(656565656)
set_1.add(-656565656)
set_1.update([4444444, 99999999])
set_1.add(11)
print(set_1)

set_1.remove(1)
set_1.discard(1777777777)

print(set_1, 99999999999999)
set_1.pop()
print(set_1, 99999999999999)

if 11 in set_1:
    set_1.remove(11)

print(set_1)

set_1 |= set_2
print(set_1)