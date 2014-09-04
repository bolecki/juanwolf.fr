from django.conf.urls import include, url, patterns
from django.contrib.sitemaps.views import sitemap
from blogengine.models import Post, Category, Tag, BlogSitemap
from blogengine.views import PostListView, CategoryDetailView, PostsFeed, TagDetailView, \
    PostDetailView, PageNotFoundView
from juanwolf_s_blog import settings

sitemaps = {
    'blog': BlogSitemap
}
urlpatterns = patterns('',
    # Index
    url(r'^(?P<page>\d+)?/?$', PostListView.as_view(
        model=Post,
        paginate_by=5,
        )),

    # Individual posts
    url(r'^(?P<category>[a-zA-Z0-9-]+)/(?P<slug>[a-zA-Z0-9-]+)/?$', PostDetailView.as_view(
        model=Post,
        )),

    # Categories
    url(r'^(?P<slug>[a-zA-Z0-9-]+)/?$', CategoryDetailView.as_view(
        paginate_by=5,
        model=Category,
        )),

    # Post RSS feed
    url(r'^feeds/posts/$', PostsFeed()),

    # Summernote
    url(r'^summernote/', include('django_summernote.urls')),

    # Tags
    url(r'^tag/(?P<slug>[a-zA-Z0-9-]+)/?$', TagDetailView.as_view(
        paginate_by=5,
        model=Tag,
        )),
    # Internationalization
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap',
        {'sitemaps': sitemaps}),
)
if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}),
        url('^test/404testing/$', PageNotFoundView.as_view()),)

