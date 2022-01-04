from .BaseRepository import BaseRepository
from ..models import Cities

class CitiesRepository(BaseRepository):
    model = Cities
