from django.urls import path

from .views import ResumeView, SlideView, CurrencySlideView

urlpatterns = [
    path("", ResumeView.as_view(), name="resume"),
    path("slide/<int:slide_number>/", SlideView.as_view(), name="slide"),
    path("currency/slide/<int:slide_number>/", CurrencySlideView.as_view(), name="currency_slide"),
]
