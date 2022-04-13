from app.models import Lead
from app.exc import EmptyDatabase
from flask import jsonify

def get_leads_controller():

     try:
        all_leads = Lead.query.order_by(Lead.visit.desc()).all()
       
        if len(all_leads) == 0:
            raise EmptyDatabase

        serializer = [
        {
            "name": lead.name,
            "email": lead.email,
            "phone": lead.phone,
            "creation_date": lead.creation_date,
            "last_visit": lead.last_visit,
            "visit": lead.visit
        } for lead in all_leads
        ]

        return jsonify(serializer)
     except EmptyDatabase as err:
        return err.message, 400 

