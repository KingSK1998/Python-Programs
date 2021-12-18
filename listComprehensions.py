# LIST
my_list = [1, 2, 3]
double = [item * 2 for item in my_list]
print(double)
# [2, 4, 6]

# DICTIONARY
users = [
    {'name': "A", 'age': 1},
    {'name': "B", 'age': 2},
    {'name': "C", 'age': 3}
]
user_name = [user['name'] for user in users]
print(user_name)
# ['A', 'B', 'C']

# Filter Data
# if the user > 2
user_name = [user['name']
             for user in users if user['age'] > 2 and user['name'] == "C"]
print(user_name)
# ['C']

user_groups = [
    [
        {'name': 'Manuel',  'age': 31},
        {'name': 'Max',     'age': 30}
    ],
    [
        {'name': 'Sarah', 'age': 29},
        {'name': 'Julie', 'age': 32}
    ]
]

user_name = [person['name'] for group in user_groups for person in group]
print(user_name)
# ['Manuel', 'Max', 'Sarah', 'Julie']

user_name = [person['name']
             for group in user_groups for person in group if person['age'] > 30]
print(user_name)
# ['Manuel', 'Julie']

# code for 2D list like [[,,,],[,,,],[,,,]]
# entr = [list(int(x) for x in input().split()) for i in range(int(input()))]

# single line input accepter like 1 2 3 4 5 until enter is pressed
entr = [str(x) for x in input().split(' ')]
print(entr)
# ['1', '2', '3']
print("".join(entr))
# 123
