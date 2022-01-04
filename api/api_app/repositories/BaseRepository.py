from django.db import models

class BaseRepository:

    def all(self):
        return self.model.objects.all()

    def create(self, **object):
        return self.model.objects.create(**object)

    def delete(self, pk):
        self.model.objects.filter(id=pk).delete()

    def update(self, pk, object):
        self.model.objects.filter(id=pk).update(**object)

    def filter(self, **kwargs):
        return self.model.objects.filter(**kwargs)

    def values_list(self, col, flat=True):
        return self.model.objects.values_list(col, flat=flat)

    def sql(self, query):
        return self.model.objects.raw(query)
