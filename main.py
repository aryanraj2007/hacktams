from gpt4all import GPT4All
from flask import Flask, render_template, request


model = GPT4All("gpt4all-13b-snoozy-q4_0.gguf")

prompt_template = ""
response = ""
prompt = ""
context = """"""
app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def index():
     if request.method == 'POST':
        prompt = request.form.get('Prompt')
        context = request.form.get('freeform')

        response = generate(prompt, context)
        
        return render_template('index.html', processed_text=response, previous_text = context)
     if request.method == 'GET':
          return render_template('index.html')
    
@app.route('/hobbies', methods = ['POST', 'GET'])
def hobbies():   
    if request.method == 'POST':
        response1 = request.form.get("response1")
        response2 = request.form.get("response2")
        response3 = request.form.get("response3")
        response4 = request.form.get("response4")
        response5 = request.form.get("response5")
        response6 = request.form.get("response6")
        response7 = request.form.get("response7")
        response8 = request.form.get("response8")
        response9 = request.form.get("response9")
        response10 = request.form.get("response10")
        response11 = request.form.get("response11")
        response12 = request.form.get("response12")
        response13 = request.form.get("response13")
        return render_template('output.html')
    if request.method == 'GET':
        return render_template('hobbies.html')
@app.route('/productivity', methods = ['POST', 'GET'])
def productivity():   
    if request.method == 'POST':
        response1 = request.form.get("response1")
        response2 = request.form.get("response2")
        response3 = request.form.get("response3")
        response4 = request.form.get("response4")
        response5 = request.form.get("response5")
        response6 = request.form.get("response6")
        response7 = request.form.get("response7")
        response8 = request.form.get("response8")
        response9 = request.form.get("response9")
        response10 = request.form.get("response10")
        return render_template('output.html')
    if request.method == 'GET':
        return render_template('productivity.html')
@app.route('/volunteering', methods = ['POST', 'GET'])
def volunteering():
    if request.method == 'POST':
        response1 = request.form.get("response1")
        response2 = request.form.get("response2")
        response3 = request.form.get("response3")
        response4 = request.form.get("response4")
        response5 = request.form.get("response5")
        response6 = request.form.get("response6")
        response7 = request.form.get("response7")
        response8 = request.form.get("response8")
        response9 = request.form.get("response9")
        response10 = request.form.get("response10")   
        return render_template('output.html')
    if request.method == 'GET':
        return render_template('volunteering.html')

@app.route('/output', methods = ['POST', 'GET'])
def output(): 
    if request.method == 'POST':
        response1 = request.form.get("response1")
        response2 = request.form.get("response2")
        response3 = request.form.get("response3")
        response4 = request.form.get("response4")
        response5 = request.form.get("response5")
        response6 = request.form.get("response6")
        response7 = request.form.get("response7")
        response8 = request.form.get("response8")
        response9 = request.form.get("response9")
        response10 = request.form.get("response10")
        return render_template('output.html')
    
def generate(p1, p2):
    with model.chat_session(p2, prompt_template):
       
        return model.generate(p1)
