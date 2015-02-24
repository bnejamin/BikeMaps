# Script that initializes Django and makes Models, Forms, etc available to other scripts

# Settings should be either 'dev' for dev machine or 'prod' for server
def import_django(settings):
    import sys, os, django

    # Get Django settings and shell commands
    sys.path.append( os.path.dirname(os.getcwd()) )
    os.environ['DJANGO_SETTINGS_MODULE'] = 'VicBikeMap.settings.' + settings
    django.setup()
