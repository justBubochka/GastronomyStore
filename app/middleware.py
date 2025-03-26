from django.shortcuts import redirect

# Middleware to check if the user is authenticated on every page
class AuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated and request.path not in ["/login/", "/register/"]:
            return redirect("/login/")
        return self.get_response(request)