# -*- coding: utf-8 -*-

from django.contrib import admin
from django import forms
from django.template.defaultfilters import slugify

from album.models import Album
from album.forms import AlbumForm

class AlbumAdmin(admin.ModelAdmin):
    """
    The Admin Model for Album
    """
    form=AlbumForm
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Album, AlbumAdmin)
