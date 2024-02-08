from django.shortcuts import render ,redirect
from hotel.models import *
from django.contrib import messages
from django.http import JsonResponse


# Create your views here.


def index(request):
    #OrderDetail.objects.all().delete()
    return render (request,'hotel/index.html')


def sunil_login(request):
    if request.method == 'POST':
        a =int(request.POST["mb"])
        b =int(request.POST["pin"])
        s = a+b
        if s == 10000 :
            request.session['sunil_mobile'] = s
            return redirect('add_admin')
        else:
            return redirect('sunil_login')
    return render(request,'hotel/sunil_login.html')


def add_admin(request):
    if request.session.has_key('sunil_mobile'):
        context={}
        a=Admin.objects.all()
        context={
            'a':a
        }
        if request.method == "POST":
            if "Add" in request.POST:
                admin_name=request.POST.get('admin_name')
                address=request.POST.get('address')
                admin_mobile=request.POST.get('admin_mobile')
                pin=request.POST.get('pin')
                #validatin
                if Admin.objects.filter(admin_mobile=admin_mobile).exists():
                    messages.success(request,"Admin Allready Exitsy")
                else:
                    Admin(
                        admin_name=admin_name,
                        address=address,
                        admin_mobile=admin_mobile,
                        pin=pin
                    ).save()
                    messages.success(request,"Admin Add Succesfully") 
            elif "Edit" in request.POST:
                admin_id=request.POST.get('admin_id')
                admin_name=request.POST.get('admin_name')
                address=request.POST.get('address')
                admin_mobile=request.POST.get('admin_mobile')
                pin=request.POST.get('pin')
                a=Admin.objects.get(id=admin_id)
                a.admin_name=admin_name
                a.address=address
                a.admin_mobile
                a.pin=pin
                a.save()
                messages.success(request,"Admin Edit Succesfully")
            elif "Active" in request.POST:
                id=request.POST.get('id')
                #print(id)
                ac=Admin.objects.get(id=id)
                ac.status='0'
                ac.save()
            elif "Deactive" in request.POST:
                id=request.POST.get('id')
                #print(id)
                ac=Admin.objects.get(id=id)
                ac.status='1'
                ac.save()   
        return render(request,'hotel/add_admin.html',context)
    else:
        return redirect('sunil_login')





def admin_login(request):
    if request.session.has_key('admin_mobile'):
        return redirect('admin_dashboard')
    else:
        if request.method == "POST":
            mb=request.POST ['mb']
            pin=request.POST ['pin']
            s= Admin.objects.filter(admin_mobile=mb,pin=pin,status=1)
            if s:
                request.session['admin_mobile'] = request.POST["mb"]
                return redirect('admin_dashboard')
            else:
                messages.success(request,"please insert correct information or call more suport 9730991252")            
                return redirect('admin_login')
        return render(request,'hotel/admin_login.html')



def admin_dashboard(request):
    if request.session.has_key('admin_mobile'):
        return render(request,'hotel/admin_dashboard.html')
    else:
        return redirect('admin_login')









def dish_category(request):
    if request.session.has_key('admin_mobile'):
        request.session.has_key('admin_mobile')
        admin_mobile = request.session['admin_mobile']
        a=Admin.objects.get(admin_mobile=admin_mobile)
        dc=Dish_category.objects.filter().all()
        context={
            'dc':dc,
            'a':a,       
        }
        if request.method == "POST":
            if "Add" in request.POST:
                name=request.POST.get('name')
                admin_id = request.POST.get('admin_id')
                Dish_category.objects.create(
                    category_name=name,
                    added_by_id=admin_id
                )
                messages.success(request,"Category Added Succesfully")
            elif "Edit" in request.POST:
                name=request.POST.get('name')
                id=request.POST.get('id')
                edit_category=Dish_category.objects.get(id=id)
                edit_category.category_name=name
                edit_category.save()
                messages.success(request,"Category Edit Successfully")
            elif "Delete" in request.POST:
                id=request.POST.get('id')
                Dish_category.objects.get(id=id).delete()
                messages.success(request,"Category Delete Successfully")
            elif "Active" in request.POST:
                id=request.POST.get('id')
                ac=Dish_category.objects.get(id=id)
                ac.status='0'
                ac.save()
            elif "Deactive" in request.POST:
                id=request.POST.get('id')
                ac=Dish_category.objects.get(id=id)
                ac.status='1'
                ac.save()            
        return render(request,'hotel/dish_category.html',context=context)
    else:
        return redirect('admin_login')






def dish(request):
    if request.session.has_key('admin_mobile'):
        admin_mobile = request.session['admin_mobile']
        a=Admin.objects.get(admin_mobile=admin_mobile)
        dc=Dish_category.objects.filter().all()
        d=Dish.objects.filter().all().order_by('-dish_category_id')
        context={
            'c':dc,
            'a':a,
            'd':d       
        }
        if "Add" in request.POST:
            dish_name=request.POST.get('dish_name')
            dish_marathi_name=request.POST.get('dish_marathi_name')
            dish_category_id=request.POST.get('dish_category_id')
            price=request.POST.get('price')
            added_by_id=request.POST.get('admin_id')
            Dish(
                dish_name=dish_name,
                dish_marathi_name=dish_marathi_name,
                dish_category_id=dish_category_id,
                price=price,
                added_by_id=added_by_id,

            ).save()
            messages.success(request,"Dish Added Succesfully")
        elif "Edit" in request.POST:
            dish_name=request.POST.get('dish_name')
            dish_marathi_name=request.POST.get('dish_marathi_name')
            dish_category_id=request.POST.get('dish_category_id')
            price=request.POST.get('price')
            added_by_id=request.POST.get('admin_id')
            dish_id=request.POST.get('dish_id')
            Dish(
                dish_name=dish_name,
                dish_marathi_name=dish_marathi_name,
                dish_category_id=dish_category_id,
                price=price,
                added_by_id=added_by_id,
                id=dish_id
            ).save()
            messages.success(request,"Dish Edit Succesfully")            
        elif "Delete" in request.POST:
            dish_id=request.POST.get('dish_id')
            Dish.objects.get(id=dish_id).delete()
            messages.success(request,"Dish Delete Successfully")
        elif "Active" in request.POST:
            id=request.POST.get('id')
            ac=Dish.objects.get(id=id)
            ac.status='0'
            ac.save()
        elif "Deactive" in request.POST:
            id=request.POST.get('id')
            ac=Dish.objects.get(id=id)
            ac.status='1'
            ac.save()            
        return render(request,'hotel/dish.html',context=context)
    else:
        return redirect('admin_login')
    



def book_order(request):
    if request.session.has_key('admin_mobile'):
        admin_mobile = request.session['admin_mobile']
        a=Admin.objects.get(admin_mobile=admin_mobile)
        dc=Dish_category.objects.filter().all()
        ng=OrderDetail.objects.all().count()
        context={
            'dish_category':dc,
            'a':a,
            'ng':ng
        }
        return render(request,'hotel/book_order.html',context=context)
    else:
        return redirect('admin_login')


def filter_by_category(request):
    if request.method == 'GET':
        dish_category_id = request.GET['dish_category_id']
        
        filter_result = Dish.objects.values().filter(dish_category_id=dish_category_id,status=1)
        dish = list(filter_result)
        #print(dish)
        return JsonResponse({'status': 1, 'dish': dish})
    else:
        return JsonResponse({'status': 0})
    



def place_order(request):
    if request.session.has_key('admin_mobile'):
        admin_mobile = request.session['admin_mobile']
        a=Admin.objects.get(admin_mobile=admin_mobile)
        if request.method == 'GET':
            dish_id = request.GET['dish_id']
            d=Dish.objects.get(id=dish_id)
            qty = request.GET['qty']
            total_price = request.GET['total_price']
            OrderDetail(
                added_by_id=a.id,
                dish_id=dish_id,
                dish_marathi_name=d.dish_marathi_name,
                qty=qty,
                price=d.price,
                total_price=total_price
            ).save()
            ng=(len(OrderDetail.objects.all()))
            print(ng)
            return JsonResponse({'status': 1,'ng':ng})
        else:
            return JsonResponse({'status': 0})
    else:
        return redirect('admin_login')




def complate_order(request):
    if request.session.has_key('admin_mobile'):
        context={}
        admin_mobile = request.session['admin_mobile']
        a=Admin.objects.get(admin_mobile=admin_mobile)
        o=OrderDetail.objects.all().order_by('-id')
        context={
            'a':a,
            'o':o
        }

        return render(request,'hotel/complate_order.html',context)
    else:
        return redirect('admin_login')



def daily_report(request):
    if request.session.has_key('admin_mobile'):
        admin_mobile = request.session['admin_mobile']
        a=Admin.objects.get(admin_mobile=admin_mobile)      
        dc=Dish.objects.all()
        result={}
        qty=0
        total=0      
        if "Search" in request.POST:
            fromdate=request.POST.get('fromdate')
            todate=request.POST.get('todate')
            dish_id=request.POST.get('dish_id')
            #print(dish_id)
            result=OrderDetail.objects.filter(date__gte=fromdate,date__lte=todate,dish_id=dish_id)
            if result:
                for r in result:
                    total +=r.total_price
                    qty +=r.qty            
            if dish_id == '0':
                result=OrderDetail.objects.filter(date__gte=fromdate,date__lte=todate)
                if result:
                    for r in result:
                        total +=r.total_price
                        qty +=r.qty
        return render(request, 'hotel/daily_report.html',{'dc':dc,'result':result,'total':total,'qty':qty,'a':a})
    
    else:
        return redirect('admin_login')
    



    
def test(request):
    return render(request,'hotel/test.html')