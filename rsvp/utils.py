from django.core.files import File
from django.utils.text import slugify
from io import BytesIO
from PIL import Image

# Image Compresser -------------------------------------------------------------------------------


# Compress images
def compress(image):
    im = Image.open(image)
    # create a BytesIO object
    im_io = BytesIO()
    try:
        # save JPG image to BytesIO object
        im.save(im_io, 'JPEG', optimize=True)
        # create a django-friendly Files object
        new_image = File(im_io, name=image.name)
    except NameError:
        # save PNG image to BytesIO object
        im.save(im_io, 'PNG', optimize=True)
        # create a django-friendly Files object
        new_image = File(im_io, name=image.name)
    except:
        # save GIF image to BytesIO object
        im.save(im_io, 'GIF', save_all=True, optimize=True)
        # create a django-friendly Files object
        new_image = File(im_io, name=image.name)
    return new_image


# Unique Slug Generator --------------------------------------------------------------------------


# Django can detect if a slug is a duplicate but won't convert it into a unique slug.
# This function converts a duplicate slug into a unique slug


# Convert Slug
def unique_slug_generator(model_instance, title):
    """
    :param model_instance:
    :param title:
    :return:
    """
    slug = slugify(title)
    model_class = model_instance.__class__
    num = 1
    while model_class._default_manager.filter(slug=slug).exists():
        slug = slugify(title)
        slug = f'{slug}-{num}'
        num += 1
    return slug


# Save Slug
def slug_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance, instance.title)


# Add Slug and save
def save(self, *args, **kwargs):
    self.s = slugify(self.q)
    super(Test, self).save(*args, **kwargs)
