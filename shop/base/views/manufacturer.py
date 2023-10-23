from django.views.generic import ListView, DetailView

from base.models import Manufacturer


class ManufacturerDetailView(DetailView):
    model = Manufacturer


class ManufacturerList(ListView):
    model = Manufacturer

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['page_title'] = 'Manufacturer'
        return context

