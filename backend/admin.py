from django.contrib import admin
from .models import Contact
admin.site.register(Contact)

from django.contrib import admin
from django.http import HttpResponse
import csv
from .models import Contact

# Unregister the Contact model if it's already registered
admin.site.unregister(Contact)

def export_csv(modeladmin, request, queryset):
    # Create a response object with CSV content type
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="contacts.csv"'

    # Create a CSV writer using the response object
    writer = csv.writer(response)

    # Write the header row
    writer.writerow(['First Name', 'Last Name', 'Email', 'Phone Number', 'Subject', 'Comments'])

    # Write the data rows
    for contact in queryset:
        writer.writerow([contact.first_name, contact.last_name, contact.email, contact.phone_number, contact.subject, contact.comments])

    return response

export_csv.short_description = "Export selected contacts to CSV"

class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number', 'subject', 'comments')
    list_filter = ('subject',)  # Add a filter for the 'subject' field
    search_fields = ('first_name', 'last_name', 'email', 'subject', 'comments')  # Add search functionality
    actions = [export_csv]

# Register the Contact model with the modified ContactAdmin
admin.site.register(Contact, ContactAdmin)

