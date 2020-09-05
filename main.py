temp = input("Enter temperature:")
unit = input ("Enter unit in F/f or C/c: ")
temp=int(temp)
if unit == "F" or unit == "f":
  n = (temp-32)/1.8
  print(f"temp° in Fahrenheit is equivalent to n° Celsius.")
elif unit == "C" or unit == "c":
  n = temp*1.8+32
  print(f"temp ° in Celsius is equivalent to n° Fahrenheit.")
else:
  print(f"Invalid unit(bad).") 
