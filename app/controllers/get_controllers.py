from http.client import REQUEST_URI_TOO_LONG
from app.models import Lead
from app.exc import EmptyDatabase

from flask import jsonify
def get_leads_controller():

    try:
         all_leads = Lead.query.all()

         if len(all_leads) == 0:
            raise EmptyDatabase

         return jsonify(all_leads)
    except EmptyDatabase as err:
        return err.message, 400

