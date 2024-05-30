from django.shortcuts import redirect


def role_required(role):
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            if request.user.is_authenticated and (
                request.user.is_superuser
                or (role == "doctor" and request.user.is_doctor)
                or (role == "client" and request.user.is_client)
            ):
                return view_func(request, *args, **kwargs)
            else:
                return redirect("about")

        return wrapper

    return decorator
