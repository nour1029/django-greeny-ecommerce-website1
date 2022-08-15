from .models import Profile


def user_info(request):
    profile = Profile.objects.get(user=request.user)

    return {'profile': profile}
