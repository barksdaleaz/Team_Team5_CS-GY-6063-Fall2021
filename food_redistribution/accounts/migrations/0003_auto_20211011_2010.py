# Generated by Django 3.2.7 on 2021-10-12 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20211011_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='email',
            field=models.CharField(default=None, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='name_of_restaurant',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]
