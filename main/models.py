from django.core.validators import URLValidator
from django.db import models


class PortfolioProfile(models.Model):
    name = models.CharField(max_length=120, default="Arshit Gondaliya")
    title = models.CharField(max_length=180, default="Software Engineer | Web Developer | Data Analytics")
    description = models.TextField()
    about_text = models.TextField(blank=True)
    location = models.CharField(max_length=160, default="Surat, Gujarat, India")
    phone = models.CharField(max_length=30, default="+91 8200993607")
    email = models.EmailField(default="arshitgondaliya09@gmail.com")
    profile_image = models.ImageField(upload_to="profile/", blank=True)
    about_image = models.ImageField(upload_to="profile/", blank=True)
    contact_image = models.ImageField(upload_to="profile/", blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Portfolio profile"
        verbose_name_plural = "Portfolio profile"

    def __str__(self):
        return self.name


class Skill(models.Model):
    CATEGORY_CHOICES = [("programming", "Programming"), ("data", "Data Science & ML"), ("web", "Web & Database"), ("tools", "Tools")]
    name = models.CharField(max_length=80)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    icon = models.CharField(max_length=60, default="fa-code")
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["category", "display_order", "name"]

    def __str__(self):
        return self.name


class Experience(models.Model):
    company = models.CharField(max_length=160)
    position = models.CharField(max_length=160)
    duration = models.CharField(max_length=80)
    description = models.TextField()
    technologies = models.CharField(max_length=240, blank=True)
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["display_order"]
        verbose_name_plural = "Experience"

    def __str__(self):
        return f"{self.position} at {self.company}"


class Project(models.Model):
    title = models.CharField(max_length=220)
    category = models.CharField(max_length=120)
    description = models.TextField()
    detailed_description = models.TextField(blank=True)
    technologies = models.CharField(max_length=320)
    project_image = models.ImageField(upload_to="projects/", blank=True)
    github_url = models.URLField(blank=True, validators=[URLValidator(schemes=["https"])])
    live_demo_url = models.URLField(blank=True, validators=[URLValidator(schemes=["https"])])
    display_order = models.PositiveIntegerField(default=0)
    featured = models.BooleanField(default=False)

    class Meta:
        ordering = ["display_order", "title"]

    def __str__(self):
        return self.title

    @property
    def technology_list(self):
        return [item.strip() for item in self.technologies.split(",") if item.strip()]


class Education(models.Model):
    degree = models.CharField(max_length=160)
    institution = models.CharField(max_length=180)
    year = models.CharField(max_length=40)
    result = models.CharField(max_length=80)
    description = models.TextField(blank=True)
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["-display_order", "-year"]
        verbose_name_plural = "Education"

    def __str__(self):
        return f"{self.degree} - {self.institution}"


class SocialLink(models.Model):
    label = models.CharField(max_length=80)
    url = models.CharField(max_length=300, blank=True)
    icon = models.CharField(max_length=60, default="fa-link")
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["display_order", "label"]

    def __str__(self):
        return self.label


class ContactMessage(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    subject = models.CharField(max_length=180)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.subject} from {self.name}"
