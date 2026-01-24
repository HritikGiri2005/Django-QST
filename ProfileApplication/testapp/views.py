from django.shortcuts import render

# Create your views here.

def nameview(request):
    if request.method == 'POST':
        name = request.POST.get('name')

        response = render(request,'testapp/age.html')
        response.set_cookie('name',name)

        return response
    
    return render(request,'testapp/name.html')


def ageview(request):
    if request.method == 'POST':
        age = request.POST.get('age')

        response = render(request,'testapp/qualification.html')
        response.set_cookie('age',age)

        return response
    
    return render(request,'testapp/age.html')




def qualificationview(request):
    if request.method == 'POST':
        # qualification = request.POST.get('qualification')
        response = render(request,'testapp/result.html')
        
        return response
    
    return render(request,'testapp/qualification.html')


def resultview(request):
    name = request.COOKIES.get('name')
    age = request.COOKIES.get('age')

    qualification = request.GET.get('qualification')

    response = render(request,
        'testapp/result.html',
        {
            'name': name,
            'age': age,
            'qualification': qualification
        })
    
    return response 




