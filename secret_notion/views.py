from django.shortcuts import render
from django.core.cache import cache
from django.http import HttpResponse
import requests
import hashlib
from secret_notion.models import SecretNotion


def notion_view(request):
    notes_count = len(SecretNotion.objects.all())

    context = {
        'notes_count': notes_count,
    }
    if request.method == 'POST':
        phrase = request.POST.get('phrase')
        salt = request.POST.get('secret_key')

        hash = hashlib.md5((phrase + salt).encode()).hexdigest()

        SecretNotion.objects.create(message=phrase, salt=salt, hashed_message=hash)

        context = {
            'notes_count': notes_count,
            'hash': hash

        }
        return render(request=request, template_name='secret_notion/index.html', context=context)

    if request.method == 'GET' :
        page_id = request.GET.get('page_id')
        hash = request.GET.get('hash')
        salt = request.GET.get('secret_key')

        if hash and salt:
            un_hashed = SecretNotion.objects.filter(hashed_message=hash, salt=salt).values('message')

        else:
            un_hashed = None

        context = {
            'notes_count': notes_count,
            'un_hashed':un_hashed,
        }

    SecretNotion.objects.filter(hashed_message=hash).delete()  # бля хз надо посмотреть я не уверен
    return render(request, 'secret_notion/index.html', context=context)
