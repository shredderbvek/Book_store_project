# Generated by Django 3.1.2 on 2020-10-15 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20201015_1921'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinquiry',
            name='delivery_date',
        ),
    ]
