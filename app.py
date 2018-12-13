from flask import Flask
from jinja2 import Template
import jinja2
import os
from flask import Flask, request, redirect, url_for
from werkzeug.utils import secure_filename
from openpyxl import load_workbook
import string
import json

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = set(['xlsx'])


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

template_dir = os.path.join(os.path.dirname(__file__), 'templates' )
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape = True)

def render_str(template,**params):
   t = jinja_env.get_template(template)
   return t.render(params)

def render(template, **kw):
   return render_str(template, **kw)


def file_parse():
	wb = load_workbook(filename = 'uploads\\rating_test.xlsx',data_only=True)
	sheet = wb.active
	col_names = list(string.ascii_uppercase)
	col_names.append('AA') 
	col_names.append('AB')
	col_names.append('AC')
	l = []
	d = {}
	keys = []
	for i in col_names:
	    keys.append(sheet['%s1'%i].value)
	i = 0
	#print('A{}:AC{}'.format(sheet.min_row,sheet.max_row))
	for row in sheet.iter_rows('A{}:AC{}'.format(sheet.min_row + 1,sheet.max_row)):
	    i = 0
	    for cell in row:
	        d[keys[i]] = cell.value
	        i+=1
	    l.append(d)
	    d = {}
	return l

@app.route("/" , methods=['GET', 'POST'])
def hello():
	if request.method == 'POST':
		if 'file' not in request.files:
			flash('No file part')
			return redirect(request.url)
		file = request.files['file']
		if file.filename == '':
			flash('No selected file')
			return redirect(request.url)
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			return redirect(url_for('uploaded_file',filename=filename))
	else:		
		return render("index.html")
def search_name(name):
	for item in file_parse():
		if item["Фамилия, имя, отчество"] == name:
			return item
@app.route("/rating" , methods=['GET', 'POST'])
def get_data():
	name = request.args.get('name')
	d = json.dumps(search_name(name), ensure_ascii=False).encode('utf-8')
	return d

@app.route("/uploaded_file:<filename>" , methods=['GET', 'POST'])
def uploaded_file(filename):
	return render('success.html')
if __name__ == '__main__':
	app.run(debug = True)