#(Celsius * 9/5) + 32 = Farenheit

#Using functions

def temp_convert():
    user_input = input("Enter temperature in Celsius: ")
    temp_in_celsius = int(user_input)
    temp_in_farenheit = (temp_in_celsius * 9/5) + 32
    if float(user_input) > 38:
        print("It is relly hot!")

    print(str(temp_in_celsius) + " degrees Celsius is " + str(temp_in_farenheit) + " degrees Farenheit")

temp_convert()