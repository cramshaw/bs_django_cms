from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from categories.models import *

# Work

class DiscplineFilterListPlugin(CMSPluginBase):
    name = "Discipline Filter Plugin"
    render_template = "filter_plugin.html"

    def render(self, context, instance, placeholder):
        context['filter_list'] = Discipline.objects.all()
        context['type'] = 'Disciplines'
        context = super(DiscplineFilterListPlugin, self).render(context, instance, placeholder)
        return context

plugin_pool.register_plugin(DiscplineFilterListPlugin)

class IndustryFilterListPlugin(CMSPluginBase):
    name = "Industry Filter Plugin"
    render_template = "filter_plugin.html"

    def render(self, context, instance, placeholder):
        context['filter_list'] = Industry.objects.all()
        context['type'] = 'Industries'
        context = super(IndustryFilterListPlugin, self).render(context, instance, placeholder)
        return context

plugin_pool.register_plugin(IndustryFilterListPlugin)