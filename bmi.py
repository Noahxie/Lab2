def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("weight = " + str(weight))
    bmi = weight / height ** 2
    return bmi
    
BMI = calculate_bmi(weight=80, height=1.73)
print("Your BMI is", BMI)

if BMI < 18.5:
    print ("under weight")
if 18.5 < BMI < 25.0:
    print ("normal weight")
if BMI > 25.0:
    print ("over weight")

