from django.utils import timezone
from django.views import generic
from .models import BlogPost


class IndexView(generic.ListView):
    template_name = "blog/index.html"
    context_object_name = "latest_blog_posts"

    def get_queryset(self):
        return BlogPost.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

