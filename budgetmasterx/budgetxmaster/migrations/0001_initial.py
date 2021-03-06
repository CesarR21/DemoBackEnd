# Generated by Django 3.2.8 on 2021-10-16 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.IntegerField(max_length=500)),
                ('Income', models.IntegerField(max_length=500)),
                ('expense', models.IntegerField(max_length=500)),
                ('date', models.DateField(max_length=500)),
                ('category', models.CharField(max_length=500)),
                ('amount', models.IntegerField(max_length=500)),
                ('Budget', models.IntegerField(max_length=500)),
                ('spent', models.IntegerField(max_length=500)),
            ],
        ),
    ]
