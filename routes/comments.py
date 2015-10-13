#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import logging
import json
from models import comment

class CommentListHandler(webapp2.RequestHandler):
    def get(self):
        logging.info('Getting all comments!')
        self.response.headers['Content-Type'] = 'application/json'
        self.response.write(json.dumps(comment.getList(100)))

    def post(self):
        #pop off the script name ('/api')
        #self.request.path_info_pop()
        #Load the JSON values that were sent to the server
        comment = json.loads(self.request.body)
        #Clever way to initialize the Data object without specifying each field
        # newObject = globals()[self.request.path_info[1:]](**comment)
        newObject = comment.Comment()
        newObject(**comment)
        #Returns the ID that was created
        self.response.write(str(newObject.put().id()))

class CommentItemHandler(webapp2.RequestHandler):
    def get(self, key):
        logging.info('Getting comment: ' + key)
        self.response.headers['Content-Type'] = 'application/json'
        self.response.write(json.dumps(comment.getItem(key)))

app = webapp2.WSGIApplication([
    (r'/comments', CommentListHandler),
    (r'/comments/(\d+)', CommentItemHandler),
])
