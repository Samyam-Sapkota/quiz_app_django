from django.db import models

# Create your models here.

class Questions(models.Model):
    questions = models.CharField(max_length=200)                      # store the questions 
    option_a = models.CharField(max_length=50)                        # option for the above questions                                                        
    option_b = models.CharField(max_length=50)                        # option for the above questions                                             
    option_c = models.CharField(max_length=50)                        # option for the above questions                 
    option_d = models.CharField(max_length=50)                        # option for the above questions   
    answer = models.CharField(max_length=50)                          # answer of the question  
    def __str__(self):
        return self.questions
    


