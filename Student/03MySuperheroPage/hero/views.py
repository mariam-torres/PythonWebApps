from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'heroes.html'

class SpidermanView(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'Spider-Man',
            'id': 'Peter Parker',
            'power1': 'Web Powers',
            'power2': 'Spidey Senses',
            'power3': 'Strength',
            'weakness1': 'His Naivete',
            'weakness2': 'Idealism and love for others',
            'weakness3': 'Ethyl Chloride Pesticide',
            'image': '/static/images/spiderman.jpg'
        }
    
class StormView(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'Storm',
            'id': 'Ororo Munroe',
            'power1': 'Weather Control',
            'power2': 'Solar Wind Manipulation',
            'power3': 'Strength',
            'weakness1': 'Claustrophobia',
            'weakness2': 'Cannot create unnatural atmospheric conditions',
            'weakness3': 'Emotions and willpower',
            'image': '/static/images/storm.jpg'
        }
    
class WandaView(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'Scarlet Witch',
            'id': 'Wanda Maximoff',
            'power1': 'Telekinesis',
            'power2': 'Energy Manipulation',
            'power3': 'Chaos Magic',
            'weakness1': 'Mental Stability',
            'weakness2': 'Physical Condition',
            'weakness3': 'Perception Range',
            'image': '/static/images/wanda.jpg'
        }
class X23View(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'X-23',
            'id': 'Laura Kinney',
            'power1': 'Regenerative healing',
            'power2': 'Adamantium Claws',
            'power3': 'Superhuman strength, durability, stamina',
            'weakness1': 'Trigger Scent',
            'weakness2': 'Heal Block',
            'weakness3': 'Critical Resistance',
            'image': '/static/images/x23.jpg'
        }    