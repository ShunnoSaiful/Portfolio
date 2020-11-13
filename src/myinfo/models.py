from django.db import models
from django.urls import reverse
from django.db.models.signals import pre_save




def upload_location(instance, filename):
    filebase, extension = filename.split(".")
    return "%s/%s.%s" %(instance.myname, instance.myname, extension)
    HomeModel = instance.__class__
    new_id = HomeModel.objects.order_by("instance.myname").last().id + 1

    return "%s" %(filename)


class Home(models.Model):
    logo        = models.ImageField(upload_to=upload_location, null=True, blank=True)
    navbar      = models.CharField(max_length=120, null=True, blank=True)
    pro_picture = models.ImageField(upload_to=upload_location, null=True, blank=True)
    myname      = models.CharField(max_length=120)
    my_title    = models.CharField(max_length=120, null=True, blank=True)
    email       = models.EmailField(null=True, blank=True)
    contact_no  = models.CharField(max_length=120, null=True, blank=True)
    address     = models.CharField(max_length=120, null=True, blank=True)
    social_link = models.URLField(null=True, blank=True)

    def __str__(self):
        return str(self.myname)

    def save(self):
        create_user = Home.objects.filter(myname=self.myname).count()
        if create_user > 1:
            raise ValidationError("Your user plan does not support more than {} posts".format(create_user))


class SocialLink(models.Model):
    home        = models.ForeignKey(Home, related_name='link', on_delete=models.CASCADE)
    social_link = models.URLField(null=True, blank=True)

    def __str__(self):
        return str(self.social_link)


class About(models.Model):
    title        = models.CharField(max_length=120, null=True, blank=True)
    content      = models.TextField(null=True, blank=True)
    tag          = models.CharField(max_length=120, null=True, blank=True)
    image        = models.ImageField(upload_to='about/', null=True, blank=True)
    icon         = models.CharField(max_length=120, null=True, blank=True)
    resume       = models.FileField(upload_to='resume/', null=True, blank=True)


    def __str__(self):
        return str(self.title)


class Tag(models.Model):
    about = models.ForeignKey(About, related_name='tags', on_delete=models.CASCADE)
    tag   = models.CharField(max_length=120, null=True, blank=True)

    def __str__(self):
        return str(self.tag)


class TechnicalSkill(models.Model):
    skill      = models.CharField(max_length=120, null=True, blank=True)
    percentage = models.DecimalField(max_digits=2, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return str(self.skill)


class ProfessionalSkill(models.Model):
    skill      = models.CharField(max_length=120, null=True, blank=True)
    percentage = models.DecimalField(max_digits=2, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return str(self.skill)



class Education(models.Model):
    degree    = models.CharField(max_length=120, null=True, blank=True)
    institute = models.CharField(max_length=120, null=True, blank=True)
    year1     = models.DateField(auto_now=True, auto_now_add=False)
    year2     = models.DateField(auto_now=True, auto_now_add=False)
    dept      = models.CharField(max_length=120, null=True, blank=True)


    def __str__(self):
        return str(self.degree)



class Work(models.Model):
    position        = models.CharField(max_length=120, null=True, blank=True)
    institute       = models.CharField(max_length=120, null=True, blank=True)
    year1           = models.DateField(auto_now=True, auto_now_add=False)
    year2           = models.DateField(auto_now=True, auto_now_add=False)
    responsibility1 = models.CharField(max_length=120, null=True, blank=True)
    responsibility2 = models.CharField(max_length=120, null=True, blank=True)
    responsibility3 = models.CharField(max_length=120, null=True, blank=True)
    responsibility4 = models.CharField(max_length=120, null=True, blank=True)


    def __str__(self):
        return str(self.position)


class RecentPortfolio(models.Model):
    title          = models.CharField(max_length=120, null=True, blank=True)
    content        = models.TextField(null=True, blank=True)
    image          = models.ImageField(upload_to='portfolio/', null=True, blank=True)
    tag            = models.CharField(max_length=120, null=True, blank=True)
    portfolio_link = models.URLField(null=True, blank=True)


    def __str__(self):
        return str(self.title)



class ClientReviews(models.Model):
    review  = models.CharField(max_length=120, null=True, blank=True)
    name    = models.CharField(max_length=120, null=True, blank=True)
    image   = models.ImageField(upload_to='Client/', null=True, blank=True)
    company = models.CharField(max_length=120, null=True, blank=True)


    def __str__(self):
        return str(self.review)



def one_profile_creator(sender, instance, *args, **kwargs):
    if instance.myname:
        instance = Home.objects.filter(myname=self.myname).count()
        if instance > 1:
            raise ValidationError("Your user plan does not support more than {} posts".format(create_user))

pre_save.connect(one_profile_creator, sender=Home)

