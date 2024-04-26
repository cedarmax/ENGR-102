gender = (input("What is the gender?   "))
age = int(input("How old it the person?   "))
Cholesterol = int(input("What is the Cholesterol amount?    "))
HDL = int(input("What is the HDL"))
smoker = (input("Is the person a smoker?   "))
Systolic_BP = int(input("What is the systolic Bp"))
Treated = (input("is the person treated?"))
points = 0
if (gender=="male" or gender=="Male" or gender =="M"):
    if(age>=20 and age<=30):
        points += -9
        if(Cholesterol<160):
            points += 0
        elif(Cholesterol>=160 and Cholesterol<=199):
            points += 4
        elif (Cholesterol >= 200 and Cholesterol <= 239):
            points += 7
        elif (Cholesterol >= 240 and Cholesterol <= 279):
            points += 9
        elif (Cholesterol >= 280):
            points += 11
        if(smoker=="no"):
                points += 0
        elif(smoker=="yes"):
            points += 8
        if (HDL>60):
            points+= -1
        elif (HDL<=59 and HDL>=50):
            points += 0
        elif (HDL >= 40 and HDL <=49):
            points += 1
        elif (HDL < 40):
            points +=2
        if(Systolic_BP<120 and Treated=="no"):
            points += 0
        elif(Systolic_BP<120 and Treated=="yes"):
            points += 0
        if (Systolic_BP >= 120 and Systolic_BP<=129 and Treated == "no"):
            points += 0
        elif (Systolic_BP >= 120 and Treated == "yes" and Systolic_BP<= 129):
            points += 1
        if (Systolic_BP >= 130 and Systolic_BP<=139 and Treated == "no"):
            points += 1
        elif (Systolic_BP >= 130 and Treated == "yes" and Systolic_BP<= 139):
            points += 2
        if (Systolic_BP >= 140 and Systolic_BP<=159 and Treated == "no"):
            points += 1
        elif (Systolic_BP >= 140 and Treated == "yes" and Systolic_BP<= 159):
            points += 2
        if (Systolic_BP >= 160 and Treated == "no"):
            points += 2
        elif (Systolic_BP >= 160 and Treated == "yes"):
            points += 3
    elif (age >= 35 and age <= 39):
        points += -4
        if (Cholesterol < 160):
             points += 0
        elif (Cholesterol >= 160 and Cholesterol <= 199):
            points += 4
        elif (Cholesterol >= 200 and Cholesterol <= 239):
             points += 7
        elif (Cholesterol >= 240 and Cholesterol <= 279):
            points += 9
        elif (Cholesterol >= 280):
            points += 11
        if (smoker == "no"):
            points += 0
        elif (smoker == "yes"):
            points += 8
        if (HDL > 60):
            points += -1
        elif (HDL <= 59 and HDL >= 50):
            points += 0
        elif (HDL >= 40 and HDL <= 49):
            points += 1
        elif (HDL < 40):
            points += 2
        if (Systolic_BP < 120 and Treated == "no"):
            points += 0
        elif (Systolic_BP < 120 and Treated == "yes"):
            points += 0
        if (Systolic_BP >= 120 and Systolic_BP <= 129 and Treated == "no"):
            points += 0
        elif (Systolic_BP >= 120 and Treated == "yes" and Systolic_BP <= 129):
            points += 1
        if (Systolic_BP >= 130 and Systolic_BP <= 139 and Treated == "no"):
             points += 1
        elif (Systolic_BP >= 130 and Treated == "yes" and Systolic_BP <= 139):
             points += 2
        if (Systolic_BP >= 140 and Systolic_BP <= 159 and Treated == "no"):
            points += 1
        elif (Systolic_BP >= 140 and Treated == "yes" and Systolic_BP <= 159):
            points += 2
        if (Systolic_BP >= 160 and Treated == "no"):
            points += 2
        elif (Systolic_BP >= 160 and Treated == "yes"):
            points += 3
    elif (age >= 40 and age <= 44):
        points += 0
        if (Cholesterol < 160):
             points += 0
        elif (Cholesterol >= 160 and Cholesterol <= 199):
            points += 3
        elif (Cholesterol >= 200 and Cholesterol <= 239):
             points += 5
        elif (Cholesterol >= 240 and Cholesterol <= 279):
            points += 6
        elif (Cholesterol >= 280):
            points += 8
        if (smoker == "no"):
            points += 0
        elif (smoker == "yes"):
            points += 5
        if (HDL > 60):
            points += -1
        elif (HDL <= 59 and HDL >= 50):
            points += 0
        elif (HDL >= 40 and HDL <= 49):
            points += 1
        elif (HDL < 40):
            points += 2
        if (Systolic_BP < 120 and Treated == "no"):
            points += 0
        elif (Systolic_BP < 120 and Treated == "yes"):
            points += 0
        if (Systolic_BP >= 120 and Systolic_BP <= 129 and Treated == "no"):
            points += 0
        elif (Systolic_BP >= 120 and Treated == "yes" and Systolic_BP <= 129):
            points += 1
        if (Systolic_BP >= 130 and Systolic_BP <= 139 and Treated == "no"):
             points += 1
        elif (Systolic_BP >= 130 and Treated == "yes" and Systolic_BP <= 139):
             points += 2
        if (Systolic_BP >= 140 and Systolic_BP <= 159 and Treated == "no"):
            points += 1
        elif (Systolic_BP >= 140 and Treated == "yes" and Systolic_BP <= 159):
            points += 2
        if (Systolic_BP >= 160 and Treated == "no"):
            points += 2
        elif (Systolic_BP >= 160 and Treated == "yes"):
            points += 3
    elif (age >= 45 and age <= 49):
        points += 3
        if (Cholesterol < 160):
             points += 0
        elif (Cholesterol >= 160 and Cholesterol <= 199):
            points += 3
        elif (Cholesterol >= 200 and Cholesterol <= 239):
             points += 5
        elif (Cholesterol >= 240 and Cholesterol <= 279):
            points += 6
        elif (Cholesterol >= 280):
            points += 8
        if (smoker == "no"):
            points += 0
        elif (smoker == "yes"):
            points += 5
        if (HDL > 60):
            points += -1
        elif (HDL <= 59 and HDL >= 50):
            points += 0
        elif (HDL >= 40 and HDL <= 49):
            points += 1
        elif (HDL < 40):
            points += 2
        if (Systolic_BP < 120 and Treated == "no"):
            points += 0
        elif (Systolic_BP < 120 and Treated == "yes"):
            points += 0
        if (Systolic_BP >= 120 and Systolic_BP <= 129 and Treated == "no"):
            points += 0
        elif (Systolic_BP >= 120 and Treated == "yes" and Systolic_BP <= 129):
            points += 1
        if (Systolic_BP >= 130 and Systolic_BP <= 139 and Treated == "no"):
             points += 1
        elif (Systolic_BP >= 130 and Treated == "yes" and Systolic_BP <= 139):
             points += 2
        if (Systolic_BP >= 140 and Systolic_BP <= 159 and Treated == "no"):
            points += 1
        elif (Systolic_BP >= 140 and Treated == "yes" and Systolic_BP <= 159):
            points += 2
        if (Systolic_BP >= 160 and Treated == "no"):
            points += 2
        elif (Systolic_BP >= 160 and Treated == "yes"):
            points += 3
    elif (age >= 50 and age <= 54):
        points += 6
        if (Cholesterol < 160):
             points += 0
        elif (Cholesterol >= 160 and Cholesterol <= 199):
            points += 2
        elif (Cholesterol >= 200 and Cholesterol <= 239):
             points += 3
        elif (Cholesterol >= 240 and Cholesterol <= 279):
            points += 4
        elif (Cholesterol >= 280):
            points += 5
        if (smoker == "no"):
            points += 0
        elif (smoker == "yes"):
            points += 3
        if (HDL > 60):
            points += -1
        elif (HDL <= 59 and HDL >= 50):
            points += 0
        elif (HDL >= 40 and HDL <= 49):
            points += 1
        elif (HDL < 40):
            points += 2
        if (Systolic_BP < 120 and Treated == "no"):
            points += 0
        elif (Systolic_BP < 120 and Treated == "yes"):
            points += 0
        if (Systolic_BP >= 120 and Systolic_BP <= 129 and Treated == "no"):
            points += 0
        elif (Systolic_BP >= 120 and Treated == "yes" and Systolic_BP <= 129):
            points += 1
        if (Systolic_BP >= 130 and Systolic_BP <= 139 and Treated == "no"):
             points += 1
        elif (Systolic_BP >= 130 and Treated == "yes" and Systolic_BP <= 139):
             points += 2
        if (Systolic_BP >= 140 and Systolic_BP <= 159 and Treated == "no"):
            points += 1
        elif (Systolic_BP >= 140 and Treated == "yes" and Systolic_BP <= 159):
            points += 2
        if (Systolic_BP >= 160 and Treated == "no"):
            points += 2
        elif (Systolic_BP >= 160 and Treated == "yes"):
            points += 3
    elif (age >= 55 and age <= 59):
        points += 8
        if (Cholesterol < 160):
             points += 0
        elif (Cholesterol >= 160 and Cholesterol <= 199):
            points += 2
        elif (Cholesterol >= 200 and Cholesterol <= 239):
             points += 3
        elif (Cholesterol >= 240 and Cholesterol <= 279):
            points += 4
        elif (Cholesterol >= 280):
            points += 5
        if (smoker == "no"):
            points += 0
        elif (smoker == "yes"):
            points += 1
        if (HDL > 60):
            points += -1
        elif (HDL <= 59 and HDL >= 50):
            points += 0
        elif (HDL >= 40 and HDL <= 49):
            points += 1
        elif (HDL < 40):
            points += 2
        if (Systolic_BP < 120 and Treated == "no"):
            points += 0
        elif (Systolic_BP < 120 and Treated == "yes"):
            points += 0
        if (Systolic_BP >= 120 and Systolic_BP <= 129 and Treated == "no"):
            points += 0
        elif (Systolic_BP >= 120 and Treated == "yes" and Systolic_BP <= 129):
            points += 1
        if (Systolic_BP >= 130 and Systolic_BP <= 139 and Treated == "no"):
             points += 1
        elif (Systolic_BP >= 130 and Treated == "yes" and Systolic_BP <= 139):
             points += 2
        if (Systolic_BP >= 140 and Systolic_BP <= 159 and Treated == "no"):
            points += 1
        elif (Systolic_BP >= 140 and Treated == "yes" and Systolic_BP <= 159):
            points += 2
        if (Systolic_BP >= 160 and Treated == "no"):
            points += 2
        elif (Systolic_BP >= 160 and Treated == "yes"):
            points += 3
    elif (age >= 60 and age <= 64):
        points += 10
        if (Cholesterol < 160):
             points += 0
        elif (Cholesterol >= 160 and Cholesterol <= 199):
            points += 1
        elif (Cholesterol >= 200 and Cholesterol <= 239):
             points += 1
        elif (Cholesterol >= 240 and Cholesterol <= 279):
            points += 2
        elif (Cholesterol >= 280):
            points += 3
        if (smoker == "no"):
            points += 0
        elif (smoker == "yes"):
            points += 3
        if (HDL > 60):
            points += -1
        elif (HDL <= 59 and HDL >= 50):
            points += 0
        elif (HDL >= 40 and HDL <= 49):
            points += 1
        elif (HDL < 40):
            points += 2
        if (Systolic_BP < 120 and Treated == "no"):
            points += 0
        elif (Systolic_BP < 120 and Treated == "yes"):
            points += 0
        if (Systolic_BP >= 120 and Systolic_BP <= 129 and Treated == "no"):
            points += 0
        elif (Systolic_BP >= 120 and Treated == "yes" and Systolic_BP <= 129):
            points += 1
        if (Systolic_BP >= 130 and Systolic_BP <= 139 and Treated == "no"):
             points += 1
        elif (Systolic_BP >= 130 and Treated == "yes" and Systolic_BP <= 139):
             points += 2
        if (Systolic_BP >= 140 and Systolic_BP <= 159 and Treated == "no"):
            points += 1
        elif (Systolic_BP >= 140 and Treated == "yes" and Systolic_BP <= 159):
            points += 2
        if (Systolic_BP >= 160 and Treated == "no"):
            points += 2
        elif (Systolic_BP >= 160 and Treated == "yes"):
            points += 3
    elif (age >= 75):
        points += 13
        if (Cholesterol < 160):
             points += 0
        elif (Cholesterol >= 160 and Cholesterol <= 199):
            points += 0
        elif (Cholesterol >= 200 and Cholesterol <= 239):
             points += 0
        elif (Cholesterol >= 240 and Cholesterol <= 279):
            points += 1
        elif (Cholesterol >= 280):
            points += 1
        if (smoker == "no"):
            points += 0
        elif (smoker == "yes"):
            points += 3
        if (HDL > 60):
            points += -1
        elif (HDL <= 59 and HDL >= 50):
            points += 0
        elif (HDL >= 40 and HDL <= 49):
            points += 1
        elif (HDL < 40):
            points += 2
        if (Systolic_BP < 120 and Treated == "no"):
            points += 0
        elif (Systolic_BP < 120 and Treated == "yes"):
            points += 0
        if (Systolic_BP >= 120 and Systolic_BP <= 129 and Treated == "no"):
            points += 0
        elif (Systolic_BP >= 120 and Treated == "yes" and Systolic_BP <= 129):
            points += 1
        if (Systolic_BP >= 130 and Systolic_BP <= 139 and Treated == "no"):
             points += 1
        elif (Systolic_BP >= 130 and Treated == "yes" and Systolic_BP <= 139):
             points += 2
        if (Systolic_BP >= 140 and Systolic_BP <= 159 and Treated == "no"):
            points += 1
        elif (Systolic_BP >= 140 and Treated == "yes" and Systolic_BP <= 159):
            points += 2
        if (Systolic_BP >= 160 and Treated == "no"):
            points += 2
        elif (Systolic_BP >= 160 and Treated == "yes"):
            points += 3
    elif (age >= 60 and age <= 64):
        points += 10
        if (Cholesterol < 160):
             points += 0
        elif (Cholesterol >= 160 and Cholesterol <= 199):
            points += 1
        elif (Cholesterol >= 200 and Cholesterol <= 239):
             points += 1
        elif (Cholesterol >= 240 and Cholesterol <= 279):
            points += 2
        elif (Cholesterol >= 280):
            points += 3
        if (smoker == "no"):
            points += 0
        elif (smoker == "yes"):
            points += 3
        if (HDL > 60):
            points += -1
        elif (HDL <= 59 and HDL >= 50):
            points += 0
        elif (HDL >= 40 and HDL <= 49):
            points += 1
        elif (HDL < 40):
            points += 2
        if (Systolic_BP < 120 and Treated == "no"):
            points += 0
        elif (Systolic_BP < 120 and Treated == "yes"):
            points += 0
        if (Systolic_BP >= 120 and Systolic_BP <= 129 and Treated == "no"):
            points += 0
        elif (Systolic_BP >= 120 and Treated == "yes" and Systolic_BP <= 129):
            points += 1
        if (Systolic_BP >= 130 and Systolic_BP <= 139 and Treated == "no"):
             points += 1
        elif (Systolic_BP >= 130 and Treated == "yes" and Systolic_BP <= 139):
             points += 2
        if (Systolic_BP >= 140 and Systolic_BP <= 159 and Treated == "no"):
            points += 1
        elif (Systolic_BP >= 140 and Treated == "yes" and Systolic_BP <= 159):
            points += 2
        if (Systolic_BP >= 160 and Treated == "no"):
            points += 2
        elif (Systolic_BP >= 160 and Treated == "yes"):
            points += 3
print(points)