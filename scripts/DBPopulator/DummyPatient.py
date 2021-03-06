from distutils.command.build_scripts import first_line_re
import names
import random
from mongoengine import Document, BooleanField, StringField, IntField, DateTimeField
from .populate_helpers import get_random_date, get_random_diagnosis
from datetime import datetime

class DummyPatient(object):
    def __init__(self, *args, **kwargs):
        self.gender = bool(random.getrandbits(1))
        self.kis_id = random.randint(10000000, 99999999)
        if self.gender:
            self.first_name = names.get_first_name(gender='male')
        else:
            self.first_name = names.get_first_name(gender='female')
        self.last_name = names.get_last_name()
        self.date_of_birth = get_random_date()
        self.created_at = datetime.now()
        self.main_diagnosis = get_random_diagnosis()

class MongoDummyPatient(Document):
    id = IntField()
    gender = BooleanField()
    kis_id = IntField()
    last_name = StringField()
    first_name = StringField()
    date_of_birth = DateTimeField()
    created_at = DateTimeField()
    main_diagnosis = StringField()
    
    meta = {
        'collection': 'api_patient'
    }
    


if __name__ == '__main__':
    patients = []
    
    for i in range(0,3):
        patients.append(DummyPatient())
        print(i,'th iteration, Patient created successfully.')
        print(patients[i].__dict__)
        
