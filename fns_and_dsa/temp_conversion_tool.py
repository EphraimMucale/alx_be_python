FAHRENHEIT_TO_CELSIUS_FACTOR = (5 / 9)
CELCIUS_TO_FAHRENHEIT_FACTOR = (9 / 5)

def convert_to_celcius(fahrenheit):
    celcius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celcius

def convert_to_fahrenheit(celcius):
    fahrenheit = (celcius * CELCIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

def main():
    try:
        temperature = float(input("Enter the temperature to convert: "))
        unit = input("Is this temperature in Celcius or Fahrenheit? (C/F) ")

        if unit == "C":
            convert_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {convert_temp}°F")

        elif unit == "F":
            convert_temp = convert_to_celcius(temperature)
            print(f"{temperature}°F is {convert_temp}°C")

        else:
            print("Invalid input for temperature unit. Please enter 'C' for celcius or 'F' for Fahrenheit.")
    
    except ValueError:
        print('Invalid temperature. Please enter a numeric value')

if __name__ == "__main__":
    main()
