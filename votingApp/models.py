from django.db import models

class Question(models.Model):
    ques_head = models.CharField(max_length=100)
    description = models.TextField(max_length=400)
    pub_date = models.DateTimeField("Date Published")
    voters_email = models.TextField(default="Emails: ")
    totalvotes =  models.IntegerField(default=0)

    def __str__(self):
        return self.ques_head

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    vote = models.IntegerField(default=0)

    def percentage(self):
        total = self.question.totalvotes
        votes = self.vote

        if total == 0:
            percentage = 0
        else:
            percentage = round((votes/total)*100, 2)

        return percentage        

    def __str__(self):
        return self.choice_text
