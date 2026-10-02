# python weight converter

weight = float(input("enter your weight:"))
unit = input("kilograms or pounds? ( K or L): ")


if unit == "K":
    weight = weight * 2.205
    unit = "Lbs."
    print(f"your weight is {round(weight,2)} {unit}.")
elif unit == "L":
    weight = weight/2.205
    unit = "Kgs"
    print(f"your weight is {round(weight,2)} {unit}.")
else:
    print(f"{unit} was not valid")
    print(f"{weight} was not valid")

