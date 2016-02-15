from django.db import models


class KindQuerySet(models.QuerySet):
    def emails(self):
        return self.filter(kind=self.model.EMAIL)

    def phones(self):
        return self.filter(kind=self.model.PHONE)


class PeriodManager(models.Manager):
    def at_mornign(self):
        # return self.filter(start__lt)
        pass