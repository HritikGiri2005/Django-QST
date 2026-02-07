from django.shortcuts import render, redirect, get_object_or_404
from .models import Person, AadharCard


# 1️⃣ Create Person + Aadhar
def create_person(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        aadhar_number = request.POST.get("aadhar")

        # Create Person
        person = Person.objects.create(
            name=name,
            age=age
        )

        # Create Aadhar linked to that person
        AadharCard.objects.create(
            person=person,
            number=aadhar_number
        )

        return redirect("testapp/person_list")  # Make sure this url exists

    return render(request, "create_person.html")

# 2️⃣ Show all persons with their Aadhar

def person_list(request):
    persons = Person.objects.all().select_related('aadharcard')
    return render(request, "testapp/person_list.html", {"persons": persons})

# 3️⃣ Detail View of a Single Person

def person_detail(request, id):
    person = get_object_or_404(Person, id=id)
    return render(request, "testapp/person_detail.html", {"person": person})
