def celsius_to_farenheit(celsius):
    farenheit = 1.8 * celsius +32
    return farenheit
 
def celsius_to_kelvin(celsius):
    kelvin= celsius +273.15
    return kelvin

def farenheit_to_celsius(farenheit):
    celsius= 5/9*(farenheit -32)
    
    return celsius

def farenheit_to_kelvin(farenheit):
    kelvin= 5/9*(farenheit-32)+273.15
    
    return kelvin
def kelvin_to_celsius(kelvin):
    celsius=kelvin-273.15
    
    return celsius

def kelvin_to_farenheit(kelvin):
    farenheit=9/5*(kelvin-273.15)+32
    
    return farenheit

def main():
    while True:
        
        print("1. Celsius to Fahrenheit")
        print("2. Celsius to Kelvin")
        print("3. Fahrenheit to Celsius")
        print("4. Fahrenheit to Kelvin")
        print("5. Kelvin to Celsius")
        print("6. Kelvin to Fahrenheit")
        print("7. Exit")
        choice=int(input())
        if choice==1:
            celsius=float(input("enter tem:"))
            print(celsius_to_farenheit(celsius))
        elif choice==2:
            celsius=float(input("enter tem:"))
            print(celsius_to_kelvin(celsius))
        elif choice==3:
            farenheit=float(input("enter tem:"))
            print(farenheit_to_celsius(farenheit))
        elif choice==4:
            farenheit=float(input("enter tem:"))
            print(farenheit_to_kelvin(farenheit))
        elif choice==5:
            kelvin=float(input("enter tem:"))
            print(kelvin_to_celsius(kelvin))
        elif choice==6:
            kelvin=float(input("enter tem:"))
            print(kelvin_to_farenheit(kelvin))
        else:
            return 0
        
main()
        