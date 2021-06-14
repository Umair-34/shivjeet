# Generated by Django 3.2 on 2021-06-10 13:09

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Amenities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=512, null=True)),
            ],
            options={
                'verbose_name': 'Amenity',
                'verbose_name_plural': 'Amenities',
            },
        ),
        migrations.CreateModel(
            name='AreaUnit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Unit', models.CharField(max_length=126)),
            ],
            options={
                'verbose_name': 'Area Unit',
                'verbose_name_plural': 'Area Unit',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=256, verbose_name='Region Name')),
            ],
            options={
                'verbose_name': 'City',
                'verbose_name_plural': 'Cities',
            },
        ),
        migrations.CreateModel(
            name='PropertyType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512, verbose_name='Property Type')),
            ],
            options={
                'verbose_name': 'Property Type',
                'verbose_name_plural': 'Property Type',
            },
        ),
        migrations.CreateModel(
            name='SubPropertyType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Property Sub-Category')),
                ('PropertyType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.propertytype')),
            ],
            options={
                'verbose_name': 'Sub-Property Type',
                'verbose_name_plural': 'Sub-Property Type',
            },
        ),
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MaxPrice', models.DecimalField(decimal_places=2, max_digits=27, verbose_name='Maximum Price')),
                ('MinPrice', models.DecimalField(decimal_places=2, max_digits=27, verbose_name='Minimum Price')),
                ('City', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.city')),
                ('Subtype', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.subpropertytype')),
                ('Type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.propertytype')),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=512, verbose_name='City Name')),
                ('City', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.city')),
            ],
            options={
                'verbose_name': 'Region',
                'verbose_name_plural': 'Regions',
            },
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UploaderName', models.CharField(max_length=512, verbose_name='Seller Name')),
                ('UploaderNumber', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='Seller Contact No')),
                ('UploaderAddress', models.CharField(max_length=256, verbose_name='Seller Address')),
                ('UploaderEmail', models.EmailField(max_length=254, verbose_name='Seller Email')),
                ('UploaderZip', models.CharField(max_length=12, verbose_name=' Seller Zip Code')),
                ('Address', models.CharField(max_length=420)),
                ('Zipcode', models.CharField(max_length=12, verbose_name='Zip Code')),
                ('Description', models.TextField()),
                ('Beds', models.PositiveIntegerField(blank=True, null=True)),
                ('Baths', models.PositiveIntegerField(blank=True, null=True)),
                ('kitchen', models.PositiveIntegerField(blank=True, null=True)),
                ('garage', models.BooleanField(default=False, verbose_name='Garage')),
                ('AddType', models.CharField(choices=[('Sell', 'Sell'), ('Rent', 'Rent'), ('Investment Opportunity', 'Investment Opportunity')], max_length=128, verbose_name='For')),
                ('Area', models.DecimalField(decimal_places=2, max_digits=17)),
                ('MinPrice', models.DecimalField(decimal_places=2, max_digits=27, verbose_name='Minimum Price')),
                ('MaxPrice', models.DecimalField(decimal_places=2, max_digits=27, verbose_name='Maximum Price')),
                ('Status', models.BooleanField(default=False, verbose_name='Approved?')),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('Featured', models.BooleanField(default=False)),
                ('BannerImage', models.ImageField(upload_to='PropertyPhotos/%Y/%m/%d')),
                ('image1', models.ImageField(upload_to='PropertyPhotos/%Y/%m/%d')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='PropertyPhotos/%Y/%m/%d')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='PropertyPhotos/%Y/%m/%d')),
                ('image4', models.ImageField(blank=True, null=True, upload_to='PropertyPhotos/%Y/%m/%d')),
                ('image5', models.ImageField(blank=True, null=True, upload_to='PropertyPhotos/%Y/%m/%d')),
                ('Amenities', models.ManyToManyField(to='core.Amenities')),
                ('Areaunit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.areaunit')),
                ('City', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='core.city')),
                ('PropertyType', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.propertytype')),
                ('Region', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='core.region')),
                ('SubType', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.subpropertytype')),
            ],
            options={
                'verbose_name': 'Property',
                'verbose_name_plural': 'Properties',
            },
        ),
    ]
