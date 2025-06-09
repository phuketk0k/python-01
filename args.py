import sys

def add(n1, n2):
    a = n1 + n2
    return a

def sub(n1, n2):
    sub = n1 - n2
    return sub

def mul(n1, n2):
    mul = n1 * n2
    return mul

def div(n1, n2):
    div = n1 / n2
    return div

n1 = int(sys.argv[1])
operation = sys.argv[2]
n2 = int(sys.argv[3])

if operation == "add":
    output = add(n1, n2)
    print(output)

if operation == "sub":
    output = sub(n1, n2)
    print(output)

if operation == "mul":
    output = mul(n1, n2)
    print(output)

if operation == "div":
    output = div(n1, n2)
    print(output)
