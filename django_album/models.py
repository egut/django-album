# -*- coding: utf-8 -*-
from django.utils.translation import ugettext as _
from django.db import models
from django.contrib.auth.models import User

class Album(models.Model):
    """


    """


class Tag(models.Model):
    """

    """


class Image(models.Model):
    """
    This model will describe the image it self. Any caption and other data
    will obuse always be related to the image.

    """

    filename = models.CharField(
        primary_key = True,
        max_length = 200,
        help_text = _("Uniq filename")
    )

    md5sum = models.CharField(
        max_length = 38,
        help_text = _("Generated md5sum for the file")
    )

    caption = models.TextField(
        blank = True,
        null = True,
        help_text = _("Describ the image or what is happening on it.")
    )

    photograph = models.ForeignKey(
        User,
        blank = True,
        null = True,
        on_delete = models.SET_NULL,
        help_text = _("Who took the photo")
    )

    snapped = models.DateTimeField(
        null = False,
        help_text = _("When was the image taken")
    )

    def __unicode__(self):
        return self.filename

    #@models.permalink
    #def get_absolute_url(self):
    #    filepath = "%s/%s" % ()
    #    return ('image-detail', [str(self.filename)])
