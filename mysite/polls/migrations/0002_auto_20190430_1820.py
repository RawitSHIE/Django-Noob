# Generated by Django 2.2 on 2019-04-30 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dayoff',
            name='date_end',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='dayoff',
            name='date_start',
            field=models.DateField(null=True),
        ),
    ]