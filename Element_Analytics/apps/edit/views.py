from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserChangeForm

# Create your views here.
def edit_profile(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance = request.user)

        if form.is_valid():
            form.save()
            return redirect('/userprof/')
    else:
        form = UserChangeForm(instance=request.user)
    args = {'form': form}
    return render(request,'edit/edit.html', args)