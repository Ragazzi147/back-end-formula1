# Generated by Django 4.1.7 on 2023-03-27 12:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_rename_car_books_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='books',
            old_name='title',
            new_name='car',
        ),
    ]