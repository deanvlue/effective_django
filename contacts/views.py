from django.views.generic import ListView
from contacts.models import Contact

# Create your views here.

class ContactListView(ListView):
  model = Contact



