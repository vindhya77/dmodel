# Generated by Django 2.2.7 on 2019-12-27 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('rollnum', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('add', models.CharField(max_length=100)),
            ],
        ),
    ]
