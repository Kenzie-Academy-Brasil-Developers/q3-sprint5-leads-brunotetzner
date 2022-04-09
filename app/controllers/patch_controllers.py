from flask import request, current_app
from app.models import Lead
from datetime import datetime
from app.exc import InvalidKey

def patch_lead_controller():
    data = request.get_json()
    invalid_keys = [key for key in data.keys() if key != "email"]

    try:
        if len(invalid_keys)>0:
            raise InvalidKey("email", invalid_keys)

        lead = Lead.query.filter_by(email=data["email"]).first()
        new_data_and_visit = {"last_visit": datetime.now(), "visit": lead.__dict__["visit"]+1 }
    
        for key,  value in new_data_and_visit.items():
            setattr(lead, key, value)

        current_app.db.session.add(lead)
        current_app.db.session.commit()
        return "" , 200

    except AttributeError:
        return {"error": f"Email {data['email']} do not exists"}, 404
    
    except InvalidKey as err:
        return err.message, 400