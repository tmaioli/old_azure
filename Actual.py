print("hi, let's compute some interest")
# Python3 program to find compound
# interest for given values.

principle = float(input("Enter the principle: "))
rate = float(input("Enter the rate: "))
time = float(input("Enter time in years: "))

# Create a function for interest


def compound_interest(principle, rate, time):

    # Calculates compound interest
    Amount = principle * (pow((1 + rate / 100), time))
    CI = Amount - principle
    print("Compound interest is", CI)


compound_interest(principle, rate, time)
