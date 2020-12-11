from django.shortcuts import render

# Create your views here.

from django.contrib.auth.models import User, Group
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy


class UserSignupView(CreateView):
    model = User
    fields = ['username', 'password', 'email', 'first_name', 'last_name']

    def form_valid(self, form):
        form.save()
        group = Group.objects.get(name='Game Catalogue Member')
        form.instance.groups.set([group])
        return super(UserSignupView, self).form_valid(form)

    success_url = reverse_lazy('sign-up-success')


def user_signup_success(request):
    # Number of collections
    user_number = User.objects.all().count()

    context = {
        'user_number': user_number,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'auth/user_signup_success.html', context = context)
