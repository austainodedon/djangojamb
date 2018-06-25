from django.http import HttpResponse

from .models import Question, Choice

from django.shortcuts import render

from django.shortcuts import get_object_or_404

from django.http import HttpResponseRedirect

from django.urls import reverse

# 2 Add the generic module
from django.views import generic

# 8 Import so we can get time information
from django.utils import timezone


# 2 The ListView displays your list of questions being
# latest_question_list
class IndexView(generic.ListView):
    template_name = 'polls/index.html'

    # 2 This defines the question list we want to use
    context_object_name = 'latest_question_list'

    # 8 Replace get_queryset and don't return questions
    #  published in the future
    '''
    def get_queryset(self):

        # 2 Return the last 5 questions entered
        return Question.objects.order_by('-pub_date')[:5]
    '''

    def get_queryset(self):
        # 8 Return only questions with a pub_date less than
        # or equal to now
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]

        # 8 Add Choices to the Admin in admin.py


# 2 The DetailView displays the details on your object
# being the Question model

# 2 The generic view expects the pk (Primary Key) value
# from the URL to be called pk as we set in polls/urls.py
class DetailView(generic.DetailView):
    model = Question

    # 2 Define the template to use with this data
    template_name = 'polls/detail.html'

    # 12 Exclude questions that are not published yet
    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())

    # 12 Add tests in polls/tests.py


# 2
class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


# 2 Remove these functions

'''
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]

    context = {
        'latest_question_list': latest_question_list,
    }

    return render(request, 'polls/index.html', context)

def detail(request, question_id):

    question = get_object_or_404(Question, pk=question_id)

    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):

    question = get_object_or_404(Question, pk=question_id)

    return render(request, 'polls/results.html', {'question': question})
'''


# 2 Vote stays the same
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])

    except(KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice"
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


# 3 Now we will explore automated testing. You can either
# check your code by entering values randomly (and miss
# a bunch of errors), or you can automate the process.

# 3 We'll now explore a bug in the was_published_recently() function
# in polls/models.py in the shell : python3 manage.py shell

# 3 Create a Question with a pub_date in the future
'''
import datetime
from django.utils import timezone
from polls.models import Question
future_question = Question(pub_date=timezone.now() + datetime.timedelta(days=30))
future_question.was_published_recently()
Returns true even though that doesn't make sense
'''

# 3 Open the file called tests.py