from django.shortcuts import render
from django.shortcuts import get_object_or_404
from . models import Page 

def index(request, pagename):
    pagename = '/' + pagename
    # pg = Page.objects.get(permalink=pagename)
    pg = get_object_or_404(Page, permalink=pagename)
    context = {
        'title': pg.title,
        'content': pg.bodytext,
        'last_updated': pg.update_date,
        'page_list': Page.objects.all()
    }
    # assert False
    return render(request, 'pages/page.html', context)

# Create your views here.
