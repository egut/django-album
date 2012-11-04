django-album
============

I wanted to build an photo album, so I did.

Version 1:
<pre>
0% [=>                                 ] 100%
</pre>

The plan
========

Album
-----

Make an album that store all images in directories that have the same name
as the album so its easy to just take one group of images to place in eg.
digital photo frame.

But it should be possible to place the same image in multiple albums and to
not loose track of all images (copies) there will not be any copies just hard
links. Albums can have sub albums if you like

eg:
<pre>
  Album1
     image1.jpg --> inode 123
     image2.png -->  inode 456
     :
  Album2
     image1.jpg --> inode 123
     image3.jpg --> inode 234
     :
  Children
    Albert
        image1.jpg --> inode 123
        :
    Maria
        :
</pre>

image1.jpg is the _same_ in all Albums not an copy, the same!



All images will also be placed in a timeline album.
```
eg:
  Timeline Album
    <year>
      <month>
        <day>
          image1 --> inode 123
```

Tags
----

Images can have tags, these tags are more for django to limit view access to
images. Tags will be manage on the admin page to on whom are allowed to view the
images. Some tags are by default, otheres are user defined.

Eg
  Tag: Public -- Anybody
  Tag: Private -- Only logged in
  Tag: PG18 -- Limited to user Dad and Mom (set in admin page)


Images
------

All images will have the name given by the user/camera if possible. Note images
need to have uniq name through out the whole system. Conflicting name will be
handled by applying _[<number>] in the file name. _


GUI
---

The whole GUI will be made in backbone/handelbars to make an simple and snappy
viewment.


Upload GUI
----------

When images have been uplaoded ether by archive (zip/tar) or by adding files to
upload directory. If images are in a directory the album-app asums that the
images belong ot that album and will apply the same album for all images. Also
all images will be added to timeline album if accepted.

All images will go through 2 step screeneing.

Step one: upload dir to albums/delete

When viewing images in upload dir images will slid in from the right in the
browser. The user gets three options. Keep, Maybe, Delete. When pressing one
of those next image will slide in from the right. In the background the
following will happend:

Keep

1. Move to Timeline album
2. Link to origin album name (if any)
3. Get tag: Private
4. Get tag: Keep (needed for later processing)

Maybe

1. Link to origin album name (if any)
2. Get tag: Private
3. Get tag: Maybe (needed for later processing)

Delete

1. Move to delete folder
2. Get tag: Delete
3. Get delete on the filesystem a few days later or when someone press the right button.

Step two: Organice keep images

For all images with tag: keep. Slide in the image from the right. Present
check button for all albums below the image. Also pressent select buttons for
tags. When the user press the next button, save all the options selected and
remove the tag Keep. Can also be deleted.

On all images there is the possiblity to add an caption.

Step three: Organice maybe images

For all images with tag: keep. Slide in the image from the right. Present
check button for all albums below the image. Also pressent select buttons for
tags. When the user press the next button, save all the options selected and
remove the tag Maybe. Can also be deleted

On all images there is the possiblity to add an caption.

View GUI
--------

If anonymous user view only public images. Also do not view album that is empty
or due to access limits appere to be empty.

If logged in the user can view  all images that have the tag private but the
same rules as for public image are then aplied.

If the user also have speciall previlige for other tags (as User:Mom have PG18)
also those images with these tags are allowed to be viewed.

The viewing will be done in 3 steps.

1. All albums (and random tumbnail)
2. Thumbnails of all images (backbone)
3. Large version where images slide in from right when clicking next (backbone)





