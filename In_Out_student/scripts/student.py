from In_Out_student.models import Student
import csv


def run():
    with open('In_Out_student/student.csv') as file:
        reader = csv.reader(file)
        next(reader)  # Advance past the header

    
        Student.objects.all().delete()

        for row in reader:
            print(row)
            x = Student(name=row[0],aadhar_num=row[1],email_id=row[2],pswrd=row[4])
            x.save()