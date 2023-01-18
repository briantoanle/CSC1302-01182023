# Toan Le
# CSC 1302
# in class activity Jan 18 2023

def main():
    meters = float(input('enter height in meter: '))
    kilogram = float(input('enter weight in kilogram: '))
    bmi(meters,kilogram)

def bmi(height, weight):
    print(f'The BMI for this person is {(weight/(height**2)):.2f}')

main()

