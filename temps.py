fah = int(input("Please type in a temperature(F)"))

cels = ((fah-32) * 5) / 9 

print(f"{fah} degress Fahrenheit equals {cels} degrees Celsius")

if cels < 0:
    print("Brr! It's cold in here!")



