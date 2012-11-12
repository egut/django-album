# -*- coding: utf-8 -*-

import backbone
from django_album.models import Album

class BackboneAlbumView(backbone.views.BackboneAPIView):
    model = Album

backbone.site.register(BackboneAlbumView)
