from django.conf.urls import patterns, include, url


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'example.views.home', name='home'),
    # url(r'^example/', include('example.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)


######################################################################
# Stuff bleow is needed for django-album, if you already have these
# then you do not need to add them again.
#

#Find all the backbones components
import backbone
backbone.autodiscover()

urlpatterns += patterns('',
    (r'^backbone/', include(backbone.site.urls))
)

#Add all django-album parts
urlpatterns += patterns('',
    (r'^album/', include('django_album.urls'))
)

# To display MEDIA files in DEVELOPMENT
# For production see:
# https://docs.djangoproject.com/en/dev/howto/static-files/#serving-static-files-in-production
from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# To display STATIC files in DEVELOPMENT
# For production see:
# https://docs.djangoproject.com/en/dev/howto/static-files/#serving-static-files-in-production
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()




