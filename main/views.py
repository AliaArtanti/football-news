from django.shortcuts import render
def show_main(request):
    context = {
        'npm' : '2406439425',
        'name': 'Alia Artanti',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)

# Create your views here.
