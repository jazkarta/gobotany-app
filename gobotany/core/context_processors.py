from gobotany import settings

def gobotany_specific_context(request):
    context_extras = {
        'in_production': settings.IN_PRODUCTION,
        'dev_features': settings.DEV_FEATURES,
        'production_js': settings.S3_STATIC or settings.IN_PRODUCTION,
        }
    return context_extras
