from django.contrib import admin
from .models import Home, SocialLink, Tag, About, TechnicalSkill, ProfessionalSkill, Education, Work, RecentPortfolio, RPTag, ClientReviews


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

class RPTagInline(admin.TabularInline):
    model = RPTag
    extra = 3

class RecentPortfolioAdmin(admin.ModelAdmin):
    inlines = [ RPTagInline]


admin.site.register(Home, HomeAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(TechnicalSkill)
admin.site.register(ProfessionalSkill)
admin.site.register(Education)
admin.site.register(Work)
admin.site.register(RecentPortfolio, RecentPortfolioAdmin)
admin.site.register(ClientReviews)