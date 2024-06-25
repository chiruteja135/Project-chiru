import csv

def read_csv_data(file_path):
    data = []
    with open(r'C:\Users\ycycr\project-chiru\tests\robot\students.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # Skip the header row
        for row in csv_reader:
            data.append(row)
    return data