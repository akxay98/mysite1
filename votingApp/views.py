from django.shortcuts import render, redirect, get_object_or_404
from .models import Question, Choice
from django.contrib import messages


def login(request):
    if request.method=='POST':
        login.email = request.POST['email']
        return redirect('index')
            
    return render(request, 'votingApp/login.html')

def index(request):
    ques = Question.objects.order_by('-pub_date')
    return render(request, 'votingApp/index.html', {'ques':ques})

def vote(request, ID):
    ques = Question.objects.get(id=ID)  
    choice = Choice.objects.filter(question=ques)
    if login.email not in ques.voters_email:
        if request.method=='POST':
            vote_id = request.POST.get('choices')
            voted = Choice.objects.get(id=vote_id)
            voted.vote += 1 
            voted.save()
        
            ques.totalvotes +=1
            ques.voters_email += login.email
            ques.save()
            return render(request, 'votingApp/result.html', {'choice':choice, 'ques':ques})
    else:
        con = "You had voted for this poll already."
        return render(request, 'votingApp/result.html', {'choice':choice, 'con':con, 'ques':ques})  
    return render(request, 'votingApp/vote.html', {'ques':ques , 'choice':choice})