from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'heroes.html'


class HulkView(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'Hulk',
            'body': 'My name is Bruce Banner',
            'image': '/static/images/hulk.jpg'
        }


class IronManView(TemplateView):
    template_name = "hero.html"

    def get_context_data(self, **kwargs):
        return {
            'title': 'Iron Man',
            'body': 'My name is Tony Stark, but I am Iron Man',
            'image': '/static/images/iron_man.jpg'
        }


class BlackWidow(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'Black Widow',
            'body': 'My name is Natasha Romanova',
            'image': '/static/images/black_widow.jpg'
        }

class SpiderManView(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'Spider-Man',
            'body': 'My name is Peter Parker',
            'image': '/static/images/spiderman.jpg'
        }
    
class ScarletWitchView(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'Scarlet Witch',
            'body': 'My name is Wanda Maximoff',
            'image': '/static/images/wanda.jpg'
        }    