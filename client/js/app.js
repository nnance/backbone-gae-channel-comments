// http://backbonetutorials.com/organizing-backbone-using-modules/
require.config({
  baseUrl: "/js/",
  paths: {
    templates: '../templates',
    jquery: '../components/jquery/dist/jquery.min',
    underscore: '../components/underscore/underscore-min',
    backbone: '../components/backbone/backbone-min',
    bootstrap: '../components/bootstrap/dist/js/bootstrap.min',
    moment: '../components/moment/min/moment.min',
    text : '../components/requirejs-text/text'
  },
  shim: {
    underscore: {
      exports: "_"
    },
    backbone: {
      deps: ['underscore', 'jquery'],
      exports: 'Backbone'
    },
    bootstrap: {
      deps: ['jquery'],
      exports: 'bootstrap'
    },
    moment: {
      exports: 'moment'
    }
  }
});


require([
  'jquery',
  'underscore',
  'backbone',
  './MainRouter',
], function($, _, Backbone, MainRouter) {
	'use strict';

  MainRouter.initialize();

});
