# Generated by Django 4.1.7 on 2023-05-13 06:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('name_brand', models.CharField(max_length=50)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('NCC', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Warranty',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('MGD', models.CharField(max_length=10, unique=True)),
                ('name_KH', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=30)),
                ('ngaynhan', models.DateField()),
                ('ngaytra', models.DateField()),
                ('note', models.TextField(null=True)),
                ('phone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warranty.phone')),
            ],
        ),
    ]