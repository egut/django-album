# -*- coding: utf-8 -*-
from django.utils.translation import ugettext as _
from django.template.defaultfilters import slugify
from django.db import models
from django.contrib.auth.models import User


class Album(models.Model):
    """
    The album will have some description and images.

    It will also have an path so that all images will be collected in one
    directory. This to make it easyer to take one album and move it to an
    photo digital photo frame.

    Albums can also placed in albums

    """

    slug = models.SlugField(
        max_length = 75,
        primary_key = True,
        help_text = _("Short URL frendly name of the album")
    )

    name = models.CharField(
        max_length = 200,
        help_text = _("The album name")
    )

    description = models.TextField(
        help_text = _("An nice description of the album")
    )

    images = models.ManyToManyField(
        'Image',
        null = True,
        blank = True,
        help_text = _("The images that belongs to this album")
    )

    parent_album = models.ForeignKey(
        'self',
        blank = True,
        null = True,
        help_text = _("Link to the parent album so that album can be grouped")
    )

    def save(self, *args, **kwargs):
        """
        Generate the slug the first time this album is saved.
        """
        if not self.slug:
            self.slug = slugify(self.name)

        super(Album, self).save(*args, **kwargs)

    def __unicode__(self):
        """
        The name to return when litsting and saving in python
        """
        return self.name

    @models.permalink
    def get_absolute_url(self):
        """
        Return the path to this album

        ToDo: Add support for patent directories
        """

        return self.slug



#class Meta(models.Model):
#    """
#    ToDo: Add meta data later
#    """


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
