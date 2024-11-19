from django.core.management.base import BaseCommand
from requests import get

class Command(BaseCommand):

    def handle(self, *args, **options):

        pages = {
            "https://seal-app-v99by.ondigitalocean.app/",
            "https://seal-app-v99by.ondigitalocean.app/hero/",
            "https://seal-app-v99by.ondigitalocean.app/hero/add",
            "https://seal-app-v99by.ondigitalocean.app/reporter/",
            "https://seal-app-v99by.ondigitalocean.app/reporter/add",
            "https://seal-app-v99by.ondigitalocean.app/article/",
            "https://seal-app-v99by.ondigitalocean.app/article/add"
                }
        
        for page in pages:
            response = get(page)
            print(response.url + "   Expected Response: 200   Actual Response: " + str(response.status_code))