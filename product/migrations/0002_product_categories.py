# Generated by Django 2.2.7 on 2020-03-24 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='categories',
            field=models.CharField(default='game present gift', max_length=400),
            preserve_default=False,
        ),
    ]
