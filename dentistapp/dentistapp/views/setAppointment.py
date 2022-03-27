from django.forms import Form, CharField, DateField, IntegerField,DateTimeField
from django.shortcuts import render
from sqlalchemy import text

from dentistapp.setup_database import get_engine


class Appointment(Form):

    appointment_iD = IntegerField(label= "Appointment ID")
    patient_ID = IntegerField(label="Patient ID")
    dentist_ID = IntegerField(label= "Dentist ID")
    appointment_date = DateField(label="Appointment Date")
    start = DateTimeField(label="Start Time")
    end = DateTimeField(label="End Time")
    a_type = CharField(label="Appointment Type")
    a_status = CharField(label="Appointment Status")
    room = IntegerField(label="Assigned Room")

    procedure_number = IntegerField(label="Number Of Procedures")



def form_to_dict(form: Form) -> dict:
    res = {}
    for value in form:
        res[value.name] = value.value()
    return res


def create_appointment(form: Appointment):
    with get_engine().connect() as conn:
        form_data = form_to_dict(form)

        query = text(
            "INSERT INTO appointment(patient_id,dentist_id,appointment_date,start_time,end_time,appointement_type,appointement_status,room_assigned)"
            "VALUES(:patient_ID,:patient_ID,:appointment_date,:start, :end, :a_type,:a_status, :room);"
        )

        conn.execute(query, form_data)

        p_num = 0
        # while form_data["procedure_number"] > p_num:
        #     x= p_num++


def insert_appointment(request):
    if request.method == "POST":
        form = Appointment(request.POST)
        if form.is_valid():
            try:
                create_appointment(form)
                return render(request, "appointment_form.html", {"success": True})
            except Exception as e:
                print(str(e))
                return render(request, "appointment_form.html", {"form": form,
                                                             "error": True})
        else:
            return render(request, "appointment_form.html", {"form": form})

def get_appointment_form(request):
    return render(request, "appointment_form.html", {"form": Appointment()})


def appointment_endpoint(request):
    if request.method == "POST":
        return insert_appointment(request)
    else:
        return get_appointment_form(request)





