import argparse
import math


def count_months(pv, m, i):
    n = math.ceil(math.log(m / (m - i * pv), 1 + i))
    return n


def nominal_interest(interest):
    return (interest * 0.01 / 12)


def monthly_payments(pv, m, i):
    i = nominal_interest(float(i))
    n = count_months(pv, m, i)
    overpay = n * m - pv
    years = divmod(n, 12)[0]
    months = divmod(n, 12)[1]
    if years == 0:
        if months == 1:
            return "It will take 1 month to repay this loan!\n" + "Overpayment = " + str(overpay)
        elif months > 1:
            return "It will take " + str(months) + " months to repay this loan!\n" + "Overpayment = " + str(overpay)
    if years == 1:
        if months == 0:
            return "It will take 1 year to repay this loan!\n" + "Overpayment = " + str(overpay)
        elif months == 1:
            return "It will take 1 year and 1 month to repay this loan!\n" + "Overpayment = " + overpay
        else:
            return "It will take " + str(years) + " year and " + str(
                months) + " to repay this loan!\n" + "Overpayment = " + str(overpay)
    if years > 1:
        if months == 0:
            return "It will take " + str(years) + " years to repay this loan!\n" + "Overpayment = " + str(overpay)
        elif months == 1:
            return "It will take " + str(years) + " years and 1 month to repay this loan!\n" + "Overpayment = " + str(
                overpay)
        else:
            return "It will take " + str(years) + " years and " + str(
                months) + " to repay this loan!\n" + "Overpayment = " + str(overpay)


def annuity_monthly(pv, n, i):
    i = nominal_interest(float(i))
    a = pv * i * math.pow(1 + i, n) / (math.pow(1 + i, n) - 1)
    return "Your monthly payment = " + str(math.ceil(a)) + "!"


def loan_principal(pmt, n, i):
    i = nominal_interest(float(i))
    p = pmt / i * (1 - (1 / math.pow(1 + i, n)))
    return "Your loan principal = " + str(p) + "!"


def calculate_differentiate(pv, n, i):
    overpay = 0
    i = nominal_interest(i)
    for m in range(1, int(n) + 1):
        diff = math.ceil((pv / n) + i * (pv - (pv * (m - 1) / n)))
        overpay += diff
        print("Month 1: payment is ", diff)
    print("Overpayment = ", overpay - pv)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Foo')
    parser.add_argument('-t', '--type', help='type of calculation', required=True, choices=['annuity', 'diff'])
    parser.add_argument('-P', '--principal', help='The loan principal', required=False)
    parser.add_argument('-p', '--periods', help='The number of periods', required=False)
    parser.add_argument('-i', '--interest', help='The loan interest', required=False)
    parser.add_argument('-c', '--payment', help='The monthly payment', required=False)
    args = parser.parse_args()

arguments = {'type': args.type, 'principal': args.principal, 'periods': args.periods, 'interest': args.interest,
             'payment': args.payment}
arg_sum = 0
for key, value in arguments.items():
    if value is not None:
        if value[0] == "-":
            print("Incorrect parameters")
            quit()
        arg_sum += 1
if arg_sum < 4 or arg_sum > 4:
    print("Incorrect parameters")
elif args.interest is None:
    print("Incorrect parameters")
elif args.type == 'annuity':
    if args.periods is None:
        pv = float(args.principal)
        m = float(args.payment)
        i = float(args.interest)
        print(monthly_payments(pv, m, i))
    elif args.payment is None:
        a = float(args.principal)
        m = float(args.periods)
        i = float(args.interest)
        print(annuity_monthly(a, m, i))
    elif args.principal is None:
        p = float(args.payment)
        n = float(args.periods)
        i = float(args.interest)
        print(loan_principal(p, n, i))
    else:
        print("Incorrect parameters")
elif args.type == 'diff':
    pv = float(args.principal)
    n = float(args.periods)
    i = float(args.interest)
    calculate_differentiate(pv, n, i)
else:
    print("Incorrect parameters")
