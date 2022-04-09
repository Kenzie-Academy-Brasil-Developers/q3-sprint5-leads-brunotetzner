from flask import request, current_app
from app.models import Lead
from app.exc import InvalidKey, InvalidTypeValue

def delete_lead_controller():
    data = request.get_json()
    invalid_keys = [key for key in data.keys() if key != "email"]

    try:
        if len(invalid_keys)>0:
            raise InvalidKey("email", invalid_keys)

        if type(data["email"]) != str:
            raise InvalidTypeValue("email")

        lead = Lead.query.filter_by(email=data["email"])

        serialize_lead = [{
        "id": people.id, 
        "name": people.name,
        "email" : people.email,
        "phone": people.phone ,
        "creation_date" : people.creation_date,
        "last_visit ": people.creation_date,
        "visit": people.visit 
        } for people in lead.all()]


        if len(serialize_lead) == 0:
           raise AttributeError
        
        lead.delete()
        current_app.db.session.commit()
        return "" , 200

    except AttributeError:
        return {"error": f"Email {data['email']} do not exists"}, 404
    
    except InvalidKey as err:
        return err.message, 400

    except InvalidTypeValue as err:
        return err.message, 400

