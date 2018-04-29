from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def change_pass(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user = request.user)
        form.new_password1.help_text = ""
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/userprof/')
    else:
         form = PasswordChangeForm(user=request.user)
    args = {'form': form}
    return render(request, 'password/password.djt', args)
