import csv

with open ("EmployeePay.csv", 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')

    header = next(csv_reader)

    print('ID','FirstName','LastName','Total salary')

    for row in csv_reader:
        x = str(row[0]) + " " + str(row[1]), " " + str(row[2])
        y = float(row[3]) * float(row[4]) + float(row[3])
        print(f'{" ".join(x)}, {str(y)}')

        Enter = input("press ENTER to continue or type STOP to end")
        if Enter == 'STOP':
            break