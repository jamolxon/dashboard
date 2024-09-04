from django.urls import path

from .views import HomeVideoCreateView, HomeVideoListView

app_name = "home_video"


urlpatterns = [
        path("create/", HomeVideoCreateView.as_view(), name="home-video-create"),
        path("", HomeVideoListView.as_view(), name="home-video-list"),
        ]

