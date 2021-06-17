from django.forms import ModelForm, CheckboxSelectMultiple
from .models import Property, PropertyType, SubPropertyType, Search
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class SearchForm(ModelForm):
    class Meta:
        model = Property
        fields = ('City', 'PropertyType', 'SubType', 'MaxPrice', 'MinPrice')

    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        self.fields['PropertyType'].widget.attrs = {'class': 'select single-select mr-5', }
        self.fields['SubType'].widget.attrs = {'class': 'select single-select mr-5', }
        self.fields['City'].widget.attrs = {'class': 'select single-select mr-5', }
        # self.fields['MaxPrice'].widget.attrs = {'class': '', }
        # self.fields['MinPrice'].widget.attrs = {'class': '', }
        self.fields['SubType'].queryset = SubPropertyType.objects.none()

        if 'PropertyType' in self.data:
            try:
                PropertyType_id = int(self.data.get('PropertyType'))
                self.fields['SubType'].queryset = SubPropertyType.objects.filter(
                    PropertyType_id=PropertyType_id).order_by('name')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['SubType'].queryset = self.instance.PropertyType.SubType_set.order_by('name')


class SearchWebForm(ModelForm):
    class Meta:
        model = Search
        fields = ('City', 'Type', 'Subtype', 'MaxPrice', 'MinPrice')

    def __init__(self, *args, **kwargs):
        super(SearchWebForm, self).__init__(*args, **kwargs)
        self.fields['MinPrice'].widget.attrs = {'class': 'area-filter filter-1 mb-0', 'placeholder': 'Minimum Price' }
        self.fields['MaxPrice'].widget.attrs = {'class': 'area-filter mb-0', 'placeholder': 'Maximum Price' }
        self.fields['Subtype'].queryset = SubPropertyType.objects.none()

        if 'Type' in self.data:
            try:
                PropertyType_id = int(self.data.get('Type'))
                self.fields['Subtype'].queryset = SubPropertyType.objects.filter(
                    PropertyType_id=PropertyType_id).order_by('name')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['Subtype'].queryset = self.instance.PropertyType.Subtype.order_by('name')


class AddPropertyForm(ModelForm):
    class Meta:
        model = Property
        exclude = ('Status', 'created_on', 'Featured', 'AddType', 'Amenities')
        widgets = {
            'Description': SummernoteWidget(),
        }
