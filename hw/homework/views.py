
from django.shortcuts import render
from django.views import View

from homework.forms import WriteLineForm
from homework.models import Student

class MainView(View):
    def get(self, request):
        context = {
            'form': WriteLineForm(),
            'title': "Form",
        }
        return render(request, 'form.html', context)


    def post(self, request):
        form = WriteLineForm(request.POST)
        if form.is_valid():
            Student.objects.create(
                firstname=form.cleaned_data.get("firstname"),
                lastname=form.cleaned_data.get("lastname"),
                age=form.cleaned_data.get("age")
            )
            context = {
                "users": Student.objects.all(),
                "title": "Profile"
            }
            # data['title'] = "Profile"
            return render(request, 'profile.html', context)


