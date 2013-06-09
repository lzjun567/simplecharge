#!/usr/bin/env python 
#encoding:utf-8
from django.db import models
from datetime import datetime
from django.contrib import admin
from django.contrib.admin import DateFieldListFilter
from django.contrib.admin.views.main import ChangeList
from django.db.models import Sum,Avg
from mychangelist import TotalAveragesChangeList
# Create your models here.

class Charge(models.Model):
    amount = models.DecimalField(max_digits=3,decimal_places=1,\
    verbose_name=u"消费金额",default=0)
    usage = models.CharField(max_length=50,default=u"吃饭",\
    verbose_name=u"用途")
    add_date = models.DateTimeField(default=datetime.now(),verbose_name=u"添加日期")



class ChargeAdmin(admin.ModelAdmin):
    list_display = ('amount','usage','add_date')
    search_fields = ('usage',)
    list_filter  = (('add_date',DateFieldListFilter),)
    #change_list_template = 'extras/change_form.html'

    def get_changelist(self,request,**kwarge):
        return TotalAveragesChangeList



admin.site.register(Charge,ChargeAdmin)






    
