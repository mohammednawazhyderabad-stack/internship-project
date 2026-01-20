import art

print(art)
def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

operations = {"+":add,
              "-":subtract,
              "*":multiply,
              "/":divide
              }

def calculator():
    should_accmulate = True
    num1 = float(input("What is your first number? :"))

    while should_accmulate:
        for symbol in operations:
            print(f"operations:{symbol}")

        operation_symbol =input("Pick your operation? :")
        num2 = float(input("What is your Next number? :"))

        answer = operations[operation_symbol](num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer} , or Type 'n' to Calculate new:")
        if choice =="y":
            num1 = answer
        else:
            should_accmulate =False
            print("\n" *20)
            calculator()


calculator()