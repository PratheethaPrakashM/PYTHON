1.list
1.x=["arun","adhi","janaki","karthik","pratheetha"]
for i in x:
    print(i)
2. x.pop()

2.tuple
1.y=("pratheetha",22,"computer science")
(name,age,course)=y
print(course)

2. Using tuple is useful because it is oredered,immutable or unchangable we cannot add or remove a data if we have already saved it. so it is useful store it in tuple if its is unchangable.

3.set
s={"python","java","data science"}
s.remove("java")
print(s)

1. as duplication is not possible the "python" will not be added if we write it
2. we can use remove keyword to check if "java" file exist in the file. as if the element will remove if we use remove method then we can know that the it exist as remove()will raise error if the element is doesnot exist

4.frozenset

rules=frozenset(["attend regularly","Respect teachers","Submit assignments on time"])
print(rules)

1. no in frozenset we cannot add or remove a rules
2. when we check the frozen set then the rules will come in the first if it is in set

5. functions
1.name=["janaki","pratheetha"]
def search_name(name):
   if name==name:
      print("the name exists")
   else:
        print("its doesnot exist")
   return name
search_name("pratheetha")

2.y=name.count
print("students enrolled",y)


6.string
1.name="pratheetha prakash"
y=name.title()
print(y)

2.x=name.startswith("A")

7.operators
1.x=["english","maths","malayalam","social","science","hindi"]
if len(x)>5:
    print("warning")
else:
    print("its okay")


2.y=75
z=82
if y>z:
    print("y scored more than z")
else:
    print("z score more than y")        