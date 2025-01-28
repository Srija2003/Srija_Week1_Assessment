def get_number():
    return int(input("enter the number for table:"))

def get_range():
    start = int(input("enter starting range:"))
    end = int(input("enther the end range:"))
    return start, end

def generate_table(number, start, end):
    print(f"table fo {number} from {start} to {end}:\n")
    for i in range(start, end+1):
        print(f"{number}x{i} = {number*i}")
        
def main():
    number = get_number()
    start, end = get_range()
    generate_table(number, start, end)
    
main()