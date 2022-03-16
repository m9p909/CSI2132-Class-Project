from django.shortcuts import render

from djangoProject2.data_access.dentists import getDentistsFromDatabase


def getDentists(request):

    #dentists = getDentistsFromDatabase(request.POST["branch_id"])
    #context = {
    #    dentists: dentists
    #}
    return render(request, "index.html", {})
