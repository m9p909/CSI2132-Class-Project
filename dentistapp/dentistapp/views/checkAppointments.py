from django.forms import Form, IntegerField
from django.shortcuts import render
from sqlalchemy import text

from dentistapp.setup_database import get_engine


class Appointment(Form):
    dentist_id = IntegerField(label="Employee ID/SSN")

def form_to_dict(form: Form) -> dict:
    res = {}
    for value in form:
        res[value.name] = value.value()
    return res

def result_to_context(result):
    res={}
    subres = {}
    for key in result.keys():
        subres[key]=[]
    for row in result:
        for key in result.keys():
            subres[key].append(row[key])
    # make form into dict
    res['query']=subres
    return res

def query_dentist(form: Appointment):
    with get_engine().connect() as conn:
        form_data = form_to_dict(form)
        query = text(
            "SELECT a.appointment_id,a.patient_id,p.f_name,p.l_name,d.employee_id,a.appointment_date,a.start_time,a.end_time,a.appointement_type, "
            "a.appointement_status,a.room_assigned "
            "FROM appointment a, dentist d, person p "
            "WHERE d.employee_id = :dentist_id AND d.employee_id = person_id;")

        result = conn.execute(query,form_data)
        # for row in result:
        #     print("First and Last name:", row['f_name'],row['l_name'])
        #     print("Dentist ID:", row['employee_id'])
        #     print("Branch ID:", row['branch_id'])
        return result



def query_appointments(request):
    form = Appointment(request.POST)
    result = query_dentist(form)
    context = result_to_context(result)
    return render(request, "dentist_appointment.html", context)

def get_appointments(request):
    return render(request, "dentist_appointment.html", {"form": Appointment()})

def check_appointment_endpoint(request):
    if(request.method=="POST"):
        return query_appointments(request)
    else:
        results = get_appointments(request)
        return results


