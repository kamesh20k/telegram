# Taking kilometers input from the user
kilometers = int(input("Enter your values in kilometers: "))

# conversion factor
conv_fac = 0.6

# calculate miles
miles = kilometers * conv_fac
print('%0.2f kilometers is equal to %0.2f miles' %(kilometers,miles))
