from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView,TemplateView
from .models import LearningCourse
from django.urls import reverse_lazy
import datetime
# Create your views here.
class CourseList(ListView):
    model = LearningCourse
    queryset = LearningCourse.objects.order_by('title')
    def get_context_data(self, **kwargs):
          context = super().get_context_data(**kwargs)
          context['today'] = datetime.date.today()
          return context
    
    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')  # 获取搜索关键字
        if query:
            queryset = queryset.filter(title__icontains=query)  # 按标题模糊搜索
        return queryset

    template_name='employee_learning/course_list.html'
    context_object_name='course_object_list'

class CourseDetail(DetailView):
    model = LearningCourse
    template_name='employee_learning/course_detail.html'
    context_object_name='course_object'

class CourseCreate(CreateView):
    model = LearningCourse
    template_name='employee_learning/course_create.html'
    fields=('title','level','employee')
    success_url=reverse_lazy('course_list')

class CourseUpdate(UpdateView):
    model = LearningCourse
    template_name="employee_learning/course_update.html"
    fields=('title','level','employee')
    success_url=reverse_lazy('course_list')

class CourseDelete(DeleteView):
    model = LearningCourse
    template_name="employee_learning/course_delete.html"
    success_url=reverse_lazy('course_list')
    
class Index(TemplateView):
    template_name = 'employee_learning/index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['today'] = datetime.date.today()
        return context
