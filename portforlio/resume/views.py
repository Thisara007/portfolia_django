from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.staticfiles.storage import staticfiles_storage
# Create your views here.
def home(request):
    return render (request,"home.html")

def about(request):
    return render (request,"about.html")

def project(request):
    project_details=[{"name":"GUI cal","details":"this is kasnbsa abssb"},
                     {"name":"Gjango Library","details":"this is kasnbsa abssb"},
                     {"name":"GREENLK","details":"this is kasnbsa abssb"}]
    return render (request,"projects.html",{"project":project_details})

def certification(request):
    certification_details=[{"name":"Python for Beginners","img":"UOM_logo.png","url":"https://open.uom.lk/lms/mod/customcert/verify_certificate.php","Issuer":"University of Moratuwa","Date":"2022 Jun"},
                     {"name":"Python Programing","img":"UOM_logo.png","url":"https://open.uom.lk/lms/mod/customcert/verify_certificate.php","Issuer":"University of Moratuwa","Date":"2022 Nov"},
                     {"name":"Python Django tutorial ","img":"simlilearn_logo.png","url":"https://verify.simplilearn.com/","Issuer":"Simplilearn.com","Date":"2024 Feb"},
                     {"name":"SQL basics ","img":"Hrank_logo.png","url":"https://www.hackerrank.com/certificates/iframe/3885cc880abe","Issuer":"HackerRank.com","Date":"2025 Feb"},
                   ]
    return render (request,"certification.html",{"certificates":certification_details})

def resume(request):
    resume_path="My_files/resume.pdf"
    resume_path=staticfiles_storage.path(resume_path)
    if staticfiles_storage.exists(resume_path):
        with open(resume_path,"rb") as resume_file:
            response=HttpResponse(resume_file.read(),content_type="application/pdf")
            response['Content-Disposition']='attachment';filename="resume.pdf"
            return response
    else:
        return HttpResponse("resume not found",status=404)
    
def contact(request):
    return render (request,"contact.html")