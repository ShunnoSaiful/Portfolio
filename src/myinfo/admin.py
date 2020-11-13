from django.contrib import admin
from .models import Home, SocialLink, About, TechnicalSkill, ProfessionalSkill, Education, Work, RecentPortfolio ,ClientReviews


# Register your models here.




class SocialLinkInline(admin.TabularInline):
    model = SocialLink
    extra = 3



class HomeAdmin(admin.ModelAdmin):
    inlines = [ SocialLinkInline]
    
admin.site.register(Home, HomeAdmin)