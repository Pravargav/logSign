from In_Out_staff.models import Staff
import csv


def run():
    with open('In_Out_staff/staff.csv') as file:
        reader = csv.reader(file)
        next(reader)  # Advance past the header

    
        Staff.objects.all().delete()

        for row in reader:
            print(row)
            x = Staff(name=row[0],aadhar_num=row[1],email_id=row[2],pswrd=row[4])
            x.save()