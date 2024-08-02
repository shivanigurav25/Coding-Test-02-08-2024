import csv


# Specify the path to your CSV file
file_path = 'C:/Users/Dell/OneDrive/Desktop/Python Code/Python Coding Test/Details.csv'

try:
    # Open and read the CSV file
    with open(file_path, mode='r') as csvfile:
        csvreader = csv.reader(csvfile)
        
        # Read and print each row
        for row in csvreader:
            print(row)
except FileNotFoundError:
    print(f"The file {file_path} does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")




#Output
#['Name', 'Surname', 'Age', 'Salary']
#['Shivani', 'Gurav', '25', '40000']
#['Sharyu', 'Gurav', '21', '42000']
#['Ankita', 'Prabhu', '28', '45000']
#['Gurunath', 'Pawar', '26', '35000']
#['Akshay', 'Hatpale', '27', '31000']

