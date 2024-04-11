from django.shortcuts import redirect, render
from .models import ContactUSModel
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def ContactUsAPI(request):
    return render(request, 'contact_us.html')

def ContactUSData(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        rating = request.POST.get('rating')  # Here, rating will be 'one', 'two', 'three', 'four', or 'five'
        feedback = request.POST.get('feedback')
        user = request.user  # Here, rating will be 'one', 'two', 'three', 'four', or 'five'
        rating_to_stars = {
                'one': '*',
                'two': '**',
                'three': '***',
                'four': '****',
                'five': '*****'
            }
            
        stars = rating_to_stars.get(rating, '*')  # Default to one star if rating is not recognized
        
        feedback_data = ContactUSModel(
            user = user,
            name=name, 
            rating=stars, 
            feedback=feedback
            )
        feedback_data.save()
            
        return render(request, 'contact_us.html')  # Redirect to a home page after submission
    return render(request, 'home.html')
