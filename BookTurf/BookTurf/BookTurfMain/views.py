from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from .models import Turf_Profile
from .models import addmin
from .models import Turf_Pics
from django.http import HttpResponse, JsonResponse




# Create your views here.
def index(request):
    try:
        search = request.GET['searchInput']
        sports = request.GET['sports']
        time = request.GET['time']
        if(sports == "any"):
            sports = ""
        if(time == "any"):
            time = ""
        profiles = Turf_Profile.objects.filter(turf_name__icontains=search,turf_category_1__icontains=sports)
        pics = Turf_Pics.objects.all()
        first_pics = {}
        for profile in profiles:
            for pic in pics:
                if pic.turf_ref_id == profile.turf_id:
                    first_pics[profile.turf_id] = pic
                    break
        params = {"profiles": profiles, "pics": first_pics}
        return render(request, 'BookTurfMain/index.html', params)
    except Exception :
        profiles = Turf_Profile.objects.all()
        pics = Turf_Pics.objects.all()
        first_pics = {}
        for profile in profiles:
            for pic in pics:
                if pic.turf_ref_id == profile.turf_id:
                    first_pics[profile.turf_id] = pic
                    break

        params = {"profiles": profiles, "pics": first_pics}
        return render(request, 'BookTurfMain/index.html', params)

def sign_up(request):
    return render(request,'BookTurfMain/sign_up.html')

def sign_up_authenticate(request):
    try:
        if(request.method == 'POST'):
            name = request.POST['name']
            email = request.POST['email']
            phone = request.POST['phone']
            password = request.POST['password']
            hashed_password = make_password(password)
            terms = request.POST['terms']
            if terms == 'on' and len(phone) == 10 and email != '' and hashed_password != '' and name != '':
                user = User.objects.create(username=email,password=hashed_password,first_name=name,email=email)
                user.save()
                messages.success(request,'Signed up successfully, you can Login now')
                return redirect('/BookTurf/BookTurfMain/login_page/')
            else:
                messages.success(request,'Please agree to our terms and conditions AND enter a 10 digit phone number and fill up all the fields of form')
                return redirect('/BookTurf/BookTurfMain/sign_up/')
        else:
            messages.success(request,'Please type the correct page url')
            return redirect('/BookTurf/BookTurfMain/sign_up/')
    except Exception as e:
        messages.success(request,e)
        return render(request,'BookTurfMain/sign_up.html')

def login_page(request):
    return render(request,'BookTurfMain/login_page.html')

def login_page_authenticate(request):
    try:
        if(request.method == 'POST'):
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(username=email, password=password)

            if user is not None:
                # Authentication successful
                login(request, user)
                messages.success(request, 'You have successfully logged in')
                return redirect('/BookTurf/BookTurfMain/index/')
            else:
                # Authentication failed
                messages.success(request, 'Invalid email or password')
                return redirect('/BookTurf/BookTurfMain/login_page/')
        else:
            messages.success(request,'Please type the correct page url')
            return redirect('/BookTurf/BookTurfMain/login_page/')
    except Exception as e:
        messages.success(request,e)
        return redirect('/BookTurf/BookTurfMain/login_page/')

def turf_profile(request,id):
    profiles = Turf_Profile.objects.filter(turf_id=id)
    pics = Turf_Pics.objects.filter(turf_ref_id=id)
    if(pics.count() == 3 or pics.count() > 3):
        params = {"profiles": profiles, "pic0": pics[0],"pic1": pics[1],"pic2": pics[2]}
    elif(pics.count() == 2):
        params = {"profiles": profiles, "pic0": pics[0],"pic1": pics[1]}
    elif(pics.count() == 1):
        params = {"profiles": profiles, "pic0": pics[0]}
    elif(pics.count() == 0):
        params={"profiles": profiles}
    return render(request,'BookTurfMain/turf_profile.html',params)

def add_turf_profile(request):
    try:
        if(request.method == "GET"):
            params = {}
            return render(request,'BookTurfMain/add_turf_profile.html',params)
        elif(request.method == "POST"):
            username=request.POST['username']
            password=request.POST['password']
            admin = (addmin.objects.filter(addmin_username = username))
            if(admin[0] == None):
                messages.success(request, 'Wrong credentials')
                return render(request,'BookTurfMain/add_turf_profile.html')
            else:
                if(admin[0].addmin_password == password):
                    request.session['id'] = "AdminAuthenticated"
                    return render(request, 'BookTurfMain/add_turf_profile.html')
                else:
                    messages.success(request, 'Wrong credentials')
                    return render(request, 'BookTurfMain/add_turf_profile.html')
    except:
        messages.success(request, 'Wrong credentials')
        return render(request, 'BookTurfMain/add_turf_profile.html')

        # params = {"email":email ,"password":password}

def createTurf_Profile(request):
    if(request.method == 'POST'):
        turf_name = request.POST['turf_name']
        turf_rating =request.POST['turf_rating']
        turf_category_1 = request.POST['turf_category_1']
        turf_category_2 = request.POST['turf_category_2']
        turf_category_3 =request.POST['turf_category_3']
        turf_category_4 = request.POST['turf_category_4']
        turf_description =request.POST['turf_description']
        turf_rules_regulations = request.POST['turf_rules_regulations']
        turf_address = request.POST['turf_address']
        turf_ownerContact_number = request.POST['turf_ownerContact_number']
        # turf_reviews =request.POST['turf_reviews']
        turf_host_name =request.POST['turf_host_name']
        turf_map =request.POST['turf_map']
        turf_price =request.POST['turf_price']
        turf_picture =request.FILES.getlist('turf_picture')
        turf_weekday_base = request.POST['turf_weekday_base']
        turf_weekday_peak = request.POST['turf_weekday_peak']
        turf_friday_base = request.POST['turf_friday_base']
        turf_friday_peak =request.POST['turf_friday_peak']
        turf_saturday_base = request.POST['turf_saturday_base']
        turf_saturday_peak = request.POST['turf_saturday_peak']
        turf_sunday_base = request.POST['turf_sunday_base']
        turf_sunday_peak = request.POST['turf_sunday_peak']
        turf_field_1 = request.POST['turf_field_1']
        turf_field_2 = request.POST['turf_field_2']
        turf_field_3 = request.POST['turf_field_3']
        try:
            new_turf_profile = Turf_Profile(turf_name=turf_name,turf_rating=turf_rating,turf_category_1=turf_category_1,
                                             turf_category_2=turf_category_2,turf_category_3=turf_category_3,turf_category_4=turf_category_4,
                                             turf_description=turf_description,turf_rules_regulations=turf_rules_regulations,turf_address=turf_address,
                                             turf_ownerContact_number=turf_ownerContact_number,turf_host_name=turf_host_name,turf_map=turf_map,turf_price=turf_price,
                                            turf_weekday_base=turf_weekday_base,turf_weekday_peak=turf_weekday_peak,turf_friday_base=turf_friday_base,
                                            turf_friday_peak=turf_friday_peak,turf_saturday_base=turf_saturday_base,turf_saturday_peak=turf_saturday_peak,
                                            turf_sunday_base=turf_sunday_base,turf_sunday_peak=turf_sunday_peak,turf_field_1=turf_field_1,turf_field_2=turf_field_2,
                                            turf_field_3=turf_field_3)
            new_turf_pic = Turf_Pics(turf_ref=new_turf_profile,turf_picture=turf_picture)
            new_turf_profile.save()
            for pic in range(len(new_turf_pic.turf_picture)) :
                Turf_Pics(turf_ref=new_turf_profile,turf_picture=turf_picture[pic]).save()
            # for new_pic in range(len(new_turf_pic.turf_picture)) :
            #     new_pic.save()
            # for new_pic in new_turf_pic.turf_picture:
            #     new_pic.save()
            messages.success(request, 'Turf Created')
            return redirect('add_turf_profile')
        except Exception as e:
            # messages.success(request, 'Turf NotCreated')
            messages.success(request, e)
            return redirect('add_turf_profile')

