from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from plugins.models import *

# Homepage

class CMSCarouselPlugin(CMSPluginBase):
    model = CarouselPlugin
    name = "Carousel Plugin"
    render_template = "carousel-plugin.html"
    allow_children = True
    child_classes = ['CMSCarouselItemPlugin']

    def render(self, context, instance, placeholder):
        context = super(CMSCarouselPlugin, self).render(context, instance, placeholder)
        return context

plugin_pool.register_plugin(CMSCarouselPlugin)

class CMSCarouselItemPlugin(CMSPluginBase):
    model = CarouselItemPlugin
    name = "Carousel Slide"
    require_parent = True
    parent_classes = ['CMSCarouselPlugin']
    render_template = "carousel-item.html"

    def render(self, context, instance, placeholder):
        context = super(CMSCarouselItemPlugin, self).render(context, instance, placeholder)
        return context

plugin_pool.register_plugin(CMSCarouselItemPlugin)

# About

class CMSMapPlugin(CMSPluginBase):
    model = MapPlugin
    name = "Map Plugin"
    render_template = "map.html"

    def render(self, context, instance, placeholder):
        context = super(CMSMapPlugin, self).render(context, instance, placeholder)
        return context

plugin_pool.register_plugin(CMSMapPlugin)

class CMSAwardPlugin(CMSPluginBase):
    model = AwardPlugin
    name = "Award Plugin"
    render_template = "award.html"
    require_parent = True
    parent_classes = ['CMSRowPlugin']

    def render(self, context, instance, placeholder):
        context = super(CMSAwardPlugin, self).render(context, instance, placeholder)
        return context

plugin_pool.register_plugin(CMSAwardPlugin)

class CMSLinkedSectionPlugin(CMSPluginBase):
    model = LinkedSectionPlugin
    name = "Linked Section"
    allow_children = True
    render_template = "linked-section.html"

    def render(self, context, instance, placeholder):
        context = super(CMSLinkedSectionPlugin, self).render(context, instance, placeholder)
        return context

plugin_pool.register_plugin(CMSLinkedSectionPlugin)


class CMSLinkVideoPlugin(CMSPluginBase):
    model = LinkVideoPlugin
    name = "Link With Video"
    render_template = "link-video.html"

    def render(self, context, instance, placeholder):
        context = super(CMSLinkVideoPlugin, self).render(context, instance, placeholder)
        return context

plugin_pool.register_plugin(CMSLinkVideoPlugin)

# Generic

class CMSRowPlugin(CMSPluginBase):
    name = "Row"
    model = RowPlugin
    allow_children = True
    render_template = "row.html"

    def render(self, context, instance, placeholder):
        context = super(CMSRowPlugin, self).render(context, instance, placeholder)
        return context

plugin_pool.register_plugin(CMSRowPlugin)

class CMSColumnPlugin(CMSPluginBase):
    name = "Column"
    model = ColumnPlugin
    allow_children = True
    render_template = "column.html"

    def render(self, context, instance, placeholder):
        context = super(CMSColumnPlugin, self).render(context, instance, placeholder)
        return context

plugin_pool.register_plugin(CMSColumnPlugin)

class CMSHRPlugin(CMSPluginBase):
    name = "HR Line"
    model = HRPlugin
    render_template = "hr.html"

    def render(self, context, instance, placeholder):
        context = super(CMSHRPlugin, self).render(context, instance, placeholder)
        return context

plugin_pool.register_plugin(CMSHRPlugin)

class CMSScrollToTopTextPlugin(CMSPluginBase):
    name = "Scroll to top Text"
    allow_children = False
    render_template = "scroll-to-top-text.html"

    def render(self, context, instance, placeholder):
        context = super(CMSScrollToTopTextPlugin, self).render(context, instance, placeholder)
        return context

plugin_pool.register_plugin(CMSScrollToTopTextPlugin)

class CMSScrollToTopPlugin(CMSPluginBase):
    name = "Scroll to top icon"
    allow_children = False
    render_template = "to-top.html"

    def render(self, context, instance, placeholder):
        context = super(CMSScrollToTopPlugin, self).render(context, instance, placeholder)
        return context

plugin_pool.register_plugin(CMSScrollToTopPlugin)

class CMSEmailFormPlugin(CMSPluginBase):
    name = "Email Subscribe Form"
    model = EmailFormPlugin
    allow_children = False
    render_template = "email_form.html"

    def render(self, context, instance, placeholder):
        context = super(CMSEmailFormPlugin, self).render(context, instance, placeholder)
        return context

plugin_pool.register_plugin(CMSEmailFormPlugin)

# Footer

class CMSFooterPlugin(CMSPluginBase):
    name = "Footer"
    allow_children = True
    render_template = "footer.html"

    def render(self, context, instance, placeholder):
        context = super(CMSFooterPlugin, self).render(context, instance, placeholder)
        return context

plugin_pool.register_plugin(CMSFooterPlugin)

class CMSAddressPlugin(CMSPluginBase):
    model = AddressPlugin
    name = "Address & Terms Block"
    allow_children = False
    render_template = "address.html"

    def render(self, context, instance, placeholder):
        context = super(CMSAddressPlugin, self).render(context, instance, placeholder)
        return context

plugin_pool.register_plugin(CMSAddressPlugin)

class CMSSocialBlockPlugin(CMSPluginBase):
    name = "Social Links Container"
    allow_children = True
    child_classes = ['CMSSocialLinkPlugin']
    render_template = "social-link.html"

    def render(self, context, instance, placeholder):
        context = super(CMSSocialBlockPlugin, self).render(context, instance, placeholder)
        return context

plugin_pool.register_plugin(CMSSocialBlockPlugin)

class CMSSocialLinkPlugin(CMSPluginBase):
    model = SocialLinkPlugin
    name = "Social Link"
    require_parent = True
    parent_classes = ['CMSSocialBlockPlugin']
    render_template = "social-block.html"

    def render(self, context, instance, placeholder):
        context = super(CMSSocialLinkPlugin, self).render(context, instance, placeholder)
        return context

plugin_pool.register_plugin(CMSSocialLinkPlugin)

class CMSSocialSharePlugin(CMSPluginBase):
    model = SocialSharePlugin
    name = "Social Share Buttons"
    require_parent = True
    render_template = "social-share.html"

    def render(self, context, instance, placeholder):
        context = super(CMSSocialSharePlugin, self).render(context, instance, placeholder)
        return context

plugin_pool.register_plugin(CMSSocialSharePlugin)

class CMSNextLastPagePlugin(CMSPluginBase):
    name = "Next/Last Buttons"
    require_parent = False
    render_template = "next-last.html"

    def render(self, context, instance, placeholder):
        context = super(CMSNextLastPagePlugin, self).render(context, instance, placeholder)
        from cms.models import Page

        current_page = context['request'].current_page

        if context['request'].GET.get('dis', None):
            print('parent', current_page.parent)

            dis = context['request'].GET['dis']
            ind = context['request'].GET['ind']
            print(dis, ind)

            params = '?dis={}&ind={}'.format(dis, ind)

            queries = {}
            if dis != '.display-all':
                dis = dis.split('-')[-1]
                queries['workextension__disciplines__id'] = dis

            if ind != '.display-all':
                ind = ind.split('-')[-1]
                queries['workextension__industries__id'] = ind

            queries['publisher_is_draft'] = False
            queries['parent'] = current_page.parent

            pages = Page.objects.filter(**queries)

        else:
            # reached this page without filtering
            # All children of current pages parent/sibling
            pages = Page.objects.filter(publisher_is_draft=False, parent=current_page.parent)
            params = ''

        n = 0
        next = None
        last = None

        for page in pages:
            print('a')

            if page == current_page:
                print(n)
                if n == 0:
                    next = pages[n+1].get_absolute_url() + params
                elif n == pages.count() - 1:
                    last = pages[n-1].get_absolute_url() + params
                else:
                    next = pages[n+1].get_absolute_url() + params
                    last = pages[n-1].get_absolute_url() + params

                context['next'] = next
                context['last'] = last
                break
            else:
                n += 1

        return context

plugin_pool.register_plugin(CMSNextLastPagePlugin)