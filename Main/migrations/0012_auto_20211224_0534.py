# Generated by Django 3.1.5 on 2021-12-24 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0011_auto_20211218_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='Image',
            field=models.ImageField(upload_to='pics/blog'),
        ),
        migrations.AlterField(
            model_name='client',
            name='Image',
            field=models.ImageField(upload_to='pics/client'),
        ),
        migrations.AlterField(
            model_name='service',
            name='Icon',
            field=models.ImageField(upload_to='pics/services'),
        ),
        migrations.AlterField(
            model_name='team',
            name='Photo',
            field=models.ImageField(upload_to='pics/teams'),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='Photo',
            field=models.ImageField(upload_to='pics/testimonial'),
        ),
    ]
