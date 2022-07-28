from django.views.generic.base import TemplateView
from django.shortcuts import render


class HomePageView(TemplateView):
    template_name = "core/index.html"

    def current_task(loop=None):
        """Return a currently executed task."""
        if loop is None:
            loop = events.get_running_loop()
        return _current_tasks.get(loop)
