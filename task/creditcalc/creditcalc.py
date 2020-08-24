import math
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--type")
parser.add_argument("--payment")
parser.add_argument("--principal")
parser.add_argument("--periods")
parser.add_argument("--interest")
args = parser.parse_args()

valid_args = 0
t = args.type
valid_args += 1 if t is not None else 0
a = args.payment
valid_args += 1 if a is not None else 0
p = args.principal
valid_args += 1 if p is not None else 0
n = args.periods
valid_args += 1 if n is not None else 0
i = args.interest
valid_args += 1 if i is not None else 0

if valid_args != 4 or t is None or t != "annuity" and t != "diff":
    print("Incorrect parameters")
    sys.exit()

if t == "diff":
    if a is not None:
        print("Incorrect parameters")
        sys.exit()

    p = float(p)
    n = int(n)
    i = float(i) / 1200
    overpayment = -p
    for m in range(n):
        a = math.ceil(p / n * (1 + i * (n - m)))
        overpayment += a
        print(f"Month {m + 1}: paid out {a}")
    print(f"\nOverpayment = {int(overpayment)}")
elif t == "annuity":
    if n is None:
        p = float(p)
        a = float(a)
        i = float(i) / 1200

        x = a / (a - i * p)
        base = 1 + i
        n = math.ceil(math.log(x, base))
        years = n // 12
        months = n % 12
        if years > 0 and months > 0:
            print(f"You need {years} years and {months} months to repay this credit!")
        elif years > 0:
            print(f"You need {years} years to repay this credit!")
        elif months > 0:
            print(f"You need {months} months to repay this credit!")
    elif a is None:
        p = float(p)
        n = int(n)
        i = float(i) / 1200

        powered = math.pow(1 + i, n)
        a = math.ceil(p * (i * powered) / (powered - 1))
        print(f"Your annuity payment = {a}!")
    elif p is None:
        a = float(a)
        n = int(n)
        i = float(i) / 1200

        powered = math.pow(1 + i, n)
        p = int(a / ((i * powered) / (powered - 1)))
        print(f"Your credit principal = {p}!")
    else:
        print("Incorrect parameters")
        sys.exit()
    overpayment = int(n * a - p)
    print(f"Overpayment = {overpayment}")
