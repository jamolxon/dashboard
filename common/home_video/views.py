from django.views.generic import ListView
from django.db.models import Q

from common.models import HomeVideo
from helpers.views import CreateView, UpdateView, DeleteView
from .forms import HomeVideoForm



class HomeVideoCreateView(CreateView):
    model = HomeVideo
    form_class = HomeVideoForm
    template_name = "home-video/create.html"
    context_object_name = "object"
    success_url = "home_video:home-video-list"
    success_create_url = "home_video:home-video-create"




class HomeVideoListView(ListView):
    model = HomeVideo
    template_name = "home-video/list.html"
    context_object_name = "objects"
    queryset = model.objects.all().order_by("-id")
    paginate_by = 10


    def get_queryset(self):
        object_list = self.queryset
        search = self.request.GET.get("search", None)
        if search:
            object_list = object_list.filter(
                    Q(name__icontains=search)
                    )

        return object_list


class HomeVideoUpdateView(UpdateView):
    model = HomeVideo
    template_name = "home-video/update.html"
    form_class = HomeVideoForm
    context_object_name = "object"
    success_url = "home_video:home-video-list"
    success_update_url = "home_video:home-video-update"


class HomeVideoDeleteView(DeleteView):
    model = HomeVideo
    success_url = "home_video:home-video-list"

