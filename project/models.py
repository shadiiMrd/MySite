from django.db import models
from django_jalali.db import models as jmodels
import jdatetime
import re


class Project(models.Model):
    EMPLOYER_CHOICES = (
        ('پروژه شخصی / نمونه کار', 'پروژه شخصی / نمونه کار'),
    )
    PROJECT_TYPE_CHOICES = (
        ('django', 'Django'),
        ('wordpress', 'WordPress'),
    )
    PROJECT_STATUS = (
        ('در حال انجام', 'در حال انجام'),
        ('تکمیل شده', 'تکمیل شده'),
    )

    PERSIAN_MONTHS = {
        1: 'فروردین', 2: 'اردیبهشت', 3: 'خرداد', 4: 'تیر',
        5: 'مرداد', 6: 'شهریور', 7: 'مهر', 8: 'آبان',
        9: 'آذر', 10: 'دی', 11: 'بهمن', 12: 'اسفند',
    }

    name = models.CharField(max_length=100)
    employer = models.CharField(choices=EMPLOYER_CHOICES, max_length=50)
    type = models.CharField(choices=PROJECT_TYPE_CHOICES, max_length=50)
    date = jmodels.jDateField(default=jdatetime.date.today)
    short_description = models.TextField(max_length=500)
    full_description = models.TextField(max_length=1000)
    github_url = models.URLField(blank=True, null=True)
    poster_image = models.FileField(upload_to='project/photo', default='project/photos/poster.jfif',
                                    blank=True, null=True)
    video_file = models.FileField(upload_to='project/videos/', blank=True, null=True)
    aparat_url = models.URLField('لینک ویدیو در آپارات', blank=True)

    sort = models.IntegerField(default=0)
    status = models.CharField(choices=PROJECT_STATUS, max_length=50, default='در حال انجام')

    def __str__(self):
        return self.name

    def get_persian_date(self):
        """خروجی: آذر 1404"""
        if not self.date:
            return ''
        return f"{self.PERSIAN_MONTHS[self.date.month]} {self.date.year}"

    get_persian_date.short_description = 'تاریخ'

    @property
    def aparat_embed_url(self):
        match = re.search(r'aparat\.com/v/([A-Za-z0-9]+)', self.aparat_url or '')
        if not match:
            return ''
        return f'https://www.aparat.com/video/video/embed/videohash/{match.group(1)}/vt/frame'

    class Meta:
        verbose_name = 'پروژه'
        verbose_name_plural = 'پروژه ها'