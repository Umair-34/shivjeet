from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.urls import reverse

from core.choices import ADD_TYPE_CHOICES


# Create your models here.
class City(models.Model):
    Name = models.CharField(max_length=256, verbose_name='Region Name')

    def __str__(self):
        return f'{self.Name}'

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'


class Region(models.Model):
    City = models.ForeignKey(City, on_delete=models.CASCADE)
    Name = models.CharField(max_length=512, verbose_name='City Name')

    def __str__(self):
        return f'{self.Name}'

    class Meta:
        verbose_name = 'Region'
        verbose_name_plural = 'Regions'


class Amenities(models.Model):
    Name = models.CharField(max_length=512, null=True, blank=True)

    def __str__(self):
        return f'{self.Name}'

    class Meta:
        verbose_name = 'Amenity'
        verbose_name_plural = 'Amenities'


class PropertyType(models.Model):
    name = models.CharField(max_length=512, verbose_name="Property Type")

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Property Type'
        verbose_name_plural = 'Property Type'


class SubPropertyType(models.Model):
    PropertyType = models.ForeignKey(PropertyType, on_delete=models.CASCADE)
    name = models.CharField(max_length=256, verbose_name="Property Sub-Category")

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Sub-Property Type'
        verbose_name_plural = 'Sub-Property Type'


class AreaUnit(models.Model):
    Unit = models.CharField(max_length=126)

    def __str__(self):
        return f'{self.Unit}'

    class Meta:
        verbose_name = 'Area Unit'
        verbose_name_plural = 'Area Unit'


class Search(models.Model):
    City = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    Type = models.ForeignKey(PropertyType, on_delete=models.SET_NULL, null=True)
    Subtype = models.ForeignKey(SubPropertyType, on_delete=models.SET_NULL, null=True)
    MaxPrice = models.DecimalField(decimal_places=2, max_digits=27, verbose_name="Maximum Price")
    MinPrice = models.DecimalField(decimal_places=2, max_digits=27, verbose_name="Minimum Price")


class Property(models.Model):
    UploaderName = models.CharField(max_length=512, verbose_name="Seller Name")
    UploaderNumber = PhoneNumberField(verbose_name="Seller Contact No")
    UploaderAddress = models.CharField(max_length=256, verbose_name="Seller Address")
    UploaderEmail = models.EmailField(verbose_name="Seller Email")
    UploaderZip = models.CharField(max_length=12, verbose_name=" Seller Zip Code")

    Title = models.CharField(max_length=30, verbose_name="Title")
    PropertyType = models.ForeignKey(PropertyType, on_delete=models.SET_NULL, null=True)
    SubType = models.ForeignKey(SubPropertyType, on_delete=models.SET_NULL, null=True)
    Address = models.CharField(max_length=420)
    City = models.ForeignKey(City, on_delete=models.CASCADE, default=0)
    Region = models.ForeignKey(Region, on_delete=models.CASCADE, default=0)
    Zipcode = models.CharField(max_length=12, verbose_name="Zip Code")
    Description = models.TextField()

    Beds = models.PositiveIntegerField(null=True, blank=True)
    Baths = models.PositiveIntegerField(null=True, blank=True)
    kitchen = models.PositiveIntegerField(null=True, blank=True)
    garage = models.BooleanField(default=False, verbose_name="Garage")

    AddType = models.CharField(max_length=128, choices=ADD_TYPE_CHOICES, verbose_name="For")

    Area = models.DecimalField(decimal_places=2, max_digits=17)
    Areaunit = models.ForeignKey(AreaUnit, on_delete=models.SET_NULL, null=True)
    MinPrice = models.DecimalField(decimal_places=2, max_digits=27, verbose_name="Minimum Price")
    MaxPrice = models.DecimalField(decimal_places=2, max_digits=27, verbose_name="Maximum Price")
    Amenities = models.ManyToManyField(Amenities)

    Status = models.BooleanField(default=False, verbose_name='Approved?')
    created_on = models.DateTimeField(auto_now=True, null=False)
    Featured = models.BooleanField(default=False)

    BannerImage = models.ImageField(upload_to='PropertyPhotos/%Y/%m/%d')
    image1 = models.ImageField(upload_to='PropertyPhotos/%Y/%m/%d')
    image2 = models.ImageField(upload_to='PropertyPhotos/%Y/%m/%d', null=True, blank=True)
    image3 = models.ImageField(upload_to='PropertyPhotos/%Y/%m/%d', null=True, blank=True)
    image4 = models.ImageField(upload_to='PropertyPhotos/%Y/%m/%d', null=True, blank=True)
    image5 = models.ImageField(upload_to='PropertyPhotos/%Y/%m/%d', null=True, blank=True)

    def __str__(self):
        return f'{self.Address}{self.Status}{self.created_on}'

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])

    class Meta:
        verbose_name = 'Property'
        verbose_name_plural = 'Properties'
