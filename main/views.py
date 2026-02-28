from django.shortcuts import render
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from .models import Project, SkillCategory, Experience

def index(request):
    projects = Project.objects.all().order_by('-created_at')
    skill_categories = SkillCategory.objects.prefetch_related('skills').all()
    extra_experience = Experience.objects.all()
    
    context = {
        'projects': projects,
        'skill_categories': skill_categories,
        'experience': extra_experience,
    }
    return render(request, 'main/index.html', context)

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        if name and email and message:
            subject = f"New Portfolio Message from {name}"
            email_message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
            try:
                send_mail(
                    subject,
                    email_message,
                    settings.EMAIL_HOST_USER, # From email
                    ['harunabib26@gmail.com'], # To email
                    fail_silently=False,
                )
                return JsonResponse({'status': 'success', 'message': 'Thank you for reaching out! Your message has been sent.'})
            except Exception as e:
                print(f"Error sending email: {e}")
                return JsonResponse({'status': 'error', 'message': 'Oops! Something went wrong while sending the email. Please try again later.'}, status=500)
        
        return JsonResponse({'status': 'error', 'message': 'All fields are required.'}, status=400)
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'}, status=405)
