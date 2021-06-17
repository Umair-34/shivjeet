from django.shortcuts import render, redirect
from .forms import AddPropertyForm, SearchForm, SearchWebForm
from .models import Property, PropertyType, SubPropertyType
from htmllaundry import strip_markup


def index(request):
    queryset = Property.objects.filter(Featured='True', Status=True)[:3]
    if request.method == 'POST':
        webform = SearchWebForm(request.POST)
        print("-----In If-----")
        if webform.is_valid():
            webCity = webform.cleaned_data['City']
            webType = webform.cleaned_data['Type']
            webSubtype = webform.cleaned_data['Subtype']
            webMinPrice = webform.cleaned_data['MinPrice']
            webMaxPrice = webform.cleaned_data['MaxPrice']
            print('--------MinPrice-------->', webMinPrice, "---Type---", type(webMinPrice))

            request.session['city'] = webCity.id
            request.session['type'] = webType.id
            request.session['subtype'] = webSubtype.id
            request.session['minprice'] = str(webMinPrice)
            request.session['maxprice'] = str(webMaxPrice)
            return redirect('search')
    else:
        webform = SearchWebForm()

    context = {
        'obj': queryset,
        'webform': webform,
    }
    return render(request, 'core/index.html', context)


def search(request):
    city = request.session['city']
    type = request.session['type']
    subtype = request.session['subtype']
    minprice = request.session['minprice']
    maxprice = request.session['maxprice']

    min = float(minprice)
    max = float(maxprice)

    queryset = Property.objects.filter(City=city, PropertyType=type,
                                       SubType=subtype, MinPrice__gte=min, MaxPrice__lte=max)
    results = Property.objects.filter(City=city, PropertyType=type,
                                      SubType=subtype, MinPrice__gte=min, MaxPrice__lte=max).count()

    context = {
        'obj': queryset,
        'results': results,
    }
    return render(request, 'core/buy.html', context)


def add_property(request):
    queryset = PropertyType.objects.all()
    queryset2 = SubPropertyType.objects.all()
    if request.method == 'POST':
        form = AddPropertyForm(request.POST, request.FILES)

        if form.is_valid():
            temp = form.save()
            request.session['id'] = temp.id
            return redirect('preview-ad')
    else:
        form = AddPropertyForm()

    context = {
        'form': form,
    }
    return render(request, 'core/add-property.html', context)


def preview_ad(request):
    model_id = request.session['id']
    queryset = Property.objects.get(id=model_id)
    context = {
        'obj': queryset,
    }
    return render(request, 'core/preview.html', context)


def buy_property(request):
    queryset = Property.objects.filter(Status=True)
    results = Property.objects.filter(Status=True).count()

    if request.method == 'POST':
        webform = SearchForm(request.POST)
        if webform.is_valid():
            webCity = webform.cleaned_data['City']
            webType = webform.cleaned_data['Type']
            webSubtype = webform.cleaned_data['Subtype']
            webMinPrice = webform.cleaned_data['MinPrice']
            webMaxPrice = webform.cleaned_data['MaxPrice']
            print('--------MinPrice-------->', webMinPrice, "---Type---", type(webMinPrice))

            request.session['city'] = webCity.id
            request.session['type'] = webType.id
            request.session['subtype'] = webSubtype.id
            request.session['minprice'] = str(webMinPrice)
            request.session['maxprice'] = str(webMaxPrice)
            return redirect('search')
    else:
        webform = SearchForm()

    context = {
        'obj': queryset,
        'webform': webform,
        'results': results,
    }

    return render(request, 'core/buy.html', context)


def featured_properties(request):
    queryset = Property.objects.filter(Status=True, Featured=True)
    results = Property.objects.filter(Status=True, Featured=True).count()
    context = {
        'obj': queryset,
        'results': results,
    }
    return render(request, 'core/buy.html', context)


def detail_property(request, pk):
    queryset = Property.objects.get(id=pk)
    context = {
        'obj': queryset
    }
    return render(request, 'core/detail.html', context)


def load_subtypes(request):
    property_id = request.GET.get('country')
    cat = SubPropertyType.objects.filter(PropertyType_id=property_id).order_by('name')
    print(cat)
    return render(request, 'hr/SubType_dropdown.html', {'Subtype': cat})


def base(request):
    return render(request, 'base.html')
