# Generated by Django 2.0 on 2018-01-25 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attraction',
            fields=[
                ('attractionId', models.AutoField(primary_key=True, serialize=False)),
                ('provinceId', models.IntegerField()),
                ('clusterId', models.IntegerField()),
                ('description', models.TextField(null=True)),
            ],
            options={
                'db_table': 'attraction',
            },
        ),
    ]
