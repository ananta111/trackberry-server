from database.db import db
import datetime


class Properties(db.EmbeddedDocument):
    time = db.DateTimeField(default=datetime.datetime.utcnow)


class Geometry(db.EmbeddedDocument):
    type = db.StringField()
    coordinates = db.ListField(db.FloatField())


class Feature(db.Document):
    type = db.StringField()
    properties = db.EmbeddedDocumentField(Properties)
    geometry = db.EmbeddedDocumentField(Geometry)
