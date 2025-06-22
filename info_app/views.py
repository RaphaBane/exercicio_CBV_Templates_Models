from datetime import datetime
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from info_app.models import Person

# Create your views here.

class WelcomeView(View):
    def get(self, request):
        response = {"message": "Welcome to the Personal Info API!"}
        return JsonResponse(response)

class GoodbyeView(View):
    def get(self, request):
        response = {"message": "Goodbye, see you next time"}
        return JsonResponse(response)

class TimeView(View):
    def get(self, request):
        current_time = datetime.now().strftime("%H:%M:%S")
        response = {"time": current_time}
        return JsonResponse(response)

class GreetView(View):
    def get(self, request):
        name = request.GET.get('name', 'Stranger')
        response = {"message": f"Hello, {name}!", }
        return JsonResponse(response)

class AgeCategoryView(View):
    def get(self, request):
        age_param = request.GET.get('age')

        if age_param is None:
            return JsonResponse({"error": "Missing 'age' parameter."})

        age = int(age_param)

        if 0 <= age <= 12:
            return JsonResponse({"category": "Child"})
        elif 13 <= age <= 17:
            return JsonResponse({"category": "Teenager"})
        elif 18 <= age <= 59:
            return JsonResponse({"category": "Adult"})
        elif age >= 60:
            return JsonResponse({"category": "Senior"})
        else:
            return JsonResponse({"error": "Invalid 'age' value."}, status=400)

class SumView(View):
    def get(self, request, num1, num2):
        try:
            n1 = int(num1)
            n2 = int(num2)
        except ValueError:
            return JsonResponse({"error": "Invalid input, please provide two integers."}, )

        return JsonResponse({"sum": n1 + n2})

class AboutView(View):
    def get(self, request):
        context = {'site_name': 'Personal Info Project',
                   'site_description': 'Um projeto que utiliza Django',
                   'current_year': datetime.now().year}

        return render(request, 'info_app/about.html', context)

class PeopleView(View):
    def get(self, request):
        people = Person.objects.all()
        data = [{'name': p.name, 'age': p.age} for p in people]
        return JsonResponse({'people': data})