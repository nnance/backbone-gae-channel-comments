#backbone-gae-channel-comments

**What**

A project that shows the power of backbone.js and Google App Engine by creating a fully featured real time comments system.

**How**

By utilizing the Google App Engine Channel API all bower sessions are synchronized reflecting the latest comments in real time.

## Resources used

* [bower](http://bower.io)
* [preen](https://github.com/braddenver/preen)
* [google app engine sdk for python](https://cloud.google.com/appengine/downloads#Google_App_Engine_SDK_for_Python)

Client-side

* [Backbone.js](http://backbonejs.org/)
* [jQuery](http://jquery.com/)
* [Bootstrap](http://twitter.github.com/bootstrap/)

Server-side:

* [python](http://python.org/)
* [google app engine](https://cloud.google.com/appengine/docs)
* [gae channel api](https://cloud.google.com/appengine/docs/python/channel/)

## Getting Started
The repo has everything needed to get started by just running the GAE server with the following command:
### Starting GAE Server
```
dev_appserver.py .
```
The required dependencies are already included in the repo as it makes the deploymnent and development of the GAE application easier.  However, if you need to add or update the dependencies use the following:
### Install resources
```
$ npm install -g bower preen
```
### Install dependencies
```
$ bower install && preen
```
## Feedback
If you have any questions or feedback, feel free to contact me using [@NanceNick](https://twitter.com/NanceNick) on Twitter.

## License

The MIT License (MIT)
Copyright (c) 2015 Nick Nance.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
