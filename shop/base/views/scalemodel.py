from django.views.generic import ListView, CreateView, DetailView

from base.models import ScaleModel


class ScaleModelDetailView(DetailView):
    model = ScaleModel


class ScaleModelList(ListView):
    model = ScaleModel

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['page_title'] = 'Models'
        return context

