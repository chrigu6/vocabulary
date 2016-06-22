from django.contrib.auth.models import User
from django.db import models

class Language(models.Model):
    name = models.CharField(default="", max_length=200, primary_key=True)
    short = models.CharField(default="", max_length=2)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Language'
        verbose_name_plural = 'Languages'

class Word(models.Model):
    word = models.CharField(default="", max_length=200)
    language = models.ForeignKey(Language)

    def __unicode__(self):
        return self.word+ " ("+self.language.short+")"

    class Meta:
        verbose_name = 'Word'
        verbose_name_plural = 'Words'
        unique_together = (("word", "language"),)

class Card(models.Model):
    asked = models.IntegerField(default=0)
    correct = models.IntegerField(default=0)
    first_language = models.ForeignKey(Language, related_name="first_language")
    second_language = models.ForeignKey(Language, related_name="second_language")
    first_language_word = models.ForeignKey(Word)
    second_language_words = models.ManyToManyField(Word, related_name="second_language")

    def __unicode__(self):
        return self.first_language_word + " " + self.second_language

    class Meta:
        verbose_name = 'Card'
        verbose_name_plural = 'Cards'

class Set(models.Model):
    name = models.CharField(default="", max_length=200)
    date_created = models.DateField(auto_now=True)
    owner = models.ForeignKey(User, unique=False)
    cards = models.ManyToManyField(Card)
    first_language = models.ForeignKey(Language, related_name="first_language")
    second_language = models.ForeignKey(Language, related_name="second_language")

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Set'
        verbose_name_plural = 'Sets'
        unique_together = (("name", "owner"),)





