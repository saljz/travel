# Generated by Django 4.2.8 on 2023-12-30 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mydgapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('img', models.ImageField(upload_to='teampic')),
                ('desc', models.TextField()),
            ],
        ),
    ]