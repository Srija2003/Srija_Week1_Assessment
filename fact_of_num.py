def display(data):
    print(f"the fact is {data}")
    
def get_input():
    num = int(input("enter the number:"))
    return num

def fact(num):
    if num < 0:
        print(f"Factorial of negative numbers is invalid")
    result = 1
    for i in range(1, num+1):
        result *= i
    return result
def main():
    num = get_input()
    result = fact(num)
    if num > 0:
         display(result)
        
    
main()
    
    
    