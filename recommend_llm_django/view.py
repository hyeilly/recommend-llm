from django.http import JsonResponse
from user_core.services import get_user_list, get_user_by_id

def user_list_view(request):
    users = get_user_list()
    return JsonResponse([user.dict() for user in users], safe=False)

def user_detail_view(request, user_id):
    try:
        user = get_user_by_id(user_id)
        return JsonResponse(user.dict())
    except ValueError:
        return JsonResponse({"error": "User not found"}, status=404)
