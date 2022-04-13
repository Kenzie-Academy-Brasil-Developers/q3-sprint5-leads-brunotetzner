from flask import request, jsonify, current_app
from app.models import Lead
from app.exc import *
import re

def post_lead_controller():
    data = request.get_json()
    valid_keys = ["name", "email", "phone"]
    invalid_keys = [key for key in data.keys() if key not in valid_keys]
    missing_keys = [key for key in valid_keys if key not in data.keys()]

    filter_cellphone= Lead.query.filter_by(phone=data["phone"])
    filter_email = Lead.query.filter_by(email=data["email"])
    invalid_key_values = [key for key in data.keys() if type(data[key]) != str]
   
    serialize_cellphones_alrealy_exists = [
    {"phone": cellphone.phone}
    for cellphone in filter_cellphone.all()
    ]
    serialize_email_alrealy_exists = [
    {"email": email.email}
    for email in filter_email.all()
    ]
    print(len(data['phone']))
    print(data['phone'])

    try:
        if len(invalid_keys)>0:
          raise InvalidKey(valid_keys, invalid_keys)
       
        if len(missing_keys)>0:
            raise MissingKey(valid_keys, missing_keys)      
       
        if len(serialize_cellphones_alrealy_exists) > 0: 
            raise PhoneAlrealyExists(serialize_cellphones_alrealy_exists[0]["phone"])
       
        if len(serialize_email_alrealy_exists) > 0: 
            raise EmailAlrealyExists(serialize_email_alrealy_exists[0]["email"])
        
        if len(invalid_key_values)>0:
            raise InvalidTypeValue(invalid_key_values)

        if not re.search('\(..\).....\-....$', data['phone']) or len(data['phone']) != 14:
            raise InvalidCellphone

        lead = Lead(**data)
        current_app.db.session.add(lead)
        current_app.db.session.commit()    

        serializer = {
            "name": lead.name,
            "email": lead.email,
            "phone": lead.phone,
            "creation_date": lead.creation_date,
            "last_visit": lead.last_visit,
            "visit": lead.visit
        }

        return jsonify(serializer), 201

    except InvalidKey as err:
        return err.message,400

    except MissingKey as err:
        return err.message,400

    except PhoneAlrealyExists as err:
        return err.message,409

    except EmailAlrealyExists as err:
        return err.message,409

    except InvalidTypeValue as err:
        return err.message,400
        
    except InvalidCellphone as err:
        return err.message,400
   