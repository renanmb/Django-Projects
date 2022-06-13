from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (TemplateView, FormView, CreateView, 
        ListView, DetailView, UpdateView, DeleteView)

from classroom.forms import ContactForm
from classroom.models import Teacher
# Create your views here.
def home_view(request):
    return render(request, 'classroom/home.html')

class HomeView(TemplateView):
    template_name = 'classroom/home.html'

class ThankYouView(TemplateView):
    template_name = 'classroom/thank_you.html'

class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'classroom/contact.html'

    # success URL ?
    success_url = "/classroom/thank_you/"

    # what to do with form ?
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class TeacherCreateView(CreateView):
    model = Teacher
    # model_form.html
    fields = "__all__"
    success_url= reverse_lazy('classroom:thank_you')

class TeacherListView(ListView):
    # look for the model_list.html
    model = Teacher
    # query allow to overide the query so can add filters and so on...
    queryset= Teacher.objects.order_by('first_name')

    context_object_name= "teacher_list"

class TeacherDetailView(DetailView):
    # model_detail.html
    model = Teacher
    # all detail view does is for a specific PK it sends back a context obejct
    # PK --> {{teacher}}

class TeacherUpdateView(UpdateView):
    # it will share the model form html that create view also uses
    #  model_form.html

    model = Teacher
    # with fields you can control what you want to update
    # fields = "__all__" # update all fields in the model
    # or it can be a list
    fields = "__all__"
    success_url = reverse_lazy('classroom:list_teacher')

class TeacherDeleteView(DeleteView):
    # Form --> Confirm Delete Button
    # default template name:
    # model_confirm_delete.html
    model = Teacher
    success_url = reverse_lazy('classroom:list_teacher')