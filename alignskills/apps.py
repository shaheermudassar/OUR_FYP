# Importing the AppConfig class from Django's apps module
from django.apps import AppConfig

# Defining the configuration class for the 'alignskills' application
class AlignskillsConfig(AppConfig):
    # Setting the default type for auto-generated primary keys in the database to 'BigAutoField'
    default_auto_field = 'django.db.models.BigAutoField'
    
    # Setting the name of the application to 'alignskills'
    name = 'alignskills'


# Importing the AppConfig class from Django's apps module
from django.apps import AppConfig

# Defining the configuration class for the 'alignskills' application again
class AlignskillsConfig(AppConfig):
    # Setting the default type for auto-generated primary keys in the database to 'BigAutoField'
    default_auto_field = 'django.db.models.BigAutoField'
    
    # Setting the name of the application to 'alignskills'
    name = 'alignskills'

    # Overriding the ready() method to initialize the signals
    def ready(self):
        # Importing the signals module within the 'alignskills' app to make sure signals are registered when the app is ready
        import alignskills.signals
