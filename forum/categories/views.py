from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.shortcuts import reverse

from forum.categories.models import Category
from forum.threads.forms import ThreadForm
from forum.threads.models import Thread
from forum.threads.utils import (
    get_paginated_queryset,
    get_filtered_threads
)
from forum.core.constants import THREAD_PER_PAGE
from forum.core.utils import get_post_login_redirect_url

def category_detail(request, slug, filter_str=None, page=1, form=None):
    
    category = get_object_or_404(Category, slug=slug)
    if not form:
        form = ThreadForm(initial={'category': category})
    ctx = {
        'category': category,
        'form': form,
    }
    thread_qs = Thread.objects.get_by_category(category=category)
    thread_data = get_filtered_threads(request, filter_str, thread_qs)
    thread_paginator = get_paginated_queryset(
        thread_data[1], THREAD_PER_PAGE, page
    )
    category_url = category.get_precise_url(thread_data[0], page)
    ctx = {
        'category': category,
        'form': form,
        'dropdown_active_text': thread_data[0],
        'threads': thread_paginator,
        'show_floating_btn': True,
        'scroll_or_login': get_post_login_redirect_url(category_url),
        'threads_url': "/categories/%s/%s" % (category.slug, thread_data[0]),
        'form_action': category.get_thread_form_action(thread_data[0], page),
    }
    return render(request, 'categories/category_detail.html', ctx)
