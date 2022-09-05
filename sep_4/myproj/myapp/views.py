from multiprocessing import context
from re import template
from django.shortcuts import render

from django.views.generic.list import ListView
from .models import student

class studentListView(ListView):
    model=student
    template_name='school/student.html'
    context_object_name='students'
    def get_queryset(self):
        return student.objects.all()
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['freshers']=student.objects.all().order_by('name')
        return context

    def get_template_names(self):
        if self.request.user.is_staff:
            template_name='school/staff.html'
        elif self.request.user.is_staff:
            template_name='school/staff.html'
        else:
            template_name=self.template_name
        return[template_name]
    
        # stud=student.objects.all()
    # context={'student_list':stud}
    
    # return render(request,'school/student_list.html',context)


# Create your views here.
