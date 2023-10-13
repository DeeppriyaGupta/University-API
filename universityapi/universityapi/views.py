
from django.http import JsonResponse
def homepage(request):
    home_message= {"message": "This is an api to manage students in universities and it only respond in JSON format"}
    return JsonResponse(home_message)