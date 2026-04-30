s = "Hello World!"

print (s[0])
print (s[2])
print (s[-2])
print (s[1:7])
print (s[1:10:2])
print (s[1:])
print (s[:8])
print (s[10:1:-1])
print (s[::-1])

s1 = "Hello "
s2 = "World"
s3 = "!"
s3 = s1 + s2 + s3
print(s3)

n1 = "10"
n2 = 3
n3 = n1 * n2
print(n3)

n1 = "World "
n2 = 3
n3 = n1 * n2
print(n3)

print(s.lower())
print(s.upper())
print(s.split("o"))
print(s.split("l"))
print(s.strip())
print(s.count("l"))

name = input("Enter name: ")
lname = input("Enter last name: ")

print("Hello {} {}!".format(lname, name))
print("Hello {1} {0}!".format(lname, name))
print(f"Hello {name} {lname}!")







