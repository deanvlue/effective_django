from django.views.generic import ListView, CreateView
from contacts.models import Contact
from django.core.urlresolvers import reverse

# Create your views here.

class ContactListView(ListView):
  model = Contact
  template_name = 'contact_list.html'

class CreateContactView(CreateView):
  model = Contact
  template_name = 'edit_contact.html'

  def get_success_url(self):
    return reverse('contacts-list')

