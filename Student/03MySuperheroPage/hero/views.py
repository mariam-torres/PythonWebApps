from django.views.generic import TemplateView


class HulkView(TemplateView):
    template_name = 'hero.html'