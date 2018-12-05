from flask import Flask
from jinja2 import Template
import jinja2
import os

app = Flask(__name__)

template_dir = os.path.join(os.path.dirname(__file__), 'templates' )
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape = True)

def render_str(template,**params):
   t = jinja_env.get_template(template)
   return t.render(params)

def render(template, **kw):
   return render_str(template, **kw)

@app.route("/")
def hello():
    return render("index.html")

if __name__ == '__main__':
	app.run(debug = True)