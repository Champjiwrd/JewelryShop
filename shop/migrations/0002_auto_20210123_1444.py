# Generated by Django 3.1.5 on 2021-01-23 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jewelry',
            name='jewelry_photo',
            field=models.ImageField(blank=True, null=True, upload_to='jewelryphoto'),
        ),
    ]
