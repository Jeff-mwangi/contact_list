from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import ListView,UpdateView,DeleteView
from .models import Contact


class ContactListView(ListView):
    model = Contact
    template_name = 'index.html'
    context_object_name = 'contacts'

def add(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        relationship = request.POST['relationship']
        profile = request.FILES['image']
        contact = Contact(name=name,email=email,phone=phone,address=address,relationship=relationship,profile = profile)
        contact.save()
        messages.success(request, 'Contact added successfully')
        return redirect('home')
    else:
        messages.error(request, 'Contact not added')
        return render(request,'add.html')


def edit(request,pk):
    contact = Contact.objects.get(id=pk)
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        relationship = request.POST['relationship']
        image = request.FILES['image']
        contact.name = name
        contact.email = email
        contact.phone = phone
        contact.address = address
        contact.relationship = relationship
        contact.profile = image
        contact.save()
        messages.success(request, 'Contact updated successfully')
        return redirect('home')
    else:
        messages.error(request, 'Contact not updated')
        return render(request,'edit.html', {'contact':contact})

def contact_profile(request,pk):
    contact = Contact.objects.get(id=pk)
    return render(request,'contact-profile.html', {'contact':contact})

def delete(request,pk):
    contact = Contact.objects.get(id=pk)
    if request.method == 'POST':
        contact.delete()
        messages.success(request, 'Contact deleted successfully')
        return redirect('home')
    else:
        messages.error(request, 'Contact not deleted')
        return render(request,'delete.html', {'contact':contact})

def search(request):
    if request.method == 'POST':
        search = request.POST['search']
        contacts = Contact.objects.filter(name__icontains=search)
        return render(request,'index.html',{'contacts':contacts})
    else:
        return redirect('home')

