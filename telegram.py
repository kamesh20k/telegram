# Taking kilometers input from the user
kilometers = int(input("Enter your numbers in kilometers: "))

# conversion factor
conv_fac = 0.6

# calculate miles
miles = kilometers * conv_fac
print('%0.2f kilometers = to %0.2f miles' %(kilometers,miles))
