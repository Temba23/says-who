# Generated by Django 5.0.6 on 2024-07-11 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('says_who', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Life',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('life', models.IntegerField(max_length=2)),
            ],
        ),
    ]
