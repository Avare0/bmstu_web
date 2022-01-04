from .BaseRepository import BaseRepository
from ..models import User
class UsersRepository(BaseRepository):
    model = User

    # def create(self, instance):
    #     # raise KeyError(instance)
    #     instance = self.model.objects.create(instance.data)
    #     return instance
