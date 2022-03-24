from django.forms import Form, IntegerField
from django.shortcuts import render
from sqlalchemy import text

from dentistapp.setup_database import get_engine


class Dentist(Form):
    employee_id = IntegerField(label="Employee ID/SSN")
    branch_id = IntegerField(label="Branch ID")


def form_to_dict(form: Form) -> dict:
    res = {}
    for value in form:
        res[value.name] = value.value()
    return res

def query_dentist():
    with get_engine().connect() as conn:

        query = text(
            "SELECT employee_id , d.branch_id FROM dentist d, branch b WHERE d.branch_id=b.branch_id;",
        )

        result = conn.execute(query)
        for row in result:
            print(row)
            print("Dentist ID:", row['employee_id'])
            print("Branch ID:", row['branch_id'])
        return result

def get_dentist_branch(request):
    if request.method == "GET":
        result = query_dentist()
        return render(request, "dentist_branch_form.html", {"success": True})

def dentist_in_branch_endpoint(request):
    return get_dentist_branch(request)

