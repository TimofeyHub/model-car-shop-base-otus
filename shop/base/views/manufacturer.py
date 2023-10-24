from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from base.models import Manufacturer


class ManufacturerDetailView(DetailView):
    model = Manufacturer


class ManufacturerList(ListView):
    model = Manufacturer

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['page_title'] = 'Manufacturer'
        return context


class ManufacturerCreate(CreateView):
    model = Manufacturer
    fields = '__all__'
    success_url = reverse_lazy('base:manufacturer-index')
