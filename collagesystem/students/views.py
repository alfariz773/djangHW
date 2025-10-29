from django.shortcuts import render, redirect

def std_list(request, message):
    students = ["Brian", "Shibin", "Arunima", "prf.Pinarayi vijayan"]
    if request.method == 'POST':
        return redirect('students:std_list', message='Welcome Students')
    return render(request, 'students/student.html', {
        'students': students,
        'message': message
    })