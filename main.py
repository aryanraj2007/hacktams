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
    return render_template('hobbies.html')

@app.route('/productivity', methods = ['POST', 'GET'])
def productivity():   
    return render_template('productivity.html')

@app.route('/volunteering', methods = ['POST', 'GET'])
def volunteering():   
    return render_template('volunteering.html')
    
def generate(p1, p2):
    with model.chat_session(p2, prompt_template):
       
        return model.generate(p1)
