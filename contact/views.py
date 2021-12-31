from django.shortcuts import render, redirect
from .models import Contact

# Create your views here.
def index(request):
    # Gets all the objects in the contact model and save in contacts variable
    # then pass the variable into ur template/html file so you can loop over it to display each item,contact or object
    contacts = Contact.objects.all()
    search_input = request.GET.get('search-area')
    if search_input:
        contacts = Contact.objects.filter(full_name__icontains=search_input)
    else:
        contacts = Contact.objects.all()
        search_input = ''
    return render(request, 'index.html', {'contacts': contacts, 'search_input': search_input})

def addContact(request):
    # if its a POST request get all data
    if request.method == 'POST':
        new_contact = Contact(
            full_name = request.POST['fullname'],
            relationship = request.POST['relationship'],
            email = request.POST['email'],
            phone_number = request.POST['phone-number'],
            address = request.POST['address']
        )
        new_contact.save()
        return redirect('/')
    return render(request, 'new.html')

def contactProfile(request, pk):
    # gets only one model in the object using the id /pk
    contact = Contact.objects.get(id=pk)
    return render(request, 'contact-profile.html', {'contact': contact})

def editContact(request, pk):
    #gets only one modal in the object, for editing or profile update
    contact = Contact.objects.get(id=pk)
    
    #save the form update in the edit page
    if request.method == 'POST':
        #contact.formername = newly updated name from the form
        contact.full_name = request.POST['fullname']
        contact.relationship = request.POST['relationship']
        contact.email = request.POST['email']
        contact.phone_number = request.POST['phone-number']
        contact.address = request.POST['address']
        contact.save()
        
        #concatenation is of type int, and we declared str on the url, so we need to change it to type str
        return redirect('/profile/'+str(contact.id))
    return render(request, 'edit.html', {'contact': contact})

def deleteContact(request, pk):
    contact = Contact.objects.get(id=pk)
    
    if request.method == 'POST':
        contact.delete()
        return redirect('/')
    return render(request, 'delete.html', {'contact': contact})