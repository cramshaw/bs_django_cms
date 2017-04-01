from django.db import models

from cms.extensions.models import PageExtension, BaseExtension
from cms.extensions.extension_pool import extension_pool

from cms.models import CMSPlugin
from filer.fields.image import FilerImageField, FilerFileField

from categories.models import Discipline, Industry

# PAGES

class WorkExtension(PageExtension):
    image = FilerImageField(null=True, related_name="work_display_image")
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    disciplines = models.ManyToManyField(Discipline)
    industries = models.ManyToManyField(Industry)

    def copy_relations(self, oldinstance, language):
        self.disciplines = oldinstance.disciplines.all()
        self.industries = oldinstance.industries.all()

extension_pool.register(WorkExtension)

# PLUGINS
# Homepage

class CarouselPlugin(CMSPlugin):
    interval = models.IntegerField(default=2000, help_text="interval between slides in milliseconds")

class CarouselItemPlugin(CMSPlugin):
    carousel = models.ForeignKey(CarouselPlugin, related_name='slides')
    background = FilerImageField(null=True, related_name="background")

# About

class LinkVideoPlugin(CMSPlugin):
    title = models.CharField(max_length=25)
    jump_to_index = models.CharField(max_length=10)
    video = FilerFileField(related_name="link_video")

    def __str__(self):
        return self.jump_to_index

class LinkedSectionPlugin(CMSPlugin):
    index = models.CharField(max_length=10)

    def __str__(self):
        return self.index

class MapPlugin(CMSPlugin):
    latitude = models.FloatField()
    longitude = models.FloatField()
    zoom = models.IntegerField()
    label = models.CharField(max_length=20)
    direct_link = models.URLField(null=True, help_text="Generate this by going to Google Maps and pressing 'Share'")

    def __str__(self):
        return self.label

class AwardPlugin(CMSPlugin):
    logo = FilerImageField(null=True, related_name="award_logo")
    text = models.TextField()

    def __str__(self):
        return instance.text[:15]

# General

class RowPlugin(CMSPlugin):
    ymargin = models.IntegerField(help_text="on a scale of 1 to 5, as per Bootstrap, adds margin to top and bottom of row")

    def __str__(self):
        return self.css_class()

    def css_class(self):
        return 'row my-' + str(self.ymargin)

class ColumnPlugin(CMSPlugin):
    COL_CHOICES = (
        ('', 'Extra Small'),
        ('sm-', 'Small'),
        ('md-', 'Medium'),
        ('lg-', 'Large'),
        ('xl-', 'Extra Large'),
        )
    size = models.CharField(max_length=3, choices=COL_CHOICES, default='md-', help_text="The larger the column, the more likely it will stack as screen size decreases.")
    width = models.IntegerField(help_text="This creates a Bootstrap Column, full width is 12.")

    def __str__(self):
        return self.css_class()

    def css_class(self):
        return 'col-' + self.size + str(self.width)

class HRPlugin(CMSPlugin):
    COLOURS = (
        ('thick', 'Dark and thick'),
        ('dark', 'Dark and thin'),
        ('light', 'Light')
        )
    css_class = models.CharField(max_length=5, choices=COLOURS, default='light')

    def __str__(self):
        return dict(self.COLOURS)[self.css_class]

class EmailFormPlugin(CMSPlugin):
    COLOURS = (
        ('dark', 'Black'),
        ('light', 'White')
        )
    css_class = models.CharField(max_length=5, choices=COLOURS, default='light')

    def __str__(self):
        return dict(self.COLOURS)[self.css_class]

# Footer

class AddressPlugin(CMSPlugin):
    address = models.TextField()
    email = models.CharField(max_length=200)

class SocialLinkPlugin(CMSPlugin):
    icon = FilerImageField(null=True, related_name="social_icon")
    text = models.CharField(max_length=30)
    link = models.URLField()

    def __str__(self):
        return self.text