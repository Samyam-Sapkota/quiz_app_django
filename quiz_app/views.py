from django.shortcuts import render 

from .models import Questions
import random
from django.views.decorators.csrf import csrf_exempt


random_numbers=[1,2,3,4,5,6,7,8,9,10]             # this is default value which is changed after the home is rendered 
n=0

def home(request):     # Renders the home.html file with questions that are selected by the above function 
    global n            # declaring the n as global variable to use it in the below funtions 
    n=Questions.objects.all().count()             # count total number of the questions in the db 

    random.seed()
    global random_numbers
    random_numbers = random.sample(range(1,n+1), 10)          # select any 10 random numbers from 1 to n+1 

    selected_questions=Questions.objects.filter(pk__in=random_numbers)           # selecting the object with the same pk as the above generated random numbers 
    return render(request,'home.html',{'selected_questions':selected_questions})

    

@csrf_exempt          # used to control the error of csrf cookie 
def get_result_and_display(request):
       
    all_results = []
    if request.method == 'POST':
        for i in range(1, 11):  # Loop from 1 to 10
            result = request.POST.get(f'question{i}_option')
            all_results.append(result)
   
   
    no_of_selected_qns=len(random_numbers)                                                            
    selected_questions=Questions.objects.filter(pk__in=random_numbers)                   # the same questions from above so that the answers are shown through this function
   
    j=score=0                        # count the numbers of question correctly answered

    correct_answers=Questions.objects.filter(pk__in=random_numbers).values_list('answer',flat=True)       # get the actual answer of the question  (QUERY SET OBJECT )
    # print(correct_answers)
    correct_ans=[]                                                                                       
    for i in correct_answers:
        correct_ans.append(i)                                                                             #conver the query to list of correct answers
        if(i==all_results[j]):
            score+=1
        j+=1

    if(score>=n):
        greetings="Congratulations"
    
    elif(score>=8):
        greetings="Great !"
    
    elif(score>=5):
        greetings="Good ! "
    else:
        greetings="Please improve,"
   
    context = {"questions_results":zip(selected_questions,correct_ans,all_results),'selected_questions':selected_questions,    #using the zip to run the 3 for loops as a whole 
               'correct_ans':correct_ans,"all_results": all_results,"no_of_selected_qns":no_of_selected_qns,"score":score,'greetings':greetings}
    
    return render(request,'result_v2.0.html',context)

