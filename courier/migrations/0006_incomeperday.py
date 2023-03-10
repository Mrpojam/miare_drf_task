# Generated by Django 4.1.5 on 2023-01-11 21:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courier', '0005_income_delete_dayincome'),
    ]

    operations = [
        migrations.CreateModel(
            name='IncomePerDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('value', models.BigIntegerField()),
                ('courier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courier.courier')),
            ],
        ),
    ]
