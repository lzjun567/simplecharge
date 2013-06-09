from django.contrib.admin.views.main import ChangeList

from django.db.models import Sum,Avg

from models import Charge

class TotalAveragesChangeList(ChangeList):
    fields_to_total = ['amount','total_sum',]

    def get_total_values(self,queryset):

        total = Charge()
        total.custom_alias_name = "Totals"

        for field in self.fields_to_total:
            setattr(total,field,queryset.aggregate(Sum(field)).items()[0][1])
        return total


    def get_average_values(self,queryset):
        average = Charge()
        average.custom_alias_name = "Average"

        for field in self.fields_to_total:
            setattr(average,field,queryset.aggregate(Avg(field)).items()[0][1])
        return average

    def get_results(self,request):

        super(TotalAveragesChangeList,self).get_result(request)
        total = self.get_total_values(self.query_set)
        average = self.get_average_values(self.query_set)

        len(self.result_list)

        self.result_list._result_cache.append(total)
        self.result_list._result_cache.append(average)

