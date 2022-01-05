# Generated by Django 4.0 on 2021-12-16 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100, null=True)),
                ('Email', models.EmailField(max_length=254)),
                ('Address', models.TextField()),
            ],
        ),
    ]
