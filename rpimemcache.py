#!/usr/bin/env python

# Copyright 2016 Google Inc.
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

# [START imports]
import os
import urllib
import paste

import webapp2
#from google.appengine.api import memcache

# [END imports]

# [START main_page]
class MainPage(webapp2.RequestHandler):

    def get(self):
        #if memcache.get('test'):
        #    message = memcache.get('test')
        #else:
        #    message = 'No content for key \'test\''
        message = 'test'
        self.response.write(message)

# [END main_page]


# [START guestbook]
class Guestbook(webapp2.RequestHandler):

    def post(self):
        guestbook_name = self.request.get('guestbook_name')
        query_params = {'guestbook_name': guestbook_name, 'content': 'content'}

        print(query_params)
        self.redirect('/?' + urllib.urlencode(query_params))
# [END guestbook]


# [START app]
app = webapp2.WSGIApplication([
    ('/', MainPage)
    ,('/sign', Guestbook),
], debug=True)

#def main():
#    from paste import httpserver
#    httpserver.serve(app, host='127.0.0.1', port='8088')

#if __name__ == '__main__':
#    main()
# [END app]
