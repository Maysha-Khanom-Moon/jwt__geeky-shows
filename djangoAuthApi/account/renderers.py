from rest_framework import renderers
import json

class UserRenderer(renderers.JSONRenderer):
    charset = 'utf-8'
    def render(self, data, accepted_media_type=None, renderer_context=None):
        # sourcery skip: assign-if-exp, inline-immediately-returned-variable
        response = ''

        if 'ErrorDetail' in str(data):
            return json.dumps({'errors': data})

        else:
            return json.dumps(data)