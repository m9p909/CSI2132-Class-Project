from django.forms import Form, IntegerField
from django.shortcuts import render
from sqlalchemy import text

from dentistapp.setup_database import get_engine


class Dentist(Form):
    employee_id = IntegerField(label="Employee ID/SSN")
    branch_id = IntegerField(label="Branch ID")


def form_to_dict(form: Form) -> dict:
    res={}
    subres = {}
    for key in form.keys():
        subres[key]=[]
    for row in form:
        for key in form.keys():
            subres[key].append(row[key])
    # make form into dict
    res['query']=subres
    return res

def query_dentist():
    with get_engine().connect() as conn:

        query = text(
            "SELECT p.f_name,p.l_name, employee_id , d.branch_id,b.city FROM person p, dentist d, branch b WHERE d.branch_id=b.branch_id and p.person_id=employee_id;",
        )

        result = conn.execute(query)
        # for row in result:
        #     print("First and Last name:", row['f_name'],row['l_name'])
        #     print("Dentist ID:", row['employee_id'])
        #     print("Branch ID:", row['branch_id'])
        return result

def get_dentist_branch(request):
    if request.method == "GET":
        result = query_dentist()
        context = form_to_dict(result)
        return render(request, "dentist_branch_form.html", context)

def dentist_in_branch_endpoint(request):
    return get_dentist_branch(request)

