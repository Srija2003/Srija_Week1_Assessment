def get_name():
    name=input(f"enter the name:")
    return name
    
def details():
    salary=int(input("enter the salary:"))
    age=int(input("enter the age:"))
    credit_score=int(input("enter your credit score:"))
    return salary, age, credit_score
    
def eligible_for_loan(salary, age, credit_score):
    if salary<30000:
        print("loan rejected")
    elif age<18:
        print("loan rejected")
    elif credit_score<680:
        print("loan rejected")
    else:
        print(f"loan approved")
    
def main():
    name=get_name()
    salary, age, credit_score=details()
    result= eligible_for_loan(salary, age, credit_score)
    print(result)  
main()
    
        