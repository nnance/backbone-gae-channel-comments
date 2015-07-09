import logging

from google.appengine.ext import ndb

class Comment(ndb.Model):
    created = ndb.DateTimeProperty(auto_now_add=True)
    text = ndb.StringProperty()
    author = ndb.StringProperty()

def getList(count):
    comments = Comment.query().order(Comment.created).fetch(count)
    to_return = [toJSON(comment) for comment in comments]
    return to_return

def getItem(key):
    comment = Comment.query(Comment.key == key).fetch(1)
    return toJSON(comment)

def toJSON(comment):
    return {
        'key': comment.key.urlsafe(),
        'created': str(comment.created),
        'text': comment.text,
        'author': comment.author
    }
