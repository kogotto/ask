from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from questions.models import Question

def index(request):
    latest_questions = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('questions/index.html')
    context = RequestContext(request, {
        'latest_questions': latest_questions,
    })
    return HttpResponse(template.render(context))

def detail(request, id):
    question = Question.objects.get(pk = id)
    return HttpResponse("Question %s" % question.text)

def results(request, id):
    return HttpResponse("Results of question %s" % id)

def votes(request, id):
    return HttpResponse("Votes for question %s" % id)
