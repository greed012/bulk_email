# Generated by Django 3.1 on 2020-08-11 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bulksms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bulkmsg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=25)),
                ('receiver', models.EmailField(max_length=254)),
                ('msg', models.CharField(max_length=10000)),
            ],
        ),
        migrations.DeleteModel(
            name='Bulk',
        ),
    ]
