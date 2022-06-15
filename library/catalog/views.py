from django import views
from django.shortcuts import render
from django.http import HttpResponse
from .models import Author,Genre,Language,Book,BookInstance
from django.views.generic import CreateView, DetailView, ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

# Create your views here.
def index(request):

    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    context= {
        'num_books':num_books,
        'num_instances':num_instances,
        'num_instances_available':num_instances_available,
    }

    return render(request,'catalog/index.html',context=context)

class BookCreate(LoginRequiredMixin,CreateView):
    # book_form.html
    model = Book
    fields = '__all__'

class BookDetail(DetailView):
    model = Book

@login_required
def my_view(request):
    return render(request, 'catalog/my_view.html')

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'catalog/signup.html'

class CheckedOutBooksByUserView(LoginRequiredMixin,ListView):
    # List of all BookInstances BUT filters based off curently logged in user session
    model = BookInstance
    template_name = 'catalog/profile.html'
    paginate_by = 5 # 5 book instances per page

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user)