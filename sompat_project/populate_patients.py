import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'sompat_project.settings')

import django
django.setup()
from patients.models import Pacient, Aparat

def populate():

    RES_IBREEZE_AUTO_CPAP = 'RES_IBREEZE_AUTO_CPAP'
    LOEWENSTEIN_PRISMA_AUTO_CPAP = 'LOEWENSTEIN_PRISMA_AUTO_CPAP'

    pacienti = [
        {"som_id": "0001ab"},
        {"som_id": "0002cd"},
    ]

    aparati = [
        {"sn": "111111",
         "model": LOEWENSTEIN_PRISMA_AUTO_CPAP},
        {"sn": "222222",
         "model": RES_IBREEZE_AUTO_CPAP},
    ]

    for p in pacienti:
        som_id = p["som_id"]
        add_pacient(som_id)

    for a in aparati:
        model = a["model"]
        sn = a["sn"]
        add_aparat(model, sn)

    #print out pacienti and aparati we have added
    for p in Pacient.objects.all():
        print("pacient: ", p)
    for a in Aparat.objects.all():
        print("aparat: ", a)


def add_pacient(som_id):
    p = Pacient.objects.get_or_create(som_id=som_id)[0]
    p.save()
    return p

def add_aparat(model, sn, aktiven=False):
    a = Aparat.objects.get_or_create(sn=sn)[0]
    a.model = model
    a.aktiven = aktiven
    a.save()
    return a


#start execution:
if __name__ == '__main__':
    print("Starting population script...")
    populate()
