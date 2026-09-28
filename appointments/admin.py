
from django.contrib import admin
from django.core.mail import send_mail

from .models import Appointment





@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):

        

        if change:

            old_appointment = Appointment.objects.get(pk=obj.pk)

            

            if old_appointment.status != obj.status:

                

                if obj.status == "Confirmed":

                    

                    result = send_mail(
                        "Appointment Confirmed",
                        f"Your appointment on {obj.appointment_date} at "
                        f"{obj.appointment_time} has been confirmed.",
                        None,
                        [obj.patient.email],
                    )

                    

                elif obj.status == "Cancelled":

                    

                    result = send_mail(
                        "Appointment Cancelled",
                        f"Your appointment on {obj.appointment_date} at "
                        f"{obj.appointment_time} has been cancelled.",
                        None,
                        [obj.patient.email],
                    )

                    

        super().save_model(request, obj, form, change)
