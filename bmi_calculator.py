print("------------------ BMI Calculator ------------------")

height = float(input("Enter your height in centimeters(cm): "))

weight = float(input("Enter your weight in kilograms(kg): "))

height = height / 100 

BMI = weight / (height ** 2)

print("Your Body Mass Index is: ", BMI)

if (BMI > 0):
    if (BMI <= 16):
        print("You are severely underweight.")
    elif (BMI <= 18.5):
        print("You are underweight.")
    elif (BMI <= 25):
        print("You are healthy.")
    elif (BMI <= 30):
        print("You are overweight.")
    else:
        print("You are severely overweight.")
else: 
    print("Enter valid details!!")