# Generated by Django 4.0.2 on 2022-03-04 05:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_complains'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='digital',
        ),
    ]
