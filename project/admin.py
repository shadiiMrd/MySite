from django.contrib import admin
from django_jalali.admin.filters import JDateFieldListFilter
from django_jalali.admin.widgets import AdminjDateWidget
from django_jalali.db import models as jmodels
import django_jalali.admin as jadmin  # noqa

from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'status', 'get_persian_date', 'sort')
    list_filter = (
        ('date', JDateFieldListFilter),
        'type',
        'status',
    )
    search_fields = ('name',)
    ordering = ('sort', '-date')

    formfield_overrides = {
        jmodels.jDateField: {'widget': AdminjDateWidget},
    }