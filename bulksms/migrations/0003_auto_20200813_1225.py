# Generated by Django 3.1 on 2020-08-13 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bulksms', '0002_auto_20200811_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bulkmsg',
            name='receiver',
            field=models.CharField(default=' ', max_length=100),
        ),
    ]