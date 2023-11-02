from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from base.models import Scale


class ScaleList(ListView):
    model = Scale

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['page_title'] = 'Scale list'
        return context


class ScaleCreate(CreateView):
    model = Scale
    fields = '__all__'
    success_url = reverse_lazy('base:scale-index')
