from django.contrib import admin
from .models import Candidate, CandidatePreferences, CandidatePreferencesLocation

class CandidateAdmin(admin.ModelAdmin):
	exclude = ('password', 'last_login', 'is_admin',)

admin.site.register(Candidate, CandidateAdmin)

class CandidatePreferencesAdmin(admin.ModelAdmin):
	pass

admin.site.register(CandidatePreferences, CandidatePreferencesAdmin)