from django.urls import path, include

from common.views import HomeView, LoginView, LogoutView

urlpatterns = [
        path("", HomeView.as_view(), name="home"),
        path("home-video/", include("common.home_video.urls")),
        path("login/", LoginView.as_view(), name="login"),
        path("logout/", LogoutView.as_view(), name="logout"),
        ]
