# Generated by Django 4.0.6 on 2022-12-03 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_alter_student_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_image',
            field=models.ImageField(upload_to='student\\images'),
        ),
    ]