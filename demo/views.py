from django.http import HttpResponse


# noinspection PyUnusedLocal
def robots_txt_view(request):
    txt_lines = [
        'User-agent: Googlebot',
        'Disallow: /nogooglebot/',
        '',
        'User-agent: *',
        'Allow: /',
        '',
        'Sitemap: https://www.example.com/sitemap.xml'
    ]
    content = '\n'.join(txt_lines)
    return HttpResponse(content, content_type='text/plain')
