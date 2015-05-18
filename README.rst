Flask Outdated Browser
=========================



.. image:: https://travis-ci.org/ondoheer/flask-outdated-browser.png?branch=master
   :target: https://travis-ci.org/ondoheer/flask-outdated-browser


A simple way to add outdated browser to your Flask project using python code.

Usage
---------

In flask add::

	from flask_outdated_browser import OutdatedBrowser 

	# regular way of initializing
	OutdatedBrowser(app)

	#it also handles Flask factory pattern
	outdated = Outdated()

	outdated.init_app(app)


Configuration Variables
-------------------------

The extension can handle the following configuration options that follow the original project capabilities


Browser support version
++++++++++++++++++++++++++

Determines which version of IE will be the first supported version for your app.

- **app.config["OUTDATED_BROWSER_FOR"]**, defaults to "IE10", accepts all the original project parameters.


Jquery Usage
++++++++++++++

Sets if jquery is used or not.

**app.config["OUTDATED_BROWSER_JQUERY"]**, defaults to False

AJAX support
++++++++++++++
Determines if AJAX is used for script rendering.

**app.config["OUTDATED_BROWSER_AJAX"]**, defaults to False

Minified files
++++++++++++++++
Determines if the .js and .css files are minimized or not.

**app.config["OUTDATED_BROWSER_MINIFIED"]**, defaults to True

Language to display
+++++++++++++++++++++

Accepts any outdatedbrowser language. It will be used to call the proper template.

**app.config["OUTDATED_BROWSER_LANGUAGE"]**, defaults to "en"

Usage in templates
--------------------

since usually the developer wants to have control of their *base.html* file, or is ussing a framework like **Boostratp** or **zurb Foundation**, I dediced the best sensible way to add the outdated browser code snippets would be macros.

to use it just add the following to your jinja2 templates::

	{% import "outdated/macros.html" as outdated %}

	<!-- In your header styles -->
	{{ outdated.style() }}

	<!-- in your body (just anywhere) -->
	{{ outdated.init() }}

	<!-- in your footer scripts, after jquery if you turned it on -->
	{{ outdated.script() }}







