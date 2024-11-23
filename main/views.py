from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view

from rest_framework.response import Response

from main.models import Word, HiddenWord
from main.serializer import WordSerializer


# Create your views here.
@api_view(['GET'])
def get_random_word(request, size):
    random_word = HiddenWord.objects.filter(size=size).order_by('?').first()
    # ser = WordSerializer(random_word, many=False)
    return Response(random_word.word)


def get_all(request):
    words = set()
    with open('words.txt', encoding='utf-8') as f:
        line = f.readline().strip()
        while line:
            if 4 <= len(line) < 7:
                new = line.replace('ё', 'е')
                words.add(new)
            line = f.readline().strip()
    for word in words:
        new_word = Word(word=word)
        new_word.save()
    return HttpResponse('Success')


def delete_all(request):
    Word.objects.all().delete()
    return HttpResponse('Success')

