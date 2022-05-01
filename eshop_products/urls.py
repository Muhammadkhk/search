from django.urls import path
#from jmespath import search

from .views import ProductsList, SearchProductsView,SearchData

urlpatterns = [
    path('products', ProductsList.as_view()),
    path('products/search', SearchProductsView.as_view(),name='search'),
    path('search/', SearchData.as_view()),
]
