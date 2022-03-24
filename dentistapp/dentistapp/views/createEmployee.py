from django.forms import Form, CharField, DateField, IntegerField,Select
from django.shortcuts import render
from sqlalchemy import text

from dentistapp.setup_database import get_engine


# may be optional, I ripped it from createPatient.py since they share Person
class Employee(Form):
    EMPLOYEE_TYPES = [  ("manager", "Manager"),
                        ("receptionist", "Receptionist"),
                        ("hygienist", "Hygienist")
                    ]
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
    salary = IntegerField(label="Salary")
    caregiver_ssn = IntegerField(label="Caregiver SSN", required=False)
    branch_id = IntegerField(label="Branch ID")
    employee_type = CharField(label="Employee Type",
                              widget=Select(choices=EMPLOYEE_TYPES))


def form_to_dict(form: Form) -> dict:
    res = {}
    for value in form:
        res[value.name] = value.value()
    return res


def create_employee(form: Employee):
    with get_engine().connect() as conn:
        form_data = form_to_dict(form)
        # Changed it so employee ID is equivalent to the person's ID
        query = text(
            "INSERT INTO person(SSN, b_date, f_name, l_name, city, house_number, street, postal_code, "
            "province, email, gender, phone_number) "
            "VALUES (:SSN,:b_date,:f_name,:l_name,:city,:house_number,:street,:postal_code,"
            ":province,:email, "
            ":gender,:phone_number);"
            "INSERT  INTO Employee(employee_ID, salary)"
            "VALUES ((select person_id from person where SSN = :SSN), :salary);")

        result = conn.execute(query, form_data)
        if form_data["caregiver_ssn"]:
            query = text(
                "update person set care_giver_id = (select person_id from person where :caregiver_ssn "
                "= SSN )where SSN=:SSN")
            conn.execute(query, form_data)
        # Got to check the dependencies on branch_ids here
        if form_data["employee_data"] == "manager":
            query = text(
                "INSERT  INTO Manager(employee_ID, branch_id)"
                "VALUES (:employee_ID,:branch_id)"
            )
            conn.execute(query, form_data)
        elif form_data["employee_data"] == "receptionist":
            query = text(
                "INSERT  INTO Receptionist(employee_ID, branch_id)"
                "VALUES (:employee_ID,:branch_id)"
            )
            conn.execute(query, form_data)
        else:
            query = text(
                "INSERT  INTO hygienist(employee_ID, branch_id)"
                "VALUES (:employee_ID,:branch_id)"
            )
            conn.execute(query, form_data)


def insert_employee(request):
    if request.method == "POST":
        form = Employee(request.POST)
        if form.is_valid():
            try:
                create_employee(form)
                return render(request, "employee_form.html", {"success": True})
            except Exception as e:
                print(str(e))
                return render(request, "employee_form.html", {"form": form,
                                                             "error": True})
        else:
            return render(request, "employee_form.html", {"form": form})


def get_employee_form(request):
    return render(request, "employee_form.html", {"form": Employee()})


def employee_endpoint(request):
    if request.method == "POST":
        return insert_employee(request)
    else:
        return get_employee_form(request)
