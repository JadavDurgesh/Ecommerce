# Generated by Django 3.2.8 on 2022-03-01 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20220301_1116'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usr', models.CharField(max_length=100)),
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('number', models.IntegerField()),
            ],
        ),
    ]