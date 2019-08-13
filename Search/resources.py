from import_export import resources
from .models import api_data

class api_dataResource(resources.ModelResource):
    class Meta:
        model = api_data
        