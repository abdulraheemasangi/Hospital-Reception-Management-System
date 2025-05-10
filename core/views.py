from django.shortcuts import render,redirect
from .models import patient_register
from django.contrib.auth.decorators import login_required
from django.db.models import Q


# Create your views here.
@login_required(login_url='login_')
def home(request):
    return render(request,"home.html",)


@login_required(login_url='login_')
def patient_register_form(request):
    if request.method=='POST':
        name=request.POST['full_name']
        phone=request.POST['phone_number']
        patient_add=request.POST['address']
        patient_age=request.POST['age']
        patient_gender=request.POST['gender']
        patient_state=request.POST['state']
        patient_aadhaar=request.POST['aadhaar_number']
        patient_email=request.POST['email']
        patient_heath_prob=request.POST['health_problem']
        visit_date=request.POST['date_of_visit']
        
    # if 'full_name' in request.GET:
    #     name=request.GET['full_name']
    #     phone=request.GET['phone_number']
    #     patient_add=request.GET['address']
    #     patient_age=request.GET['age']
    #     patient_gender=request.GET['gender']
    #     patient_state=request.GET['state']
    #     patient_aadhaar=request.GET['aadhaar_number']
    #     patient_email=request.GET['email']
    #     patient_heath_prob=request.GET['health_problem']
    #     visit_date=request.GET['date_of_visit']
        
        patient_register.objects.create(
            full_name=name,
            phone_number=phone,
            address=patient_add,
            age=patient_age,
            gender=patient_gender,
            state=patient_state,
            aadhaar_number=patient_aadhaar,
            email=patient_email,
            health_problem=patient_heath_prob,
            date_of_visit=visit_date
            )
    return render(request,"patient_register.html")



@login_required(login_url='login_')
def patient_list(request):

    patientdata=patient_register.objects.all()

    # search

    querry=request.GET.get('querry')
    if querry :
        search=patient_register.objects.filter(
            Q(full_name__icontains=querry) | Q(phone_number__icontains=querry) | Q(email__icontains=querry) | Q(age__icontains=querry) | Q(gender__icontains=querry) | Q(health_problem__icontains=querry)
        )
    else:
        search=patient_register.objects.all()

    context={

        'data':patientdata,
        'search':search 
    }

    return render(request,'patient_list.html',context)

# Details or Read function


@login_required(login_url='login_')
def patient_details(request, pk):



    patient=patient_register.objects.get(id=pk)

    print(patient,pk)

    context = {'data': patient}

    return render(request, 'patient_details.html', context)



def about(request):
    
    return render(request,'about.html')

