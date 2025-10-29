from django.shortcuts import render, redirect

def teach_list(request, message):
    teachers = ["Anjali", "Raju", "Meera", "Joseph"]
    if request.method == 'POST':
        return redirect('teachers:teach_list', message='Welcome Teachers')
    return render(request, 'teachers/teacher.html', {
        'teachers': teachers,
        'message': message
    })