from django.urls import path
from .views import index, add_property, preview_ad, buy_property, featured_properties, detail_property, \
    load_subtypes

urlpatterns = [
    path('', index, name='home'),
    path('add-property', add_property, name='add-property'),
    path('preview-ad', preview_ad, name='preview-ad'),
    path('buy', buy_property, name='buy'),
    path('featured-properties', featured_properties, name='featured'),
    path('detail/<int:pk>/', detail_property, name='detail'),
    path('ajax/load-sub-types/', load_subtypes, name='ajax_load_subtypes'),
]
