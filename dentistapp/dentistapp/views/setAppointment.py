from django.forms import Form, CharField, DateField, IntegerField,DateTimeField,Select
from django.shortcuts import render
from sqlalchemy import text

from dentistapp.setup_database import get_engine


class Appointment(Form):
    PROCEDURE_TYPE = [("scaling", "Scaling"),
                      ("fluoride", "Fluoride"),
                      ("removal", "Removal"),
                      ("cavity filling", "Cavity Filling"),
                      ]

    appointment_ID = IntegerField(label= "Appointment ID")
    patient_ID = IntegerField(label="Patient ID")
    dentist_ID = IntegerField(label= "Dentist ID")
    appointment_date = DateField(label="Appointment Date")
    start = DateTimeField(label="Start Time")
    end = DateTimeField(label="End Time")
    a_type = CharField(label="Appointment Type")
    a_status = CharField(label="Appointment Status")
    room = IntegerField(label="Assigned Room")

    invoice_ID = IntegerField(label="Invoice ID")
    procedure_ID = IntegerField(label="Procedure ID")
    procedure_number = IntegerField(label="Number Of Procedures")
    procedure_type = CharField(label="Type of Procedure",
                               widget=Select(choices=PROCEDURE_TYPE))
    tooth = CharField(label="Tooth/Teeth involved")



def form_to_dict(form: Form) -> dict:
    res = {}
    for value in form:
        res[value.name] = value.value()
    return res


def create_appointment(form: Appointment):
    with get_engine().connect() as conn:
        form_data = form_to_dict(form)

        query = text(
            "INSERT INTO appointment(apointment_id,patient_id,dentist_id,appointment_date,start_time,end_time,appointement_type,appointement_status,room_assigned)"
            "VALUES(:appointment_ID,:patient_ID,:dentist_ID,:appointment_date,:start, :end, :a_type,:a_status, :room);"
        )

        conn.execute(query, form_data)

    
        if form_data["procedure_type"] == "scaling":
            type = "scaling"
            query = text(" INSERT  INTO Appointment_Procedure(appointment_proc_id, appointment_id, procedure_code, procedure_type, date, invoice_id, tooth_involved, amount_of_procedure, total_charge)"
                         "VALUES (:procedure_ID,:appointment_ID,:11112,:type,:appointment_date,:invoice_ID,:tooth,:100,:125);"
                         "INSERT INTO Invoice(invoice_id, patient_id, date_of_issue)"
                         "VALUES (:invoice_ID,:patient_ID,:dentist_ID);"
                         )
            conn.execute(query, form_data)
        elif form_data["procedure_type"] == "fluoride":
            type = "fluoride"
            query = text(" INSERT  INTO Appointment_Procedure(appointment_proc_id, appointment_id, procedure_code, procedure_type, date, invoice_id, tooth_involved, amount_of_procedure, total_charge)"
                         "VALUES (:procedure_ID,:appointment_ID,:12101,:type,:appointment_date,:invoice_ID,:tooth,:115,:140);"
                         "INSERT INTO Invoice(invoice_id, patient_id, date_of_issue)"
                         "VALUES (:invoice_ID,:patient_ID,:dentist_ID);"
                         )
            conn.execute(query, form_data)
        elif form_data["procedure_type"] == "removal":
            type = "removal"
            query = text(" INSERT  INTO Appointment_Procedure(appointment_proc_id, appointment_id, procedure_code, procedure_type, date, invoice_id, tooth_involved, amount_of_procedure, total_charge)"
                         "VALUES (:procedure_ID,:appointment_ID,:311140,:type,:appointment_date,:invoice_ID,:tooth,:200,:250);"
                         "INSERT INTO Invoice(invoice_id, patient_id, date_of_issue)"
                         "VALUES (:invoice_ID,:patient_ID,:dentist_ID);"
                         )
            conn.execute(query, form_data)
        else:
            type = "cavity filling"
            query = text(
                " INSERT  INTO Appointment_Procedure(appointment_proc_id, appointment_id, procedure_code, procedure_type, date, invoice_id, tooth_involved, amount_of_procedure, total_charge)"
                "VALUES (:procedure_ID,:appointment_ID,:99111,:type,:appointment_date,:invoice_ID,:tooth,:180,:200);"
                "INSERT INTO Invoice(invoice_id, patient_id, date_of_issue)"
                "VALUES (:invoice_ID,:patient_ID,:dentist_ID);"
                )
            conn.execute(query, form_data)




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





