from django.http import HttpResponseForbidden

def role_required(*roles):
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            if request.user.role not in roles:
                return HttpResponseForbidden("Доступ запрещен")
            return view_func(request, *args, **kwargs)
        return wrapper
    return decorator