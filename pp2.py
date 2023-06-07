# Practice problem 2--------------->>>>>> Divide the apples

n = int(input("Enter the  number of apples: "))
mn = int(input("Enter the minimum number of range: "))
mx = int(input("Enter the maximum number of range: "))

if n < mn or n < mx:
    print(f"Number of apples is less than range {mn}-{mx}")

if mn == mx:
    print("Please enter a range, here lower bound and upper bound are equal")
    if n % mn == 0:
        print(f"{mn} is a divisor of n")

elif mn < mx:
    print(f"Between the range {mn}-{mx}, divisor of {n} are:")
    for i in range(mn, mx + 1):
        if n % i == 0:
            print(f"{i} is a divisor of {n}")
        else:
            print(f"{i} is not a divisor of {n}")

else:
    print("Please enter a correct input!!")
