# Generated by Django 2.2.3 on 2019-07-22 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0006_services_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='image',
            field=models.ImageField(default='background.jpg', upload_to='services/static/testimage'),
        ),
    ]