#!/usr/bin/env python 
#encoding:utf-8
from django.db import models
from datetime import datetime
from django.contrib import admin
from django.contrib.admin import DateFieldListFilter
from django.contrib.admin.views.main import ChangeList
from django.db.models import Sum,Avg
from django.contrib.auth.models import User
#from mychangelist import TotalAveragesChangeList
# Create your models here.

class Charge(models.Model):
    amount = models.DecimalField(max_digits=3,decimal_places=1,\
    verbose_name=u"消费金额",default=0)
    usage = models.CharField(max_length=50,default=u"吃饭",\
    verbose_name=u"用途")
    add_date = models.DateTimeField(default=datetime.now(),verbose_name=u"添加日期")
    owner = models.ForeignKey(User)




class ChargeAdmin(admin.ModelAdmin):
    exclude = ('owner',)
    list_display = ('owner','amount','usage','add_date')
    search_fields = ('usage',)
    list_filter  = (('add_date',DateFieldListFilter),)

    def save_model(self,request,charge,form,change):
       charge.owner = request.user
       charge.save()
    #change_list_template = 'extras/change_form.html'

   # def get_changelist(self,request,**kwarge):
   #     return TotalAveragesChangeList



admin.site.register(Charge,ChargeAdmin)






    
