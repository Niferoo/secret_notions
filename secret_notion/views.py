from django.shortcuts import render
from django.core.cache import cache
import requests


def notion_view(request):
    notes_count = 12

    if request.method == 'POST':
        phrase = request.POST.get('phrase')
        secret_key = request.POST.get('secret_key')

        context = {
            'notes_count': notes_count,
            'phrase': phrase,
            'secret_key': secret_key,
        }

    if request.method == 'GET':
        page_id = request.GET.get('page_id')
        secret_key = None
        phrase = request.GET.get('phrase')
        secret_key = request.GET.get('secret_key')

        context = {
            'notes_count': notes_count,
            'phrase': phrase,
            'secret_key': secret_key,
        }
    print(context)
    return render(request, 'secret_notion/index.html', context=context)
