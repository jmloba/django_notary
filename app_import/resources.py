from import_export import resources
from app_import.models import Phil_City


    
class CityResource(resources.ModelResource):
  class Meta:
    model= Phil_City