# Generated by Django 3.1.5 on 2021-01-23 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jewelry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jewelry_name', models.CharField(blank=True, max_length=200, null=True)),
                ('jewelry_photo', models.ImageField(blank=True, null=True, upload_to=None)),
                ('jewelry_about', models.TextField(blank=True, null=True)),
                ('jewelry_price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
