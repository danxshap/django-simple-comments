import importlib

from django.conf import settings
from django.contrib.comments.models import Comment

from simple_comments.forms import SimpleCommentForm

def get_form():
    """
    Tells django to use the simple_comments form or optionally a user-defined form
    (which should subclass the SimpleCommentForm) instead of the stock comments form
    """
    if hasattr(settings, 'SIMPLE_COMMENTS_FORM_MODULE') and \
        hasattr(settings, 'SIMPLE_COMMENTS_FORM_CLASS_NAME'):
        form_module = importlib.import_module(settings.SIMPLE_COMMENTS_FORM_MODULE)
        form_class = getattr(form_module, settings.SIMPLE_COMMENTS_FORM_CLASS_NAME)

    else:
        form_class = SimpleCommentForm

    return form_class

def get_model():
    """
    Tells django to optionally use a user-defined comment model
    instead of the stock comments model
    """
    if hasattr(settings, 'SIMPLE_COMMENTS_MODELS_MODULE') and \
        hasattr(settings, 'SIMPLE_COMMENTS_MODEL_NAME'):
        model_module = importlib.import_module(settings.SIMPLE_COMMENTS_MODELS_MODULE)
        model_class = getattr(model_module, settings.SIMPLE_COMMENTS_MODEL_NAME)

    else:
        model_class = Comment

    return model_class

