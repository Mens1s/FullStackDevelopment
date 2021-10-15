# Generated by Django 3.2.7 on 2021-10-15 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20211014_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='balance',
            field=models.IntegerField(null=True, verbose_name='Balance : '),
        ),
        migrations.AlterField(
            model_name='customer',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Login Date : '),
        ),
        migrations.AlterField(
            model_name='customer',
            name='first_name',
            field=models.CharField(max_length=100, null=True, verbose_name='Name : '),
        ),
        migrations.AlterField(
            model_name='customer',
            name='last_name',
            field=models.CharField(max_length=100, null=True, verbose_name='Surname : '),
        ),
        migrations.AlterField(
            model_name='customer',
            name='password',
            field=models.CharField(max_length=100, null=True, verbose_name='Password : '),
        ),
        migrations.AlterField(
            model_name='customer',
            name='username',
            field=models.CharField(max_length=100, null=True, verbose_name='ID : '),
        ),
    ]