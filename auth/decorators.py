from django.core.exceptions import PermissionDenied

def lecture_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.has_perm('auth.can_view_students_detail'):
            raise PermissionDenied
        return view_func(request, *args, **kwargs)
    return _wrapped_view
