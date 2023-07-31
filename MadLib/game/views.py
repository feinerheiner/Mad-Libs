from django.shortcuts import render, redirect
from django.http import HttpResponse
from random import choice
from .models import Story
from .models import Input
from .forms import GamePrepForm
from django.urls import reverse



# Create your views here.
def home(request):
    stories = Story.objects.all()
    context = {
        'stories': stories,
    }
    return render(request, 'gamePages/index.html', context)


def get_random_story_with_inputs():
    stories = Story.objects.all()
    random_story = choice(stories)
    inputs = Input.objects.filter(story=random_story)
    return random_story, inputs


def pickGame(request, id):
    story = Story.objects.get(pk=id)
    inputs = Input.objects.filter(story=story)
    user_inputs = []

    if request.method == 'POST':
        form = GamePrepForm(inputs, request.POST)

        if form.is_valid():
            for item in inputs:
                input_name = item.input_name
                user_input = form.cleaned_data.get(input_name)
                user_inputs.append(user_input)
            filled_story = story.content.format(*user_inputs)
            return redirect(reverse('storyMaker', kwargs={'filled_story': filled_story, 'story_title': story.title}))
        else:
            return HttpResponse("Form is not valid")
    else:
        form = GamePrepForm(inputs)
        context = {
            'story': story,
            'inputs': inputs,
            'form': form,
        }
        return render(request, 'gamePages/gameprep.html', context)


def checkInputs(request):
    inputs_list = Input.objects.all()
    return render(request, 'gamePages/checkInputs.html', {'inputs_list': inputs_list})


def storyMaker(request, filled_story, story_title):
    return render(request, 'gamePages/story.html', {'filled_story': filled_story, 'story_title': story_title})
