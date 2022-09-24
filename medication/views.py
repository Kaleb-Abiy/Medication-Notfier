from django.shortcuts import render
from .models import Medications
from django.contrib.auth.decorators import login_required
from .forms import MedicationForm
from django.utils import timezone
from django.core.mail import send_mail
import datetime



def home(request):
    return render(request, 'medication/home.html')

@login_required()
def dashboard(request):
    user = request.user
    meds = user.medications.all()


    leng = len(meds)
    if meds.count() <= 1:
        medication = meds[0]

    print(medication)
    context = {
        'meds': meds,
        'medication': medication,
        'leng': leng
    }
    return render(request, 'medication/dashboard.html', context)



@login_required()
def index(request, id):
    med = Medications.objects.get(id=id)
    notf_times = med.get_notf()

    type_of = type(notf_times)
    t = (type_of == datetime.time)
    context = {
        'med': med,
        'notf_times': notf_times,
        't': t
    }
    return render(request, 'medication/index.html', context)

@login_required
def add_medication(request):
    form = MedicationForm()
    if request.method == 'POST':
        form = MedicationForm(request.POST)
        if form.is_valid():
            obj= form.save(commit=False)
            obj.user = request.user
            obj.save()

    context = {
        'form': form
    }
    return render(request, 'medication/add_med.html', context)



def reminder(request):
    meds = Medications.objects.filter(user=request.user)
    big_notf = []

    if len(meds) <= 1:
        medication = meds[0]
        notf_times = medication.get_notf()
        if timezone.now() == notf_times:
             send_mail(
                    'Take medication!',
                    f'Hello, {request.user.username} please take ur medication now',
                    'from@example.com',
                    [f'{request.user.email}'],
                    fail_silently=False,
                )
        else:
            print('no')

    else:
        for m in meds:
            notf_times = m.get_notf()
            big_notf.append(notf_times)

        for i in big_notf:
            for j in i:
                if timezone.now() == j:
                    send_mail(
                        'Take medication!',
                        f'Hello, {request.user.username} please take ur medication now',
                        'from@example.com',
                        [f'{request.user.email}'],
                        fail_silently=False,
                    )
                else:
                    print('no')
    return render(request, 'medication/reminder.html')