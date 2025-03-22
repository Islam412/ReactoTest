from django.shortcuts import render , redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


from .models import User , Account , KYC
from .forms import UserRegisterForm , KYCForm


# Create your views here.


def register_view(request):
    if request.user.is_authenticated:
        messages.warning(request, f"You are already logged in.")
        return redirect("userauths:account")

    
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data['username']

            messages.success(request, f'Account created for {username}! You are now able to log in.')

            new_user = authenticate(
                username = form.cleaned_data['email'],
                password = form.cleaned_data['password1'],
            )

            login(request, new_user)
            return redirect("userauths:account")
        

    else:
        
        form = UserRegisterForm()

    context = {
        'form': form,
    }

    return render(request,'userauths/sign-up.html', context)



def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(email=email, password=password)

        try:
            user = User.objects.get(email=email)
            user = authenticate(request, email=email, password=password)

            if user is not None: # if there is a user
                login(request, user)
                messages.success(request, "You are logged.")
                return redirect("userauths:account")
            else:
                messages.warning(request, "Username or password does not exist")
                return redirect("userauths:sign-in")
        except:
            messages.warning(request, "User does not exist")

    if request.user.is_authenticated:
        messages.success(request, 'You are already logged in')
        return redirect("userauths:account")

    return render(request, 'userauths/sign-in.html')


def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out')
    return redirect('userauths:sign-in')



@login_required
def kyc_registration(request):
    user = request.user
    account = Account.objects.get(user=user)

    try:
        kyc = KYC.objects.get(user=user)
    except:
        kyc = None
    
    if request.method == "POST":
        form = KYCForm(request.POST, request.FILES, instance=kyc)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = user
            new_form.account = account
            new_form.save()
            messages.success(request, "KYC Form submitted successfully, In review now.")
            return redirect("core:home")
    else:
        form = KYCForm(instance=kyc)
    context = {
        "account": account,
        "form": form,
        "kyc": kyc,
    }
    return render(request, "userauths/kyc-form.html", context)



@login_required
def account(request):
    if request.user.is_authenticated:
        try:
            kyc = KYC.objects.get(user=request.user)
        except:
            messages.warning(request, "You need to submit your kyc")
            return redirect("userauths:kyc-registration")
        
        account = Account.objects.get(user=request.user)
    else:
        messages.warning(request, "You need to login to access the dashboard")
        return redirect("userauths:sign-in")

    context = {
        "kyc":kyc,
        "account":account,
    }
    return render(request, "userauths/account.html", context)



@login_required
def delete_account(request):
    user = request.user
    if request.method == "POST":
        Account.objects.filter(user=user).delete()
        KYC.objects.filter(user=user).delete()

        user.delete()
        messages.success(request, "Your account has been deleted successfully.")
        return redirect("userauths:sign-in")

    return render(request, "userauths/delete_account.html")
