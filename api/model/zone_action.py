from flask_restplus import Model, fields

ZoneActionModel = Model('ZoneAction', {
    'id': fields.Integer(required=True),
})
