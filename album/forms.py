# -*- coding: utf-8 -*-

from django.forms import ModelForm
from album.models import Album

class AlbumForm(ModelForm):
    """
    The main album form, this one can edit all fields
    """
    class Meta:
        model = Album
        fields=(
            'name',
            'parent_album',
            'description',
            'images',
            'slug',
            )

