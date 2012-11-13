# -*- coding: utf-8 -*-

import backbone
from album.models import Album

class BackboneAlbumView(backbone.views.BackboneAPIView):
    """
    Base backbone View for Album
    """
    model = Album

backbone.site.register(BackboneAlbumView)
