from pathlib import Path
from typing import Any, Dict
from django.shortcuts import render
from django.views.generic import TemplateView
import json

class HeroDetailView(TemplateView):
    template_name = "hero.html"

    def get_context_data(self, **kwargs):
        numID = kwargs["numID"]

        with open('./static/heroes.json') as f:
            jsonData = json.load(f)
        
        heroData = jsonData.get(numID)
        if not heroData:
            
            return {}

        context = {
            "title": heroData.get("title", "No Title"),
            "id": heroData.get("id", "No ID"),
            "strength1": heroData.get("strength1", ""),
            "strength2": heroData.get("strength2", ""),
            "strength3": heroData.get("strength3", ""),
            "weakness1": heroData.get("weakness1", ""),
            "weakness2": heroData.get("weakness2", ""),
            "weakness3": heroData.get("weakness3", ""),
            "imagePath": heroData.get("imagePath", ""),
            "photo": heroData.get("imagePath", "")
        }

        return context

class HeroListView(TemplateView):
    template_name = 'heroes.html'

    def get_context_data(self, **kwargs):
        with open('./static/heroes.json') as f:
            jsonData = json.load(f)

        heroes = []
        for key, hero in jsonData.items():
            heroes.append({
                'numID': key,
                'imagePath': hero.get("imagePath", ""),
                'title': hero.get("title", "No Title")
            })

        return {'heroes': heroes}