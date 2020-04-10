#(Celsius * 9/5) + 32 = Farenheit

#Using functions

def temp_convert(temp_in_celsius):
    temp_in_farenheit = (temp_in_celsius * 9/5) + 32
    return str(temp_in_celsius) + " degrees Celsius is " + str(temp_in_farenheit) + " degrees Farenheit"

user_input = input("Enter temperature in Celsius: ")
farenheit_result = temp_convert(float(user_input))

if float(user_input) > 38:
    print("It is relly hot!")

print(farenheit_result)