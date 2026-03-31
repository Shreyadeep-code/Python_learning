# in dictionary all types of value can be stored
info ={
    "name" : "shreyadeep",
    "learn" : "coding",
    "branch" : "CSE",
    "age": 19,
    "is  a voter" : True,
    "marks" : 88,
    "subjects" : ["C", "java", "python"],#list
    "topics" : ("dict", "set")#tuple
}
print(info)
print(type(info))
# dictionary can be changed, key are not repeated
print(info["name"])# returns the value at that key if not available then it givrs error
info["name"] = "shuprakash"
info["age"] = 13
info["surname"] = "parida"# adding new key
print(info)
#null dictionary can be created
# Nested dictionary
student ={
    "name" : "shreyadeep",
    "score" : {
        "math" : 99,
        "chem" : 94
    }
}
"""print(student)
print(student["score"])
print(student["score"]["math"])
#methods
print(info.keys())#return all the keys used in dictionary
print(list(info.keys())) # type casting to list
print(len(info))
print(tuple(info.values()))"""
print(list(info.items()))# items() returns the value of keys with their values in forms of pairs
print(info.get("name"))# retutn the value at the key if not available it return none
new__dict ={'city' : 'goa','name' : 'suvendu'}
info.update(new__dict)
print(info)