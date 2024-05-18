from django.contrib import admin
from .models import Question, Choice

admin.site.site_header="The Voting Sysytem"
admin.site.site_title="Voting Admin"
admin.site.index_title="Welcome to our Voting Site"

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets =[(None,{'fields':['ques_head']}),('Description',{'fields':['description']}),('Voters List', {'fields':['voters_email', 'totalvotes'],}),('Date Information',{'fields':['pub_date'],'classes':['collapse']}),]
    inlines = [ChoiceInline]
   

admin.site.register(Question, QuestionAdmin)    



