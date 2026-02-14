from django.shortcuts import render
from .models import Toogle
from .forms import ToogleForm, UserRegistrationForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
# Create your views here.
def index(request):
    return render(request, 'index.html')


def toogle_list(request):
    toogles = Toogle.objects.all().order_by('-created_at')
    return render(request,'toogle_list.html', {'toogles':toogles})

@login_required
def toogle_create(request):
    if request.method == "POST":
      form = ToogleForm(request.POST, request.FILES)
      if form.is_valid():
        toogle = form.save(commit=False)
        toogle.user = request.user
        toogle.save()
        return redirect('toogle_list')

    else:
        form = ToogleForm()
    return render(request, 'toogle_form.html',{'form':form})

@login_required
def toogle_edit(request, toogle_id):
    toogle = get_object_or_404(Toogle, pk=toogle_id, user=request.user)

    if request.method == 'POST':
        form = ToogleForm(request.POST, request.FILES, instance=toogle)
        if form.is_valid():
            toogle = form.save(commit=False)
            toogle.user = request.user
            toogle.save()
            return redirect('toogle_list')
    else:
        form = ToogleForm(instance=toogle)

    return render(request, 'toogle_form.html', {'form': form})

@login_required
def toogle_delete(request, toogle_id):
    toogle = get_object_or_404(Toogle, pk=toogle_id, user=request.user)

    if request.method == 'POST':
        toogle.delete()
        return redirect('toogle_list')

    return render(request, 'toogle_confirm_delete.html', {'toogle': toogle})

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('toogle_list')
    else:
        form = UserRegistrationForm()

    return render(request, 'registration/register.html', {'form': form})

