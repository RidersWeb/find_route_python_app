from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse
from django.shortcuts import render
from cities.models import City
from cities.forms import HtmlForm, CityForm
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

__all__ = (
    'home', 'CityDetailView', 'CityCreateView', 'CityUpdateView', 'CityDeleteView', 'page'
)


def home(request, pk=None):
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
    # if pk:
    #     city = City.objects.filter(id=pk).first()
    #     context = {'object': city}
    #     return render(request, 'cities/detal.html', context)
    form = CityForm()
    qs = City.objects.all()
    context = {'objects_list': qs, 'form': form}
    return render(request, 'cities/home.html', context)

class CityDetailView(DetailView):
    queryset = City.objects.all()
    template_name = 'cities/detail.html'

class CityCreateView(CreateView):
    model = City
    form_class = CityForm
    template_name = 'cities/create.html'
    success_url = reverse_lazy('cities:home')

class CityUpdateView(SuccessMessageMixin, UpdateView):
    model = City
    form_class = CityForm
    template_name = 'cities/update.html'
    success_url = reverse_lazy('cities:home')
    success_message = "Город успешно отредактирован"

class CityDeleteView(SuccessMessageMixin, DeleteView):
    model = City
    template_name = 'cities/delete.html'
    success_url = reverse_lazy('cities:home')

# def page(request, page_num):
#         try:
#             num = int(page_num)
#             return HttpResponse(f'int page {page_num}')
#         except:
#             return HttpResponse('Страница 404 такой страницы не существует')

def page(request, page_num):
    return HttpResponse(f'page {page_num}')