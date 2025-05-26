# Importing the 'UserStats' model from the current app's models
from .models import UserStats

# Defining the 'user_stats' function that will return a dictionary with statistical data
def user_stats(request):
    # Fetching the count of active students from the 'UserStats' model where the 'is_active' field is True
    return {
        'active_students': UserStats.objects.filter(is_active=True).count(),
        
        # Fetching the count of graduate students from the 'UserStats' model where the 'is_graduate' field is True
        'graduate_students': UserStats.objects.filter(is_graduate=True).count(),
        
        # Fetching the count of certified students from the 'UserStats' model where the 'is_certified' field is True
        'certified_students': UserStats.objects.filter(is_certified=True).count(),
    }
