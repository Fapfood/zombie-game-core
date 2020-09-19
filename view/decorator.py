import functools
import json

from flask_restplus import marshal

from view.display import render_part


def modal_body_with(cls):
    def _wrap(func):
        @functools.wraps(func)  # lifts docstring and name
        def _func(*args, **kwargs):
            res = func(*args, **kwargs)
            if type(res) == str:
                return render_part(template='modal-body/modal-body-message.html',
                                   color='green', message=res)
            else:
                json_message = json.dumps(res)
                json_message = marshal(json_message, cls, skip_none=True)
                return render_part(template='modal-body/modal-body-json.html',
                                   modal_id='common-modal', json_message=json_message)

        return _func

    return _wrap
