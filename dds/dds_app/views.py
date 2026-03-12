from rest_framework import viewsets
from .serializer import StatusSerializer, TypeSerializer, CategorySerializer, SubcategorySerializer, DDSSerializer
from .models import Status, Type, Category, Subcategory, DDS
from django.http import JsonResponse
from django.contrib.admin.views.decorators import staff_member_required

class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


class TypeViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SubcategoryViewSet(viewsets.ModelViewSet):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer


class DDSViewSet(viewsets.ModelViewSet):
    queryset = DDS.objects.all()
    serializer_class = DDSSerializer

@staff_member_required
def get_categories(request):
    type_id = request.GET.get('type_id')
    if type_id:
        categories = Category.objects.filter(type_id=type_id).values('id', 'name')
        return JsonResponse(list(categories), safe=False)
    return JsonResponse([], safe=False)

@staff_member_required
def get_subcategories(request):
    category_id = request.GET.get('category_id')
    if category_id:
        subcategories = Subcategory.objects.filter(category_id=category_id).values('id', 'name')
        return JsonResponse(list(subcategories), safe=False)
    return JsonResponse([], safe=False)
