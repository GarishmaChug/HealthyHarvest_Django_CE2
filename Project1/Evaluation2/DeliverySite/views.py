from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.core.paginator import Paginator
from django.db.models import Q
from .models import DeliveryPersonApplication
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.admin.views.decorators import staff_member_required

# Admin check decorator
# def admin_required(view_func):
#     return user_passes_test(lambda u: u.is_staff)(view_func)

# User application form
def apply_for_job(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        resume = request.FILES.get('resume')

        if name and email and phone and resume:
            DeliveryPersonApplication.objects.create(
                name=name,
                email=email,
                phone=phone,
                resume=resume
            )
            return render(request, 'thanks.html')

    return render(request, 'apply.html')


# Admin-only view of applications with pagination + search
# @admin_required

@staff_member_required


def admin_applications_view(request):
    query = request.GET.get('search', '')

    applications = DeliveryPersonApplication.objects.all().order_by('-applied_on')

    if query:
        applications = applications.filter(
            Q(name__icontains=query) |
            Q(email__icontains=query) |
            Q(phone__icontains=query)
        )

    paginator = Paginator(applications, 5)  # Show 5 per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'admin_applications.html', {
        'page_obj': page_obj,
    })


# Admin-only status update
# @admin_required
def update_status(request, pk, status):
    app = get_object_or_404(DeliveryPersonApplication, pk=pk)
    if status in ['accepted', 'rejected']:
        app.status = status
        app.save()
    return redirect('admin_applications')



def logout_view(request):
    logout(request)
    return redirect('login')