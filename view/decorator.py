import functools
import json

from view.display import render_part


def modal_result(func):
    @functools.wraps(func)
    def _func(*args, **kwargs):
        res = func(*args, **kwargs)
        if type(res) == str:
            return render_part(template='modal-body/modal-body-message.html',
                               color='green', message=res)
        else:
            json_message = json.dumps(res)
            return render_part(template='modal-body/modal-body-json.html',
                               modal_id='common-modal', json_message=json_message)

    return _func
