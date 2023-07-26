'''
Design a Python program that asks the user for a temperature in Fahrenheit.

The program should convert the temperature to Celsius and print out a message with the value.

When dealing with any numeric values in this problem, prefer floating point values to integers.
Fahrenheit to Celsius Formula

    Subtract 32 from the Fahrenheit temperature.

    Multiply the result by (5 / 9).

Example:

100 Fahrenheit

100 - 32 = 68

68 multiplied by (5 / 9) is 37.77

37.77 Celsius

'''

f_temperature = int(input("Enter the temperature in Fahrenheit: "))

c_temperature = format((f_temperature - 32) * (5 / 9), ".2f")

print(c_temperature) 

