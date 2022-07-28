# Generated by Django 4.0.5 on 2022-06-28 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='state',
            field=models.CharField(choices=[('Biratnagar', 'Biratnagar'), ('Kathmandu', 'Kathmandu'), ('Chitwan', 'Chitwan'), ('Bhairawa', 'Bhairawa'), ('Jhapa', 'Jhapa'), ('Pokhara', 'Pokhara'), ('Illam', 'Illam'), ('Sindhuli', 'Sindhuli'), ('Lalitpur', 'Lalitpur')], max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Banknotes', 'Banknotes'), ('Coins', 'Coins')], max_length=15),
        ),
    ]