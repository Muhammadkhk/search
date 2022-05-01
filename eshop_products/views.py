
import itertools
from django.views.generic import ListView
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from eshop_products.models import Product,Product1,Product2
from .serializers import ProductModelSerializer

# Create your views here.

class ProductsList(ListView):
    template_name = 'home/shop.html'
    paginate_by = 3

    def get_queryset(self):
        product = Product.objects.get_active_products()
        product1 = Product1.objects.get_active_products()
        product2 = Product2.objects.get_active_products()

        product3 = list(itertools.chain(product, product1, product2))
        return product3


class SearchProductsView(ListView):
    template_name = 'home/shop.html'
    paginate_by = 3
    def get_queryset(self):
        request = self.request
        print(request.GET)
        query = request.GET.get('q')
        if query is not None:
            product = Product.objects.search(query)
            product1 = Product1.objects.search(query)
            product2 = Product2.objects.search(query)
            product3 = list(itertools.chain(product, product1, product2))
            return product3

        product = Product.objects.get_active_products()
        product1 = Product1.objects.get_active_products()
        product2 = Product2.objects.get_active_products()

        product3 = list(itertools.chain(product, product1, product2))

        return product3

class SearchData(APIView):
    def  get(self,request):
        search = request.GET['brand']
        query = Product.objects.filter(brand__contains=search)
        serializers = ProductModelSerializer(query, many=True)
        list_id = []
        for i in serializers.data:
            list_id.append(i["id"])
        print(list_id)

        return Response(list_id, status=status.HTTP_200_OK)

