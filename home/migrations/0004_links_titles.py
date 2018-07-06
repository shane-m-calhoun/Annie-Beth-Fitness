# Generated by Django 2.0.2 on 2018-02-26 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20180226_0206'),
    ]

    operations = [
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=100, unique=True)),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('text', models.TextField()),
                ('link', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Titles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=100, unique=True)),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('text', models.TextField()),
            ],
        ),
    ]