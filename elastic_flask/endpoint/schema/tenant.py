from marshmallow import Schema, fields

class TenantSchema(Schema):
    id = fields.UUID()
    name = fields.String()
    domain = fields.String()
    is_avaiable = fields.Boolean()
    created_at = fields.LocalDateTime()
    updated_at = fields.LocalDateTime()
