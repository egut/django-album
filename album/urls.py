# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from album.views import *

urlpatterns = patterns('album.views',
    url(r'^$',
        AlbumList.as_view(),
        name = "album-list")
    )
