import requests

from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseBadRequest
from rest_framework import generics, mixins

from .models import Lead
from .serializers import LeadSerializer

# Create your views here.
class LeadListCreate(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer

    def get(self, request, *args, **kwargs):
        if(request.user.is_superuser):
            return self.list(request, *args, **kwargs)

        return HttpResponseForbidden()

    def post(self, request, *args, **kwargs):
        secret_key = settings.RECAPTCHA_SECRET_KEY
        data = {
            'response': request.data.get('token'),
            'secret': secret_key
        }
        resp = requests.post(settings.RECAPTCHA_VERIFICATION_URL, data=data)
        result_json = resp.json()

        if(result_json.get('score') < settings.RECAPTCHA_SCORE_THREASHOLD):
            return HttpResponseForbidden()

        lead = Lead(
            name = request.data.get('name'), 
            phone_number = request.data.get('phone-number'),
            email = request.data.get('email'),
            message = request.data.get('message')
        )
        
        try:
            lead.full_clean()
        except:
            print(lead)
            return HttpResponseBadRequest('missing fields')
        else:
            self.notifyDev(lead)
            self.thankCustomer(lead.email, lead.name)
            lead.save()

        return HttpResponse(status=201)

    def notifyDev(self, lead):
        send_mail(
                'New Lead',
                str(lead),
                'rohi@roldev.cc',
                ['rohi@roldev.cc']
            )

    def thankCustomer(self, email, name = ""):
        message = ""
        if(len(name) > 0):
            message += "Dear {},\n\n".format(name);
        message += "Thank you for leaving me a message, I will contact you as soon as possible\n\n"
        message += "Sincerely,\n"
        message += "Rohi Ulecia\n"
        message += "Roldev Developer"
        if(email):
            send_mail(
                'Thank you for contacting Roldev',
                message,
                'rohi@roldev.cc',
                [email]
            )
