# Generated by Django 4.0 on 2022-03-19 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='classform2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('StuID', models.CharField(max_length=30)),
                ('Email', models.CharField(max_length=30)),
                ('Mon', models.TextField()),
                ('Tue', models.TextField()),
                ('Wed', models.TextField()),
                ('Thu', models.TextField()),
                ('Fri', models.TextField()),
            ],
        ),
    ]
