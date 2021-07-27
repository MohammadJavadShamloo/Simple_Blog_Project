from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from django.urls import reverse_lazy
from .models import Post


class LatestPostFeeds(Feed):
    title = 'My Blog'
    link = reverse_lazy('blog:post_list')
    description = 'New Posts Of My Blog'

    def items(self):
        return Post.published.all().order_by('-publish')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.body, 30)
