# Generated by Django 3.2.10 on 2022-07-19 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TeamsApp', '0007_auto_20220719_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archivedb',
            name='END',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='archivedb',
            name='START',
            field=models.DateField(),
        ),
    ]