# Generated by Django 2.2.7 on 2020-03-22 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('count', models.IntegerField(verbose_name='count')),
                ('price', models.FloatField(verbose_name='price')),
                ('image', models.FileField(upload_to='', verbose_name='image')),
                ('company_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Company', verbose_name='company')),
            ],
        ),
    ]
