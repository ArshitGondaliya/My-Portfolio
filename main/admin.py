from django.contrib import admin
from .models import ContactMessage, Education, Experience, PortfolioProfile, Project, Skill, SocialLink


@admin.register(PortfolioProfile)
class PortfolioProfileAdmin(admin.ModelAdmin):
    list_display = ("name", "title", "email", "updated_at")


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "display_order")
    list_filter = ("category",)
    list_editable = ("display_order",)


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("position", "company", "duration", "display_order")
    list_editable = ("display_order",)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "featured", "display_order")
    list_filter = ("featured", "category")
    list_editable = ("featured", "display_order")


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ("degree", "institution", "year", "result", "display_order")


@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ("label", "url", "display_order")


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("subject", "name", "email", "created_at", "is_read")
    list_filter = ("is_read", "created_at")
    list_editable = ("is_read",)
    readonly_fields = ("created_at",)
