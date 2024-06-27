
from typing import Type 

def ciao(name: str):
    return f"Ciao, {name}"

def salve(name: str) -> str:
    return f"Salve, {name}"


def saluta_bob(func) -> str:
    return func("Bob")

print(saluta_bob(ciao))
print(saluta_bob(salve))


def parent():
    print("Sono in parent")



    def first_child():

        print("Sono in First Child!")

    def second_child():
        print("Sono in Second Child")

    second_child()
    first_child()

parent()

def decorator(func):
    def wrapper():
        print(f"Prima di func")
   
        func()
         
        print(f"Dopo func")
    return wrapper
 
def ciao():
    print(f"Ciao")

ciao = decorator(ciao)
ciao()

