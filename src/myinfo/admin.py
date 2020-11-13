from django.contrib import admin
from .models import Home, SocialLink, Tag, About, TechnicalSkill, ProfessionalSkill, Education, Work, RecentPortfolio ,ClientReviews


# Register your models here.



class SocialLinkInline(admin.TabularInline):
    model = SocialLink
    extra = 3

class HomeAdmin(admin.ModelAdmin):
    inlines = [ SocialLinkInline]

class TagInline(admin.TabularInline):
    model = Tag
    extra = 3

class AboutAdmin(admin.ModelAdmin):
    inlines = [ TagInline]



admin.site.register(Home, HomeAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(TechnicalSkill)
admin.site.register(ProfessionalSkill)
admin.site.register(Education)
admin.site.register(Work)
admin.site.register(RecentPortfolio)
admin.site.register(ClientReviews)