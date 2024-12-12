from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib import messages
from django.views.decorators.cache import never_cache
from .models import ContactMessage, SiteStatistics
import os

# Create your views here.

def get_or_create_site_stats():
    """
    מחזיר את אובייקט הסטטיסטיקות הקיים, או יוצר אחד חדש אם לא קיים
    """
    stats, created = SiteStatistics.objects.get_or_create(pk=1)
    if created:
        # אם זה אובייקט חדש, שמור אותו
        stats.save()
    return stats

@never_cache  # מונע קאש של הדף כך שכל טעינה תיספר
def home(request):
    """דף הבית של האתר"""
    stats = get_or_create_site_stats()
    stats.increment_site_visit()
    context = {
        'title': 'Commander Persky - דף הבית',
        'game_name': 'Commander Persky',
        'game_version': '1.0 Demo',
        'total_levels': 5
    }
    return render(request, 'home.html', context)

@never_cache
def game_details(request):
    stats = get_or_create_site_stats()
    stats.increment_site_visit()
    
    # יצירת רשימה של טווח תמונות
    screenshot_range = [str(i) for i in range(1, 16)]
    
    # חלוקת התמונות ל-3 שורות של 5 תמונות
    screenshot_rows = [
        screenshot_range[0:5],   # שורה ראשונה: תמונות 1-5
        screenshot_range[5:10],  # שורה שנייה: תמונות 6-10
        screenshot_range[10:15]  # שורה שלישית: תמונות 11-15
    ]
    
    # הגדרת סרטונים
    # video_list = [
    #     {'filename': 'Crater.mp4', 'title': 'Crater Level'},
    #     {'filename': 'Desert.mp4', 'title': 'Desert Level'},
    #     {'filename': 'Iceland.mp4', 'title': 'Iceland Level'}
    # ]
    
    # חלוקת סרטונים לשורות
    video_rows = []  # כרגע שורה אחת, ניתן להרחיב בעתיד
    
    context = {
        'description': 'Commander Persky is an adventure game in style of platform games from the early 90s',
        'genre': 'Platform Game',
        'engine': 'DanoGameLab',
        'credit': 'Developed by Dr. Dan Nirel',
        'screenshot_range': screenshot_range,
        'screenshot_rows': screenshot_rows,
        'video_rows': video_rows
    }
    return render(request, 'game_details.html', context)

@never_cache
def download(request):
    stats = get_or_create_site_stats()
    stats.increment_site_visit()
    stats.increment_game_download()
    download_url = 'https://drive.google.com/uc?id=1ehNIn9uYc1oMVAu1U4mrWO14zFr76sDF'
    return redirect(download_url)

@never_cache
def support(request):
    """דף תמיכה"""
    stats = get_or_create_site_stats()
    stats.increment_site_visit()
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        # שמירת ההודעה במסד הנתונים
        contact_message = ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        
        # שליחת אימייל
        from django.core.mail import send_mail
        
        try:
            send_mail(
                f'Contact Form: {subject}',
                f'Name: {name}\nEmail: {email}\n\nMessage:\n{message}',
                'commanderpersky@gmail.com',
                ['commanderpersky@gmail.com'],
                fail_silently=False,
            )
            messages.success(request, 'Your message was sent successfully!')
        except Exception as e:
            # גם אם יש שגיאה בשליחת אימייל, נציג הודעת הצלחה
            messages.success(request, 'Your message was sent successfully!')
        
        return redirect('support')
    
    context = {
        'title': 'תמיכה - Commander Persky',
        'support_email': 'commanderpersky@gmail.com',
        'discord_link': 'https://discord.gg/commanderpersky',
        'twitter_link': 'https://twitter.com/CommanderPersky',
        'system_requirements': {
            'min_os': 'Windows 7 or later',
            'min_ram': '2 GB RAM',
            'min_storage': '200 MB available space',
            'recommended_cpu': '2.5 GHz Quad Core'
        }
    }
    return render(request, 'support.html', context)

@never_cache
def faq(request):
    """FAQ & Tips page"""
    stats = get_or_create_site_stats()
    stats.increment_site_visit()
    context = {
        'title': 'FAQ & Tips - Commander Persky',
    }
    return render(request, 'faq.html', context)

@never_cache
def terms_and_conditions(request):
    """Terms and Conditions page"""
    stats = get_or_create_site_stats()
    stats.increment_site_visit()
    context = {
        'title': 'Terms and Conditions - Commander Persky',
    }
    return render(request, 'terms_and_conditions.html', context)
