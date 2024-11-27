# quiz/views.py
from django.shortcuts import render
import random
from .models import Question

def dashboard(request):
    user_stats = request.session.get('user_stats', {'attempted': 0, 'correct': 0})
    
    # Calculate the percentage
    if user_stats['attempted'] > 0:
        percentage = (user_stats['correct'] / user_stats['attempted']) * 100
    else:
        percentage = 0.0
    
    # Pass the percentage to the template
    return render(request, 'quiz/dashboard.html', {
        'user_stats': user_stats,
        'percentage': percentage,
    })
def quiz(request):
    questions = Question.objects.all()

    # Check if there are any questions
    if not questions:
        return render(request, 'quiz/quiz.html', {'error_message': "No questions available. Please add questions."})
    
    question = random.choice(questions)
    return render(request, 'quiz/quiz.html', {'question': question})

def submit_answer(request):
    if request.method == 'POST':
        user_answer = int(request.POST['answer'])
        question_id = int(request.POST['question_id'])
        question = Question.objects.get(id=question_id)

        # Determine if the answer is correct
        correct = user_answer == question.correct_option

        # Get the correct option text
        correct_option_text = getattr(question, f"option{question.correct_option}")
        
        # Get the user's answer text
        user_answer_text = getattr(question, f"option{user_answer}")

        # Track user statistics
        user_stats = request.session.get('user_stats', {'attempted': 0, 'correct': 0})
        user_stats['attempted'] += 1
        if correct:
            user_stats['correct'] += 1
        request.session['user_stats'] = user_stats

        # Pass the correct option text and user's answer text to the result page
        context = {
            'correct': correct,
            'user_answer_text': user_answer_text,  # Pass the user's answer text
            'correct_option_text': correct_option_text,  # Pass the correct option text
        }
        return render(request, 'quiz/result.html', context)