import importlib

from django.contrib.auth.decorators import login_required  
from django.views.decorators.http import require_POST 
from django.shortcuts import get_object_or_404, redirect
from django.conf import settings
from django.contrib import comments
from django.http import Http404
from django.contrib import messages
from django.contrib.comments.signals import comment_was_posted
import django.contrib.comments.views.comments as django_comments
import django.contrib.comments.views.moderation as django_comments_moderation

@login_required
def post(request, next=None, using=None):
    """
    This wrapper view only serves to require login for posting comments
    """
    return django_comments.post_comment(request, next, using)    


@login_required
@require_POST
def delete(request):
    """
    Wrapper to make sure the user deleting a comment is the user who originally posted that comment.  Also gets around moderation permissions by calling perform_delete() directly.
    """
    comment = get_object_or_404(comments.get_model(), pk=request.POST.get('comment_id'), site__pk=settings.SITE_ID)
    
    if comment.user == request.user:
        django_comments_moderation.perform_delete(request, comment)
        messages.success(request, 'Your comment has been deleted')  

        # should add some error handling here if 'next' is not in request.POST
        return redirect(request.POST.get('next'))

    else:
        raise Http404

def after_comment_has_been_posted(sender, comment, request, **kwargs):
    """
    Function to run when the comments app fires the comment_was_posted signal.
    Can be configured to run some function called "after_comment_has_been_posted"
    defined by the user and in a module specified by the SIMPLE_COMMENTS_SIGNAL_MODULE setting
    """
    if hasattr(settings, 'SIMPLE_COMMENTS_SIGNAL_MODULE'):
        signal_module = importlib.import_module(settings.SIMPLE_COMMENTS_SIGNAL_MODULE)
        signal_module.after_comment_has_been_posted(sender, comment, request, **kwargs)

    else:
        messages.success(request, 'Your comment has been posted!')

comment_was_posted.connect(after_comment_has_been_posted)
