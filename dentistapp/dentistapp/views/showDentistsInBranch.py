from django.forms import Form, IntegerField
from django.shortcuts import render
from sqlalchemy import text

from dentistapp.setup_database import get_engine


class Dentist(Form):
    employee_id = IntegerField(label="Employee ID/SSN")
    branch_id = IntegerField(label="Branch ID")


def result_to_context(form: Form) -> dict:
    res = {}
    rows = []
    for formrow in form:
        row = []
        for key in form.keys():
            row.append(formrow[key])
        rows.append(row)
    # make form into dict
    res['keys'] = [key for key in form.keys()]
    res['rows'] = rows
    res['columns'] = len(rows[0]) if len(rows) > 1 else 0
    return res


def query_dentist():
    with get_engine().connect() as conn:
        query = text(
            "SELECT p.f_name,p.l_name, employee_id , d.branch_id,b.city FROM person p, dentist d, branch b "
            "WHERE d.branch_id=b.branch_id and p.person_id=employee_id;",
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
        context = result_to_context(result)
        return render(request, "dentist_branch_form.html", context)


def dentist_in_branch_endpoint(request):
    return get_dentist_branch(request)
