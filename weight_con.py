weight=float(input("Enter Your weight: "))
unit= (input("Kilogram or Pound.(K or L): "))
if unit=="K":
    weight= weight * 2.205
    unit= "lbs"
    print(f"Your weight is: {round(weight,2) } {unit}")
elif unit=="L":
    weight= weight / 2.205
    unit= "kgs"
    print(f"Your weight is: {round(weight,2)} {unit}")
else:
    print(f"Your given {unit} is NOT valid")