# Generated by Django 2.0.2 on 2018-02-26 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20180226_2157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='text',
            field=models.CharField(max_length=1000),
        ),
    ]
