# Generated by Django 3.1 on 2020-09-11 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_auto_20200830_0217'),
    ]

    operations = [
        migrations.AddField(
            model_name='replacement',
            name='oid',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='reset',
            name='oid',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='replacement',
            name='order_id',
            field=models.IntegerField(default='1111'),
        ),
    ]
