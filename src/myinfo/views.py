from django.shortcuts import render,  get_object_or_404, redirect
from .models import Home, SocialLink, Tag, RPTag, About, TechnicalSkill, ProfessionalSkill, Education, Work, RecentPortfolio ,ClientReviews
from blog.models import BlogPost




def home(request):
	home = Home.objects.all()
	social_link = SocialLink.objects.all()
	about = About.objects.all()[:1]
	about2 = About.objects.all()[1:4]
	tag = Tag.objects.all()
	technical_skill = TechnicalSkill.objects.all()
	professional_skill = ProfessionalSkill.objects.all()
	education = Education.objects.all()
	work = Work.objects.all()
	recent_portfolio = RecentPortfolio.objects.all()
	for x in recent_portfolio:
		rptag =x.rptags.all()
	
	reviews = ClientReviews.objects.all()
	blog = BlogPost.objects.all()
	context = {
		"home": home,
		"social_link": social_link,
		"about": about,
		"about2": about2,
		"tag": tag,
		"technical_skill": technical_skill,
		"professional_skill": professional_skill,
		"education": education,
		"work": work,
		"recent_portfolio": recent_portfolio,
		"rptag": rptag,
		"reviews": reviews,
		"blog": blog,
	}
	return render(request, "index.html", context)



def blog_details(request):
	# instance = get_object_or_404(Job, slug=slug)
	# print(instance.company)
	# instance.count=instance.count+1
	# print(instance.count)
	# instance.save()
	# if instance.salaray == None:
	# 	instance.salaray = "negotiable"
	# if instance.employment_status =="f":
	# 	instance.employment_status = "Full Time"
	# elif instance.employment_status =="p":
	# 	instance.employment_status = "Part Time"
	# elif instance.employment_status =="r":
	# 	instance.employment_status = "Remote"

		
	# obj_id = instance.id
	# context = {
	# 	"instance": instance,
	# }
	return render(request, "job/job_details.html", context)