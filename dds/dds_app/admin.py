from django import forms
from django.contrib import admin
from rangefilter.filters import DateRangeFilter
from .models import Status, Type, Category, Subcategory, DDS

admin.site.register(Status)
admin.site.register(Type)
admin.site.register(Category)
admin.site.register(Subcategory)

class DDSAdminForm(forms.ModelForm):
    class Meta:
        model = DDS
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        type_id = None
        category_id = None

        if self.data.get('type'):
            try:
                type_id = int(self.data.get('type'))
            except (ValueError, TypeError):
                pass

        if self.data.get('category'):
            try:
                category_id = int(self.data.get('category'))
            except (ValueError, TypeError):
                pass

        if self.instance.pk and not self.data:
            type_id = self.instance.type_id
            category_id = self.instance.category_id

        if type_id:
            self.fields['category'].queryset = Category.objects.filter(type_id=type_id)
            if self.instance.pk and self.instance.category_id:
                self.fields['category'].initial = self.instance.category_id
        else:
            self.fields['category'].queryset = Category.objects.all()

        if category_id:
            self.fields['subcategory'].queryset = Subcategory.objects.filter(category_id=category_id)
            if self.instance.pk and self.instance.subcategory_id:
                self.fields['subcategory'].initial = self.instance.subcategory_id
        elif type_id and not category_id:
            categories = Category.objects.filter(type_id=type_id).values_list('id', flat=True)
            self.fields['subcategory'].queryset = Subcategory.objects.filter(category_id__in=categories)
        else:
            self.fields['subcategory'].queryset = Subcategory.objects.all()

        self.fields['type'].widget.attrs.update({
            'data-type-id': self.instance.type_id if self.instance.pk else ''
        })
        self.fields['category'].widget.attrs.update({
            'data-category-id': self.instance.category_id if self.instance.pk else ''
        })


@admin.register(DDS)
class DDSAdmin(admin.ModelAdmin):
    form = DDSAdminForm
    list_display = ['date_create', 'status', 'type', 'category', 'subcategory', 'sum', 'comment']
    list_filter = [
        ('date_create', DateRangeFilter),
        'status',
        'type__name',
        'category__name',
        'subcategory__name'
    ]

    class Media:
        js = ('admin/js/jquery.init.js', 'dds_app/js/dds_admin.js',)