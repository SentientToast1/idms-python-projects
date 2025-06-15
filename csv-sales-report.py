import csv
 
FILENAME = "products.csv"
REPORTFILE = "reports.txt"
OUTPUTCSV = "products-cleaned.csv"

with open(FILENAME,'r') as file:
    reader = list(csv.reader(file))


# Blanks checker
new_rows = [] 
blank = False
for rows in range(len(reader)):
    if len(reader[rows]) == 0:
        blank = True
    else:
        for cols in range(len(reader[rows])):
            if reader[rows][cols] == '':
                blank = True
    if not blank:
        new_rows.append(reader[rows])
    else:
        blank = False

#highest sales
working_rows = new_rows.copy()
working_rows.pop(0)
products = []
for rows in working_rows:
    products.append((rows[0],(int(rows[1]) * int(rows[2]))))

products.sort(key=lambda x : x[1])



reportTxt = f'Highest Sales:-\n{products[-1][0]}: {products[-1][1]}\nLowest Sales:-\n{products[0][0]}: {products[0][1]}\nproducts sold: {len(products)}'

with open(REPORTFILE, 'w', newline='') as report:
    report.write(reportTxt)

with open(OUTPUTCSV, 'w', newline="") as file:
    writer = csv.writer(file)
    writer.writerows(new_rows)

print("done!")