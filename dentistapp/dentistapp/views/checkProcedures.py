from django.forms import Form, IntegerField
from django.shortcuts import render
from sqlalchemy import text

from dentistapp.setup_database import get_engine

class Procedure(Form):
    PROCEDURE_TYPE = [("scaling", "Scaling"),
                          ("fluoride", "Fluoride"),
                          ("removal", "Removal"),
                          ("cavity filling", "Cavity Filling"),
                          ]


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

def get_query(form: Procedure):
    with get_engine().connect() as conn:
        form_data = form_to_dict(form)
        query = text("SELECT DISTINCT procedure_type FROM Appointment_procedure ;")
        result = conn.execute(query, form_data)
        return result

def query_procedure(request):
    form = Procedure(request.POST)
    context = result_to_context(get_query(form))
    return render(request, "procedure_list.html", context)

def get_procedures(request):
    return render(request, "procedure_list.html", {"form": Procedure()})

def check_procedure_endpoint(request):
    if(request.method=="POST"):
        return query_procedure(request)
    else:
        results = get_procedures(request)
        return results


