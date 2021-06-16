# Generated by Django 3.2 on 2021-06-16 18:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_property_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='Title',
            field=models.CharField(max_length=30, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='search',
            name='City',
            field=models.ForeignKey(default='Select City', null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.city'),
        ),
    ]