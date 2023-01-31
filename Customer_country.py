import csv

with open ("customers.csv", 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    
    with open("customer_country.csv", 'w', newline = "") as new_file:
        csv_writer = csv.writer(new_file)
	
        for row in csv_reader:
            x = row[1] + " " + row[2], " " + row[4]
            csv_writer.writerow(x)

new_file.close()
