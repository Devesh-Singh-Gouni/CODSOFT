
def add(n1, n2):
    return n1 + n2
def multi(n1,n2):
    return n1*n2
def sub(n1,n2):
    return n1-n2
def div(n1,n2):
    if n2==0:
        return "error"
    else:
        return n1/n2

operations={
    "+": add ,
    "*": multi,
    "-": sub,
    "/": div
}
def calculator():

    conti = True
    f = float(input("Type the first number: "))

    while conti:
        op=input("Enter mathematical operator '+', '-', '*' or '/' ")
        s=float(input("Type the second number: "))

        result=operations[op](f,s)
        print(f"{f} {op} {s} = {result}")

        again=input(f" type 'y' to continue with {result} or 'n' to start new operation :").lower()
        if again=="y":
            f=result
        else:
            f = float(input("Type the first number: "))
            print("\n" * 20)
            calculator()

calculator()
