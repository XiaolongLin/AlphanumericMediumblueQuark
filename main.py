temp = input("Enter temperature:")
unit = input ("Enter unit in F/f or C/c: ")
temp=int(temp)
if unit == "F" or "f":
  
  c = (temp-32)/1.8
  print(f"temp° in Fahrenheit is equivalent to c° Celsius.")
elif unit == "C" or "c":
  
  f = temp*1.8+32
  print(f"temp ° in Celsius is equivalent to f° Fahrenheit.")
else:
  print(f"Invalid unit(bad).") 
