# Generated by Django 2.0.2 on 2018-03-09 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buttons', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='index',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
