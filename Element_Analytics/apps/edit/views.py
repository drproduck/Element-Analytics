from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserChangeForm
from apps.edit.forms import EditProfileForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance = request.user)

        if form.is_valid():
            form.save()
            return redirect('/userprof/')
    else:
        form = EditProfileForm(instance=request.user)
    args = {'form': form}
    return render(request,'edit/edit.djt', args)
