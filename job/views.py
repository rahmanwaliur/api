from django.shortcuts import render
from django.views.generic import View
from .models import Job
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

class JobView(View):

    def get(self, request, *args, **kwargs):
        jobId = request.GET["jobId"]
        jobStatus = request.GET["jobStatus"]
        job = Job.objects.filter(job_id=jobId).get()
        job.status = jobStatus 
        job.save()
        response_data = {"saved": True }
        return HttpResponse(json.dumps(response_data), content_type="application/json")

class CreateJob(View):

    def get(self, request, *args, **kwargs):
        jobId = request.GET["jobId"]
	job, created = Job.objects.get_or_create(id=request.GET["id"], defaults={"id": request.GET["id"], "job_id": jobId})
        job.status = "Pending"
        job.save()
        response_data = {"saved": True }
        return HttpResponse(json.dumps(response_data), content_type="application/json")
