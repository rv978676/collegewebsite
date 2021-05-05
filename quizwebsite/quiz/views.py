from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse
from quiz.models import users,subject,question,quey
from datetime import date

# Create your views here.
def Home(request):
    M_id = request.session['member_id']
    user=(users.objects.get(id=M_id))
    details={
        "user":user,
        "subjects":subject.objects.filter(department="IT",semester=user.current_sem),
        }
    # print(details.subject.name)
    return render(request,"Home.html",context=details)
    # return HttpResponse(user.emailid)

def logout(request):
    del (request.session['member_id'])
    return HttpResponse("logged out")

def Login(request):
    # user=users.objects.get(emailid="rajveer@sal.com")
    # return HttpResponse("user.password")
    if request.method=="POST":
        email=request.POST['emailid']
        user=users.objects.get(emailid=email)
        if request.POST['password']==user.password:
            request.session['member_id'] = user.id
            return redirect("/Home")

    return render(request,"login.html")
    # return HttpResponse("login")

def Register(request):
    if request.method=="POST":
        # =request.POST['']Enrollment Number,Department,password-repeat
        # try:
        u=users(emailid=request.POST['emailid'],firstname=request.POST['firstname'],lastname=request.POST['lastname'],password=request.POST['password'],enrollment_no=request.POST['Enrollment Number'],current_sem=request.POST['Current sem'],is_student=True,is_staff=False)
        u.save()
        
        return HttpResponse("user created")
        # return redirect('/login')

    return render(request,"register.html")
# def Exam(request):
    # return HttpResponse("exam")

def Exam(request, id):
    if request.session['member_id']:
        if request.method=="POST":
            submited_response=list()
            for key,value in request.POST.items():
                print(key,"==>",value)
                submited_response.append(key+":"+value)
            submited_response=submited_response[1:]
            print(submited_response)# for each in (question.objects.filter(exam_code=id).all()):
            #     print(each)
            #     print(request.POST[each.number])
            user=(users.objects.get(id=M_id))
            return HttpResponse("submitted")

        elif request.method=="GET":
            details={
                "question":question.objects.filter(exam_code=id).all(),
                "id": id,
                "name":subject.objects.get(code=id)
            }
            return render(request,"quiz.html",context=details)
    else:
        return redirect('Login')

def Subject(request, id):
    if request.session['member_id']:
        if request.method=="POST":
            pass
        elif request.method=="GET":
            subjects=subject.objects.get(code=id)
            details={
                "subject":subjects,
                "id": id,
                # "chapter":chapters,
            }
            return render(request,"subject.html",context=details)
    else:
        return redirect("login")

def Department(request):
    return render(request,"department.html")

def queries(request):
    if request.method=="POST":
        print(request.POST['email'])
        d=date.today()
        q=quey(email=request.POST['email'],name=request.POST['Name'],description=request.POST['comment'],timestamp=d)
        q.save()
        return HttpResponse("submitted")
    return render(request,"about.html")