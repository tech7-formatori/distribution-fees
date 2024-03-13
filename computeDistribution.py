import csv

def update_distribution(csv_filename, total_dollars, minimum_hours_eligibility):
    students = []
    total_hours = 0

    # Read the CSV file and calculate total hours
    with open(csv_filename, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            hours = float(row['Total Hours'])
            students.append({'Student Name': row['Student Name'], 'Total Hours': hours, 'Distribution ($)': 0})
            if hours >= minimum_hours_eligibility:
                total_hours += hours



    # Calculate the distribution and update the list
    for student in students:
        if student['Total Hours'] >= minimum_hours_eligibility:
            student['Distribution ($)'] = round((student['Total Hours'] / total_hours) * total_dollars, 2)

    # Update the CSV file with the new distribution
    with open(csv_filename, mode='w', newline='') as file:
        fieldnames = ['Student Name', 'Total Hours', 'Distribution ($)']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        writer.writeheader()
        writer.writerows(students)

    print("Updated distributions have been saved to the CSV file.")

# Example usage
if __name__ == "__main__":
    csv_filename = input("Enter the name of the CSV file: ")
    total_dollars = float(input("Enter the total dollar amount to distribute: "))
    minimum_hours_eligibility = float(input("Enter the minimum amount of hours of each student to be eligible:"))
    update_distribution(csv_filename, total_dollars, minimum_hours_eligibility)