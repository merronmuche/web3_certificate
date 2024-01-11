from django.shortcuts import render
from app.models import Trainee


from django.shortcuts import render

def view_certificate(request, trainee_id):

    trainee = Trainee.objects.get(pk = trainee_id)
    context = {
        'trainee_name': trainee.name,
        'course_name': trainee.course,
        'certified_date': trainee.date_certified,
        'certificate': trainee.certificate
    }

    # Render and return the template
    return render(request, 'certificates/view_certificate.html', context)
