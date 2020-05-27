from django.contrib import admin

from quize.models import Topic , Blank ,Nameoflist ,ListSorting


admin.site.register(Nameoflist)#, NameoflistA)
admin.site.register(ListSorting)#, ListSortingA
admin.site.register(Topic )#, TopicA)
admin.site.register(Blank )#, BlankA)