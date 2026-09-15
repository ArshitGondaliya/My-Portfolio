from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .forms import ContactForm
from .models import Education, Experience, PortfolioProfile, Project, Skill, SocialLink


def home(request):
    profile = PortfolioProfile.objects.first()
    context = {
        "profile": profile,
        "skills": Skill.objects.all(),
        "experiences": Experience.objects.all(),
        "projects": Project.objects.all(),
        "education": Education.objects.all(),
        "social_links": SocialLink.objects.all(),
        "contact_form": ContactForm(),
    }
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thanks for reaching out. Your message is on its way.")
            return redirect(f"{reverse('home')}#contact")
        context["contact_form"] = form
    return render(request, "home.html", context)


def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, "project_detail.html", {"project": project, "profile": PortfolioProfile.objects.first()})


def custom_404(request, exception):
    return render(request, "404.html", status=404)
