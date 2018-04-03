from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect

# Create your views here.
def change_pass(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user = request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/userprof/')
        else:
            return redirect('/password/')
    else:
         form = PasswordChangeForm(user=request.user)
    args = {'form': form}
    return render(request, 'password/password.html', args)
