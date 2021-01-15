import csv

print("Bounding Box results:")
with open('dataset/clasification_analises_bbs.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

print("Real Lesion Contours results:")        
with open('dataset/clasification_analises_bbs.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
