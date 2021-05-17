# Generated by Django 3.1.2 on 2021-05-17 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Administrator',
            },
        ),
        migrations.CreateModel(
            name='bookdetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookname', models.CharField(max_length=100, null=True)),
                ('author', models.CharField(max_length=100, null=True)),
                ('year', models.CharField(max_length=1000, null=True)),
                ('publisher', models.CharField(max_length=200, null=True)),
                ('pdf', models.FileField(upload_to='books/pdfs/')),
            ],
            options={
                'db_table': 'Book Table',
            },
        ),
    ]
