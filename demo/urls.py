from django.urls import path
# from django.views.generic import TemplateView

from .views import robots_txt_view

# template-based solution
# urlpatterns = [
#     path(
#         'robots.txt',
#         TemplateView.as_view(
#             template_name='demo/robots.txt',
#             content_type='text/plain'
#         )
#     )
# ]

# view-only solution
urlpatterns = [
    path('robots.txt', robots_txt_view),
]
