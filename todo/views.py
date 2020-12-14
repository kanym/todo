from django.views.generic import ListView, DetailView
from .models import  ListPage
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

class TodoListView(ListView):
    model = ListPage
    template_name = "home.html"
 

class TodoCreateView(CreateView):
    model = ListPage
    template_name = "create.html"
    fields = "__all__"
    success_url = reverse_lazy("home")

class TodoUpdateView(UpdateView):
    model = ListPage
    template_name = "update.html"
    fields = ["title","body"]
    success_url = reverse_lazy("home")


class TodoDeleteView(DeleteView):
    model = ListPage
    template_name = "delete.html"
    fields = "__all__"
    success_url = reverse_lazy("home")