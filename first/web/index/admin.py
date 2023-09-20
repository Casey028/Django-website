from django.contrib import admin
from .models import classform
from django.urls import path
from django.shortcuts import render
from django import forms
from .models import classform2

# Register your models here.
class CsvImportForm(forms.Form):
    csv_upload=forms.FileField()

class ClassformAdmin(admin.ModelAdmin):
    list_display=('Name','StuID','Email','Mon','Tue','Wed','Thu','Fri')
    
    def get_urls(self):
        urls=super().get_urls()
        new_urls=[path('upload-csv/',self.upload_csv),]
        return new_urls+urls
    def upload_csv(self,request):
        if request.method == "POST":
            csv_file = request.FILES["csv_upload"]
            file_data = csv_file.read().decode("utf-8")
            csv_data = file_data.splitlines()

            for x in csv_data:
                fields = x.split(",")
                created = classform.objects.update_or_create(
                    Name=fields[0],
                    StuID=fields[1],
                    Email=fields[2],
                    Mon=fields[3],
                    Tue=fields[4],
                    Wed=fields[5],
                    Thu=fields[6],
                    Fri=fields[7],
                )
        form = CsvImportForm()
        data = {"form":form}
        return render(request,"admin/csv_upload.html",data)

admin.site.register(classform,ClassformAdmin)
admin.site.register(classform2,ClassformAdmin)