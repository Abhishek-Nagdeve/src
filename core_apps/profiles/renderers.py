import json
from rest_framework.renderers import JSONRenderer

class ProfileJSONRenderers(JSONRenderer):
    charset = 'utf-8'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        status_code=renderer_context["response"].status_code
        errors = data.get('errors' , None)

        if errors is not None:
            return super(ProfileJSONRenderers,self).render(data)
        return json.dumps({"status_code":status_code,"profile":data})
    
class ProfilesJSONRenderers(JSONRenderer):
    charset = 'utf-8'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        status_code=renderer_context["response"].status_code
        errors = data.get('errors' , None)

        if errors is not None:
            return super(ProfileJSONRenderers,self).render(data)
        return json.dumps({"status_code":status_code,"profiles":data})