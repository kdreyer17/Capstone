from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import UserRegisterForm
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        # print (form.errors.as_data())
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.email = form.cleaned_data.get('username')+'@mail.wou.edu'
            print(user.email)
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate Your Account'
            message = render_to_string('users/acc_activate_email.html', {  
                    'user': user,  
                    'domain': current_site.domain,  
                    'uid': urlsafe_base64_encode(force_bytes(user.id)),  
                    'token': account_activation_token.make_token(user),  
                })    
            #to_email = form.cleaned_data.get('email')
            email = EmailMessage(mail_subject, message, to =[user.email])
            email.send()
            messages.success(request, f'An activation link has been sent to your email account. Please activate your account to log in.')
            return redirect('login')
        else:
            messages.error(request, f'Error creating account!')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(id=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, f'Your account has been activated, you may now login!')
        return redirect('login')
        #return HttpResponse ('Thank you for your email confirmation. You may now login to your account.')
    else:
        return HttpResponse('Activation link is invalid!')

@login_required
def profile(request):
    return render(request, 'users/profile.html')
