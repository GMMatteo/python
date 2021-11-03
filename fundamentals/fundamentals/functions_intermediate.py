"""
Update Values In Dictionaries & Lists

Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
Change the last_name of the first student from 'Jordan' to 'Bryant'
In the sports_directory, change 'Messi' to 'Andres'
Change the value 20 in z to 30

"""

x = [ [5,2,3], [10,8,9] ]
(x[1][0]) = 15
print(x)

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
(students[0]['last_name']) = "Bryant"
print(students)

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
(sports_directory['soccer'][0])="Andres"
print(sports_directory)

z = [ {'x': 10, 'y': 20} ]
(z[0]['y'])=30
print(z)

"""
Iterate Through a List of Dictionaries
Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops through each dictionary in the list and prints each key and the associated value. For example, given the following list:

# iterateDictionary(students)
# # should output: (it's okay if each key-value pair ends up on 2 separate lines;
# # bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel
"""
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(some_list):
    listReturn = ""
    for i in some_list:
        listReturn += f"first_name - {i['first_name']}, last_name - {i['last_name']}\n"
    return listReturn
print(iterateDictionary(students))


"""
Get Values From a List of Dictionaries
Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary. For example, iterateDictionary2('first_name', students) should output:
"""

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary2(first_last,some_list):
    name = ""
    for x in some_list:
        name += f"{x[first_last]} \n"
    return name
print(iterateDictionary2('first_name',students))
print(iterateDictionary2('last_name',students))

"""
Iterate Through a Dictionary with List Values
Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key along with the size of its list, and then prints the associated values within each key's list. For example:

# output:
7 LOCATIONS
San Jose
Seattle
Dallas
Chicago
Tulsa
DC
Burbank

8 INSTRUCTORS
Michael
Amy
Eduardo
Josh
Graham
Patrick
Minh
Devon
"""
dojo = {
'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for key,val in some_dict.items():
        print('')
        print(f"{len(val)} {key.upper()}")
        for i in range(0,len(val)):
            print(val[i])
printInfo(dojo)

