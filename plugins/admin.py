from django.contrib import admin
from cms.extensions import PageExtensionAdmin

from plugins.models import WorkExtension

from cms.models import Page
from cms.utils.page_permissions import user_can_change_page
from django.core.exceptions import PermissionDenied

@admin.register(WorkExtension)
class WorkExtensionAdmin(PageExtensionAdmin):
    pass