# -*- coding: utf-8 -*-
from django.views.generic import ListView
from album.models import Album

class AlbumList(ListView):
    """
    List all Albums View
    """

    model = Album
    template_name = "album/list.html"
