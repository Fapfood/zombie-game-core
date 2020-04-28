from flask_restplus import Model, fields

SkillTypeModelSimple = Model('SkillType', {
    'id': fields.Integer(required=True),
    'name': fields.String(required=True),
})
