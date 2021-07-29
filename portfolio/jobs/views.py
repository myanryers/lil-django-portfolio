from django.shortcuts import render, get_object_or_404
from django.http.response import Http404

from .models import Job

def home(request):
    jobs = Job.objects.all()
    return render(request, 'jobs/home.html', {'jobs': jobs})


def job_detail(request, job_id):
    """Shows details on Job `job_id`."""
    job = get_object_or_404(Job, pk=job_id)
    # try:
    #     job = Job.objects.get(id=job_id)
    # except Job.DoesNotExist:
    #     raise Http404(f'No job found for {job_id}')
    return render(request, 'jobs/job_detail.html', {'job': job})
