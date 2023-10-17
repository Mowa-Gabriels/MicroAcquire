from rest_framework import renderers
import json


class UserRenderers(renderers.JSONRenderer):
    charset= 'utf-8'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        response = ''

        # import pdb
        # pdb.set_trace()
        if 'ErrorDetail' in str(data):
            response = json.dumps({'errors':data})
        else:
            response = json.dumps({'data':data})

        return response