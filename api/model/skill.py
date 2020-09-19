from flask_restplus import Model, fields

SkillModel = Model('Skill', {
    'id': fields.Integer(required=True),
    'type': fields.String(required=True),
    'level': fields.Integer(required=True),
})
