def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("weight = " + str(weight))
    bmi = weight / height ** 2
    return bmi
    
BMI = calculate_bmi(weight=80, height=1.73)
print("Your BMI is", BMI)


def get_weight_status(bmi):
    if bmi < 18.5:
        return -1  # Underweight
    if 18.5 <= bmi < 25.0:
        return 0   # Normal weight
    if bmi > 25.0:
        return 1   # Overweight
    
status = get_weight_status(BMI)
print("Your weight status: ",status)
