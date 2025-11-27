from django.urls import path

from .views import ResumeView, PresentationsListView, SlideView, CurrencySlideView, BaholashSlideView

urlpatterns = [
    path("", ResumeView.as_view(), name="resume"),
    path("presentations/", PresentationsListView.as_view(), name="presentations_list"),
    path("slide/<int:slide_number>/", SlideView.as_view(), name="slide"),
    path("currency/slide/<int:slide_number>/", CurrencySlideView.as_view(), name="currency_slide"),
    path("baholash/<int:slide_number>/", BaholashSlideView.as_view(), name="baholash_slide"),
]
