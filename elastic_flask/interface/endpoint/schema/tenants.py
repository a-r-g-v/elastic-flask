from marshmallow import Schema, fields
from .tenant import TenantSchema

class TenantsSchema(Schema):
    tenants = fields.Nested(TenantSchema, many=True)
