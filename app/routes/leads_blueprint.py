from flask import Blueprint
from app.controllers import *

bp_leads = Blueprint("bp_leads", __name__, url_prefix="/leads")

bp_leads.get("")(get_leads_controller)
bp_leads.post("")(post_lead_controller)
bp_leads.patch("")(patch_lead_controller)
bp_leads.delete("")(delete_lead_controller)


