NumOfProp = int(input("Please enter how many propositions u want :  "))

variables = input("Please enter ur variables in the propo. :  ").split()

Prop = input("Please enter the Proposition :  ").split()

index1 = len(Prop)
count1 = 0
while count1 < index1:

    if Prop[count1] == "not":
        Prop[count1] = "(" + Prop[count1] + " " + Prop[count1 + 1] + ")"
        del Prop[count1 + 1]
        index1 -= 1

    count1 += 1

index2 = len(Prop)
count2 = 0
while count2 < index2:

    if Prop[count2] == "and":
        Prop[count2 - 1] = "(" + Prop[count2 - 1] + " " + Prop[count2] + " " + Prop[count2 + 1] + ")"
        del Prop[count2]
        del Prop[count2]
        index2 -= 2
        count2 -= 1

    count2 += 1

index3 = len(Prop)
count3 = 0
while count3 < index3:
    if Prop[count3] == "or":
        Prop[count3 - 1] = "(" + Prop[count3 - 1] + " " + Prop[count3] + " " + Prop[count3 + 1] + ")"
        del Prop[count3]
        del Prop[count3]
        index3 -= 2
        count3 -= 1

    count3 += 1

index4 = len(Prop)
count4 = 0
while count4 < index4:
    if Prop[count4] == "imply" or Prop[count4] == "implies":
        Prop[count4 - 1] = "(" + Prop[count4 - 1] + " " + Prop[count4] + " " + Prop[count4 + 1] + ")"
        del Prop[count4]
        del Prop[count4]
        index4 -= 2
        count4 -= 1

    count4 += 1

index5 = len(Prop)
count5 = 0
while count5 < index5:
    if Prop[count5] == "iff":
        Prop[count5 - 1] = "(" + Prop[count5 - 1] + " " + Prop[count5] + " " + Prop[count5 + 1] + ")"
        del Prop[count5]
        del Prop[count5]
        index5 -= 2
        count5 -= 1

    count5 += 1

index6 = len(Prop)
count6 = 0
while count6 < index6:
    if Prop[count6] == "xor":
        Prop[count6 - 1] = "(" + Prop[count6 - 1] + " " + Prop[count6] + " " + Prop[count6 + 1] + ")"
        del Prop[count6]
        del Prop[count6]
        index6 -= 2
        count6 -= 1

    count6 += 1

print("the proposition is : ", Prop)







