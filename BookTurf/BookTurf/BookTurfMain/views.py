from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from .models import Turf_Profile,Turf_Booked
from .models import addmin
from .models import Turf_Pics,Turf_Host
from django.http import HttpResponse, JsonResponse
import datetime




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
        return redirect('/BookTurf/BookTurfMain/sign_up/')

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
        host_username =request.POST['host_username']
        host_email =request.POST['host_email']
        host_password =request.POST['host_password']
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
        # turf_field_1 = request.POST['turf_field_1']
        # turf_field_2 = request.POST['turf_field_2']
        # turf_field_3 = request.POST['turf_field_3']

        # remove_timeslot_1 = request.POST['time_slot_1']
        # remove_timeslot_2 = request.POST['time_slot_2']
        # remove_timeslot_3 = request.POST['time_slot_3']
        # remove_timeslot_4 = request.POST['time_slot_4']
        # remove_timeslot_5 = request.POST['time_slot_5']
        # remove_timeslot_6 = request.POST['time_slot_6']
        # remove_timeslot_7 = request.POST['time_slot_7']
        # remove_timeslot_8 = request.POST['time_slot_8']
        # remove_timeslot_9 = request.POST['time_slot_9']
        # remove_timeslot_10 = request.POST['time_slot_10']
        # remove_timeslot_11 = request.POST['time_slot_11']
        # remove_timeslot_12 = request.POST['time_slot_12']
        # remove_timeslot_13 = request.POST['time_slot_13']
        # remove_timeslot_14 = request.POST['time_slot_14']
        # remove_timeslot_15 = request.POST['time_slot_15']
        # remove_timeslot_16 = request.POST['time_slot_16']
        # remove_timeslot_17 = request.POST['time_slot_17']
        # remove_timeslot_18 = request.POST['time_slot_18']
        # remove_timeslot_19 = request.POST['time_slot_19']
        # remove_timeslot_20 = request.POST['time_slot_20']
        # remove_timeslot_21 = request.POST['time_slot_21']
        # remove_timeslot_22 = request.POST['time_slot_22']
        # remove_timeslot_23 = request.POST['time_slot_23']
        # remove_timeslot_24 = request.POST['time_slot_24']

        remove_timeslot_start = request.POST['remove_time_slot_start'].split(" ")
        remove_timeslot_end = request.POST['remove_time_slot_end'].split(" ")
        remove_timeslot_diff = request.POST['remove_time_slot_diff']
        removed_timeslot = []
        for i in range(int(remove_timeslot_start[0]),int(remove_timeslot_start[0])+int(remove_timeslot_diff)):
            if remove_timeslot_start[1] == remove_timeslot_end[1]:
                removed_timeslot.append(f"{i}-{i+1} {remove_timeslot_start[1]}")
            else:
                if(i<11):
                    removed_timeslot.append(f"{i}-{i+1} {remove_timeslot_start[1]}")
                elif(i >=11):
                    if(i > 12):
                        removed_timeslot.append(f"{(i+1) % 13}-{(i+2)%13} {remove_timeslot_end[1]}")
                    else:
                        removed_timeslot.append(f"{i % 13}-{(i+1)%13} {remove_timeslot_end[1]}")

        try:
            index = removed_timeslot.index("12-0 AM")
            removed_timeslot[index] = "12-1 AM"
        except ValueError:
            print("12-0 AM not in list")

        try:
            indexx = removed_timeslot.index("12-0 PM")
            removed_timeslot[indexx] = "12-1 PM"
        except ValueError:
            print("12-0 PM not in list")

            
        peak_timeslot_start = request.POST['peak_time_slot_start'].split(" ")
        peak_timeslot_end = request.POST['peak_time_slot_end'].split(" ")
        peak_timeslot_diff = request.POST['peak_time_slot_diff']
        peak_timeslot = []
        for i in range(int(peak_timeslot_start[0]),int(peak_timeslot_start[0])+int(peak_timeslot_diff)):
            if peak_timeslot_start[1] == peak_timeslot_end[1]:
                peak_timeslot.append(f"{i}-{i+1} {peak_timeslot_start[1]}")
            else:
                if(i<11):
                    peak_timeslot.append(f"{i}-{i+1} {peak_timeslot_start[1]}")
                elif(i >=11):
                    if(i > 12):
                        peak_timeslot.append(f"{(i+1) % 13}-{(i+2)%13} {peak_timeslot_end[1]}")
                    else:
                        peak_timeslot.append(f"{i % 13}-{(i+1)%13} {peak_timeslot_end[1]}")

        try:
            index = peak_timeslot.index("12-0 AM")
            peak_timeslot[index] = "12-1 AM"
        except ValueError:
            print("12-0 AM not in list")

        try:
            indexx = peak_timeslot.index("12-0 PM")
            peak_timeslot[indexx] = "12-1 PM"
        except ValueError:
            print("12-0 PM not in list")
        
        print(peak_timeslot)

        
        try:
            new_turf_profile = Turf_Profile(turf_name=turf_name,turf_rating=turf_rating,turf_category_1=turf_category_1,
                                             turf_category_2=turf_category_2,turf_category_3=turf_category_3,turf_category_4=turf_category_4,
                                             turf_description=turf_description,turf_rules_regulations=turf_rules_regulations,turf_address=turf_address,
                                             turf_ownerContact_number=turf_ownerContact_number,turf_map=turf_map,turf_price=turf_price,
                                            turf_weekday_base=turf_weekday_base,turf_weekday_peak=turf_weekday_peak,turf_friday_base=turf_friday_base,
                                            turf_friday_peak=turf_friday_peak,turf_saturday_base=turf_saturday_base,turf_saturday_peak=turf_saturday_peak,
                                            turf_sunday_base=turf_sunday_base,turf_sunday_peak=turf_sunday_peak,removed_timeslot=removed_timeslot,peak_timeslot=peak_timeslot)
                                            # ,turf_field_1=turf_field_1,turf_field_2=turf_field_2,
                                            # turf_field_3=turf_field_3)
            new_turf_pic = Turf_Pics(turf_ref=new_turf_profile,turf_picture=turf_picture)
            new_turf_profile.save()
            for pic in range(len(new_turf_pic.turf_picture)) :
                Turf_Pics(turf_ref=new_turf_profile,turf_picture=turf_picture[pic]).save()
            new_turf_host = Turf_Host(turf_profile=new_turf_profile,username=host_username,email=host_email,password=host_password)
            new_turf_host.save()
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

def ajax_date_and_timeslot_update(request):
    # Define a date as year, month, and day WASE USE AJAX AND GET THESE INPUTS HERE
    # year = 2023
    # month = 10
    # date = 1

    date_object = datetime.date(year, month, date)
    day = date_object.strftime("%A")
    
    turf_profile = Turf_Profile(turf_id= 2,turf_name="Amaan")

    if(day == ('Monday' or 'Tuesday' or 'Wednesday' or 'Thursday')):
        return HttpResponse(turf_profile.turf_weekday_base,turf_profile.turf_weekday_peak)
    elif(day == 'Friday'):
        return HttpResponse(turf_profile.turf_friday_base,turf_profile.turf_friday_peak)
    elif(day == 'Saturday'):
        return HttpResponse(turf_profile.turf_saturday_base,turf_profile.turf_saturday_peak)
    elif(day == 'Sunday'):
        return HttpResponse(turf_profile.turf_sunday_base,turf_profile.turf_sunday_peak)



def date_view(request):
    if request.method == "POST":
        
        
        date_toggle_value = request.POST.get("dateToggleValue")
       


        # Process the form data or perform any necessary actions here

        # Print the received data (you can replace this with your own logic)
        
        print("Date Toggle Value:", date_toggle_value)
        

        response_content = f"Date Toggle Value: {date_toggle_value}\n"
                           

        # Return an HTTP response with the data
        return HttpResponse(response_content, content_type="text/plain")

    return HttpResponse("Invalid request method", content_type="text/plain")

selected_time_slot = ""
datess = ""
def submit_booking(request):
    if request.method == 'POST':
        # Get the data from the form
        global selected_time_slot
        selected_time_slot = request.POST.get('selectedTimeSlotValue')  # Updated variable name
        global datess
        datess = request.POST.get('datessValue')  # Updated variable name

        # Process the data (you can save it to the database or perform any other actions)

         # For demonstration purposes, print the data to the console
        print("Selected Time Slot:", selected_time_slot)
        print("Date:", datess)

        # You can also save the data to the database here if needed

        # Return a JSON response with the values
        return JsonResponse({'selectedTimeSlotValue': selected_time_slot, 'datessValue': datess})

    # Handle GET requests or other cases
    return JsonResponse({'error': 'Invalid request'})

def reserve(request):
    if(request.method == "POST"):
        if(request.user.is_authenticated):
            user_email = request.user
            turf_profile_id = request.POST["turf_profile_id"]
            # global profile_number
            # profile_number = request.get_full_path()
            # print(selected_time_slot)
            # print(datess)
            # print(request.user)
            # print(turf_profile_id)
            turf_profile = Turf_Profile.objects.get(turf_id = turf_profile_id)
            user = User.objects.get(email=user_email)
            turf_profile_booked = Turf_Booked(turf_profile=turf_profile,user=user,turf_timeslot=selected_time_slot,turf_date=datess)
            turf_profile_booked.save()
            turf_pics = Turf_Pics.objects.filter(turf_ref = turf_profile_id)[:1]
            params = {"photo":turf_pics,"name":turf_profile.turf_name,"address":turf_profile.turf_address,"date":datess,"timeslot":selected_time_slot}
            return render(request,"BookTurfMain/check_out.html",params)
        else:
            return redirect(login_page)

def check_out(request):
    return render(request,"BookTurfMain/check_out.html")

# def turf_page(request):
#     turf_booked = Turf_Booked.objects.all()
#     params = {"turf_booked" : turf_booked}
#     return render(request,"BookTurfMain/turf_page.html",params)

def host_login(request):
    return render(request,"BookTurfMain/host_login.html")

def host_login_authenticate(request):
    if(request.method == "POST"):
        email = request.POST["email"]
        password = request.POST["password"]
        try:
            host = Turf_Host.objects.get(email=email,password=password)
            if(host is not None):
                turf_booked = Turf_Booked.objects.filter(turf_profile=host.turf_profile)
                params = {"turf_booked" : turf_booked}
                return render(request,"BookTurfMain/turf_page_wase.html",params)
            else:
                return render(request,"BookTurfMain/host_login.html")
        except:
            return render(request,"BookTurfMain/host_login.html")

    else:
        return render(request,"BookTurfMain/host_login.html")

