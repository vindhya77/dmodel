from faker import *
ob=Faker()
print(ob.name())
print(ob.email())
print(ob.random_int())
for _ in range(10):
    print(ob.name())
