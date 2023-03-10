# Generated by Django 3.2.5 on 2023-01-11 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courier',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=160)),
                ('last_name', models.CharField(max_length=160)),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateTimeField()),
                ('income', models.BigIntegerField()),
                ('courier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courier.courier')),
            ],
            options={
                'ordering': ['Date', 'courier'],
            },
        ),
    ]
