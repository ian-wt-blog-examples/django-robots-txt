from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path(
        'robots.txt',
        TemplateView.as_view(
            template_name='demo/robots.txt',
            content_type='text/plain'
        )
    )
]
