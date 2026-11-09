import django_filters
from django import forms

from project.models import *


class DateSelect(forms.Select):
    def __init__(self, *args, **kwargs):
        attrs = kwargs.pop('attrs', {})
        attrs.update({'class': 'form-control'})
        super().__init__(*args, attrs=attrs, **kwargs)


class ProjectFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(field_name='name', method='name_search')
    type = django_filters.ChoiceFilter(field_name='type', choices=Project.PROJECT_TYPE_CHOICES)
    date_sort = django_filters.OrderingFilter(choices=(
        ('-date', 'جدیدترین'),
        ('date', 'قدیمی‌ترین'),
    ), widget=DateSelect)

    class Meta:
        model = Project
        fields = ('name', 'type',)

    def name_search(self, queryset, name, value):
        if value:
            return queryset.filter(name__icontains=value)
        return queryset
