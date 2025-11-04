from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template.loader import get_template, render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
from io import BytesIO
from xhtml2pdf import pisa
from .models import Product
from .forms import PrdtForm

def home(request):
    return render(request, 'home.html')

def add_product(request):
    if request.method == 'POST':
        form = PrdtForm(request.POST)
        if form.is_valid():
            product = form.save()
            return redirect('product_detail', pk=product.pk)
    else:
        form = PrdtForm()
    return render(request, 'add_product.html', {'form': form})


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})



def generate_pdf(request, pk):
    product = get_object_or_404(Product, pk=pk)
    template = get_template('product_pdf.html')
    html = template.render({'product': product})

    buffer = BytesIO()
    pisa_status = pisa.CreatePDF(html, dest=buffer)

    if pisa_status.err:
        return HttpResponse('PDF creation error!')
    else:
        response = HttpResponse(buffer.getvalue(), content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{product.name}.pdf"'
        return response



def send_product_email(request, pk):
    product = get_object_or_404(Product, pk=pk)

    subject = f"Product Info: {product.name}"
    from_email = "sander@gmail.com"
    recipient_list = ["your_mailtrap_inbox@mailtrap.io"]

    html_message = render_to_string('product_email.html', {'product': product})
    plain_message = strip_tags(html_message)

    send_mail(subject, plain_message, from_email, recipient_list, html_message=html_message)

    return HttpResponse('Email sent successfully!')
