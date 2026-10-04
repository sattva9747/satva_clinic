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
                    print(
                        "SENDING CONFIRMED EMAIL TO:",
                        repr(obj.patient.email)
                    )

                    send_mail(
                        subject="Appointment Confirmed",
                        message=(
                            f"Your appointment on {obj.appointment_date} "
                            f"at {obj.appointment_time} has been confirmed."
                        ),
                        from_email=None,
                        recipient_list=[obj.patient.email],
                        fail_silently=False,
                    )

                elif obj.status == "Cancelled":
                    print(
                        "SENDING CANCELLED EMAIL TO:",
                        repr(obj.patient.email)
                    )

                    send_mail(
                        subject="Appointment Cancelled",
                        message=(
                            f"Your appointment on {obj.appointment_date} "
                            f"at {obj.appointment_time} has been cancelled."
                        ),
                        from_email=None,
                        recipient_list=[obj.patient.email],
                        fail_silently=False,
                    )

        super().save_model(request, obj, form, change)
        