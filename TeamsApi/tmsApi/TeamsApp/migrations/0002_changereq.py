# Generated by Django 3.2.10 on 2022-06-13 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TeamsApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChangeReq',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('FNAME', models.CharField(max_length=500)),
                ('LNAME', models.CharField(max_length=500)),
                ('OLDTEAM', models.CharField(max_length=500)),
                ('NEWTEAM', models.CharField(max_length=500)),
                ('MANAGER', models.CharField(max_length=500)),
                ('COMMENTS', models.CharField(max_length=5000)),
                ('APPROVAL', models.IntegerField(max_length=10)),
            ],
        ),
    ]
