"""
############################
# 1st phase - all in 1 app #
############################
1. flask hello world
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()

2. add other flask endpoints


3. hard code responses


4. look up how to accept only POST (GET is default)


5. return html for GET /
<form method="post" enctype="multipart/form-data" action="/upload" method="post">
  <div>
    <label for="file">Choose file to upload</label>
    <input type="file" id="file" name="form_file" accept="image/jpeg"/>
  </div>
  <div>
    <button>Submit</button>
  </div>
</form>

6. in GET /files return a hardcoded list for initial testing
files = ['file1.jpeg', 'file2.jpeg', 'file3.jpeg']

7. in GET / call the function for GET /files and loop through the list to add to the HTML
GET /
    ...
    for file in list_files():
        index_html += "<li><a href=\"/files/" + file + "\">" + file + "</a></li>"

    return index_html

8. in POST /upload - lookup how to extract uploaded file and save locally to ./files
def upload():
    file = request.files['form_file']  # item name must match name in HTML form
    file.save(os.path.join("./files", file.filename))

    return redirect("/")
#https://flask.palletsprojects.com/en/2.2.x/patterns/fileuploads/

9. in GET /files - look up how to list files in a directory

    files = os.listdir("./files")
    #TODO: filter jpeg only
    return files

10. filter only .jpeg
@app.route('/files')
def list_files():
    files = os.listdir("./files")
    for file in files:
        if not file.endswith(".jpeg"):
            files.remove(file)
    return files
"""
import os
from flask import Flask, redirect, request, send_file

os.makedirs('Project/files', exist_ok = True)

app = Flask(__name__)

@app.route('/')
def index():
    index_html="""
<form method="post" enctype="multipart/form-data" action="/upload" method="post">
  <div>
    <label for="file">Choose file to upload</label>
    <input type="file" id="file" name="form_file" accept="image/jpeg"/>
  </div>
  <div>
    <button>Submit</button>
  </div>
</form>"""    

    for file in list_files():
        index_html += "<li><a href=\"/Project/files/" + file + "\">" + file + "</a></li>"

    return index_html

@app.route('/upload', methods=["POST"])
def upload():
    file = request.files['form_file']  # item name must match name in HTML form
    file.save(os.path.join("./Project/files/", file.filename))

    return redirect("/")

@app.route('/Project/files')
def list_files():
    files = os.listdir("./Project/files")
    jpegs = []
    for file in files:
        if file.lower().endswith(".jpeg") or file.lower().endswith(".jpg"):
            jpegs.append(file)
    
    return jpegs

@app.route('/home/lukebro321123/Project/files/<filename>')
def get_file(filename):
  return send_file('/home/lukebro321123/Project/files/'+filename)

if __name__ == '__main__':
    app.run(debug=True)

