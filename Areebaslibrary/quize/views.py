from django.shortcuts import render
from django.views.generic import (ListView,DetailView)
from .models import Topic,Blank , Nameoflist , ListSorting





def Topicdetail(request,pk):
    blanks = Blank.objects.filter(topic=pk)
    name = Topic.objects.filter(id=pk)
    for x in name:
    	print(x.topicname , "gtggggg")
    context = {'blanks':blanks,'topicnames':x.topicname}
    return render(request , 'quize/topic_detail.html',context)


# Create your views here.
class MCQSListView(ListView):
    model = Topic
    paginate_by = 6

    def get_queryset(self):
        return Topic.objects.all().order_by('topicname')
	# return render(request, 'quize/index.html')

class ListView(ListView):
    model = Nameoflist
    paginate_by = 6

    def get_queryset(self):
        return Nameoflist.objects.all().order_by('nameoflist')
def Sortinglist(request,pk):
    lists = ListSorting.objects.filter(listname=pk)
    context = {'lists':lists}
    return render(request , 'quize/list_detail.html',context)