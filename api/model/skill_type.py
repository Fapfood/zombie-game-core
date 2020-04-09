from flask_restplus import Model, fields

SkillTypeModelSimple = Model('SkillType', {
    'id': fields.Integer(required=True, description='Skill type id'),
    'name': fields.String(required=True, description='Skill type name'),
})
