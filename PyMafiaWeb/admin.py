from django.contrib import admin
from pymafia.models import Action, Character, Classification, Game, Skill

admin.site.register(Game)
admin.site.register(Character)
admin.site.register(Action)
admin.site.register(Classification)
admin.site.register(Skill)
