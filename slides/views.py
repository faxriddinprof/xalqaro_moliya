from django.http import Http404
from django.shortcuts import render
from django.views.generic import TemplateView


class ResumeView(TemplateView):
    """Asosiy resume sahifasi"""

    template_name = "resume.html"


class PresentationsListView(TemplateView):
    """Prezentatsiyalar ro'yxati sahifasi"""

    template_name = "presentationslist.html"


class SlideView(TemplateView):
    """Slayd sahifalari uchun view"""

    def get_template_names(self):
        slide_number = self.kwargs.get("slide_number", 1)

        # 1 dan 15 gacha bo'lgan slaydlar
        if 1 <= slide_number <= 15:
            return [f"international_finance/{slide_number}-slide.html"]
        else:
            raise Http404("Bunday slayd mavjud emas")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slide_number = self.kwargs.get("slide_number", 1)

        # Navigatsiya uchun ma'lumotlar
        context["current_slide"] = slide_number
        context["total_slides"] = 15
        context["has_previous"] = slide_number > 1
        context["has_next"] = slide_number < 15
        context["previous_slide"] = slide_number - 1 if slide_number > 1 else None
        context["next_slide"] = slide_number + 1 if slide_number < 15 else None

        return context


class CurrencySlideView(TemplateView):
    """Valyuta riski (currency_risk) slayd sahifalari uchun view"""

    def get_template_names(self):
        slide_number = self.kwargs.get("slide_number", 1)

        # 1 dan 15 gacha bo'lgan slaydlar
        if 1 <= slide_number <= 15:
            return [f"currency_risk/{slide_number}-slide.html"]
        else:
            raise Http404("Bunday slayd mavjud emas")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slide_number = self.kwargs.get("slide_number", 1)

        # Navigatsiya uchun ma'lumotlar
        context["current_slide"] = slide_number
        context["total_slides"] = 15
        context["has_previous"] = slide_number > 1
        context["has_next"] = slide_number < 15
        context["previous_slide"] = slide_number - 1 if slide_number > 1 else None
        context["next_slide"] = slide_number + 1 if slide_number < 15 else None

        return context


class BaholashSlideView(TemplateView):
    """Baholash ishi (baholash-ishi) slayd sahifalari uchun view"""

    def get_template_names(self):
        slide_number = self.kwargs.get("slide_number", 1)

        # 1 dan 12 gacha bo'lgan slaydlar
        if 1 <= slide_number <= 12:
            return [f"baholash-ishi/{slide_number}.html"]
        else:
            raise Http404("Bunday slayd mavjud emas")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slide_number = self.kwargs.get("slide_number", 1)

        # Navigatsiya uchun ma'lumotlar
        context["current_slide"] = slide_number
        context["total_slides"] = 12
        context["has_previous"] = slide_number > 1
        context["has_next"] = slide_number < 12
        context["previous_slide"] = slide_number - 1 if slide_number > 1 else None
        context["next_slide"] = slide_number + 1 if slide_number < 12 else None

        return context
