# Generated by Django 4.0.3 on 2022-03-30 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trains', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestTrain',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('cost', models.CharField(max_length=255, null=True)),
            ],
        ),
    ]
