from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q
from helper_app.models import*
import bcrypt


def index(request):

    return render(request, 'login.html')

def create_user(request):
    if request.method == "POST":
        
        errors = User.objects.registration_validator(request.POST)
        if len(errors) > 0:
            for key,value in errors.items():
                messages.error(request, value)
            return redirect('/')

        hash_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        
        new_user = User.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email'],
            password = hash_pw
        )
        request.session['logged_user'] = new_user.id

        return redirect('/user/hello')
    return redirect("/")
    # localhost:8000/dashboard

def login(request):
    if request.method == "POST":
        user = User.objects.filter(email = request.POST['email'])

        if user:
            log_user = user[0]

            if bcrypt.checkpw(request.POST['password'].encode(), log_user.password.encode()):
                request.session['logged_user'] = log_user.id
                return redirect('/user/hello')
        messages.error(request, "Email or password are incorrect.")
            
    return redirect("/")

def dashboard(request):
    logged_user = User.objects.get(id=request.session['logged_user'])
    context = {
        'logged_user': logged_user,
        'all_jobs': Job.objects.filter(~Q(added_job=request.session['logged_user'])),
        'logged_user_jobs': Job.objects.filter(added_job = request.session['logged_user'])
        }
        
    return render(request, 'jobs.html', context)

def create_job(request):
    if request.method == 'POST':
        errors = Job.objects.basic_validator(request.POST)
        
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect(f'/user/job')
                
    
        user = User.objects.get(id=request.session['logged_user'])
        print(request.POST['category'])
        new_job = Job.objects.create(
            title = request.POST['title'],
            description = request.POST['description'],
            location = request.POST['location'],
            category = request.POST['category'],
            user_job = user
                )
        user.added_jobs.add(new_job)
    return redirect(f'/user/hello')

def add_job(request, job_id):
    if 'logged_user' not in request.session:
        messages.error(request, "Please register or log in first")
        return redirect('/')
    logged_user = User.objects.get(id=request.session['logged_user'])
    job = Job.objects.get(id=job_id)
    logged_user.added_jobs.add(job)
    

    return redirect(f'/user/hello')

def move_job(request, job_id):
    if 'logged_user' not in request.session:
        messages.error(reques, "Please register or log in first")
        return redirect('/')
    logged_user = User.objects.get(id=request.session['logged_user'])
    job = Job.objects.get(id=job_id)
    job.added_job.remove(logged_user)


    return redirect(f'/user/hello')

def job(request):
    context = {
        'logged_user' : User.objects.get(id=request.session['logged_user']),
        'all_jobs': Job.objects.all()

    }

    return render(request, 'create_job.html', context)

def edit_job(request, job_id):
    
    job = Job.objects.get(id=job_id)
    context = {
        'logged_user' : User.objects.get(id=request.session['logged_user']),
        'job': job
        
        
    }
    
    return render(request, 'edit_job.html', context)

def updated_job(request, job_id):
    if request.method == 'POST':
        errors = Job.objects.basic_validator(request.POST)
        
    if len(errors) > 0:
        
        for key, value in errors.items():
            messages.error(request, value)
        
        return redirect(f'/job/{job_id}/edit')
    else:
        update_job = Job.objects.get(id=job_id)
        update_job.title = request.POST['title']
        update_job.description = request.POST['description']
        update_job.location = request.POST['location']
        update_job.category = request.POST['category']
        update_job.save()
        messages.success(request, "Job successfully updated")

        
    return redirect(f'/user/hello')

def view_job(request, job_id):
    context = {
        'logged_user' : User.objects.get(id=request.session['logged_user']),
        'job' : Job.objects.get(id=job_id),

    }
    return render(request, 'work.html', context)

def delete_job(request, job_id):
    if 'logged_user' not in request.session:
        messages.error(reques, "Please register or log in first")
    job = Job.objects.get(id=job_id)
    job.delete()
    return redirect(f'/user/hello')

def logout(request):
    request.session.flush()
    return redirect('/')


# Create your views here.
