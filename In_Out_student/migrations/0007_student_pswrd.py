# Generated by Django 4.1.3 on 2023-01-23 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('In_Out_student', '0006_student_aadhar_num_student_email_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='pswrd',
            field=models.CharField(default='x', max_length=217),
        ),
    ]
