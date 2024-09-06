from django.urls import path

from .views import HomeVideoCreateView, HomeVideoDeleteView, HomeVideoListView, HomeVideoUpdateView

app_name = "home_video"


urlpatterns = [
        path("create/", HomeVideoCreateView.as_view(), name="home-video-create"),
        path("", HomeVideoListView.as_view(), name="home-video-list"),
        path("<int:pk>/", HomeVideoUpdateView.as_view(), name="home-video-update"),
        path("delete/<int:pk>/", HomeVideoDeleteView.as_view(), name="home-video-delete"),
        ]

