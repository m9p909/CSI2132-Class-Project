from django.forms import Form, CharField, DateField, IntegerField
from django.shortcuts import render
from sqlalchemy import text

from dentistapp.setup_database import get_engine


# may be optional, I did this cause it's a big one
class Patient(Form):
    SSN = IntegerField(label="SSN")
    b_date = DateField(label="Birth Date")
    f_name = CharField(label="First Name")
    l_name = CharField(label="Last Name")
    city = CharField(label="City")
    house_number = IntegerField(label="House Number")
    street = CharField(label="Street", )
    postal_code = CharField(label="Postal Code", max_length=6)
    province = CharField(label="Province")
    email = CharField(label="Email")
    gender = CharField(label="Gender")
    phone_number = CharField(label="Phone Number")
    insurance = CharField(label="Insurance Name")
    caregiver_ssn = IntegerField(label="Caregiver SSN", required=False)


def form_to_dict(form: Form) -> dict:
    res = {}
    for value in form:
        res[value.name] = value.value()
    return res


def create_patient(form: Patient):
    with get_engine().connect() as conn:
        form_data = form_to_dict(form)
        # we probably should have had ssn be a PK
        query = text(
            "INSERT INTO person(SSN, b_date, f_name, l_name, city, house_number, street, postal_code, "
            "province, email, gender, phone_number) "
            "VALUES (:SSN,:b_date,:f_name,:l_name,:city,:house_number,:street,:postal_code,"
            ":province,:email, "
            ":gender,:phone_number);"
            "INSERT  INTO patient(person_id, insurance)"
            "VALUES ((select person_id from person where SSN = :SSN), :insurance);")

        result = conn.execute(query, form_data)
        if form_data["caregiver_ssn"]:
            query = text(
                "update person set care_giver_id = (select person_id from person where :caregiver_ssn "
                "= SSN )where SSN=:SSN")
            conn.execute(query, form_data)


def insert_patient(request):
    if request.method == "POST":
        form = Patient(request.POST)
        if form.is_valid():
            try:
                create_patient(form)
                return render(request, "patient_form.html", {"success": True})
            except Exception as e:
                print(str(e))
                return render(request, "patient_form.html", {"form": form,
                                                             "error": True})
        else:
            return render(request, "patient_form.html", {"form": form})


def get_patient_form(request):
    return render(request, "patient_form.html", {"form": Patient()})


def patient_endpoint(request):
    if request.method == "POST":
        return insert_patient(request)
    else:
        return get_patient_form(request)
