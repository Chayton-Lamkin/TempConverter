# CIT 144 - Python I 
# Chayton Lamkin

inputTemp = int(input("Enter a temperature value to convert: "))
inputValue = input("Convert to Fahrenheit or Celsius? Enter F or C: ")

if inputValue == "F" or inputValue == "f" :
    degF = 1.8 * inputTemp + 32
    print(f"{inputTemp} deg C - {round(degF, 2)} degree F")
elif inputValue == "C" or inputValue == "c" :
    degC = (inputTemp - 32) / 1.8
    print(f"{inputTemp} deg F - {round(degC, 2)} degree C")
else :
    print("You did not enter an F or C. Goodbye.")

