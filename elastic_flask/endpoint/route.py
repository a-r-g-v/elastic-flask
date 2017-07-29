from flask import Blueprint

from .schema.tenant import TenantSchema
from .view.tenant import TenantView

api = Blueprint('api', __name__)

TenantView.register(api, trailing_slash=False)
