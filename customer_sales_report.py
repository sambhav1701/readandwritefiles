import csv

with open ('sales.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    with open('salesreport.csv', 'w', newline = "") as new_file:
        csv_writer = csv.writer(new_file)
        
        header = next(csv_reader)

        csv_writer.writerow(['Customer ID','Total'])
        
        k = 0
        l = 0
        
        for row in csv_reader:
            x = (row[0])
            y = round(float(row[3]) + float(row[4]) + float(row[5]),2)
            if x != k:
                if k != 0:
                    csv_writer.writerow([k,round(l,2)])
                k = x
                l = y
            else:
                l += y
        round(csv_writer.writerow([k,l]),2)
    
new_file.close()