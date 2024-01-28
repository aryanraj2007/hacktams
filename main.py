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
        
        return render_template('chat.html', processed_text=response, previous_text = context)
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
        context = """
        You are an AI assistant designed to provide users with enjoyable hobbies.
        They have provided some of their life information to help you decide on their hobbies.
        Their daily schedule: """ + response1 + """. Are they physically active: """ + response2 + """ 
        Do they enjoy social interaction: """ + response3 + """ Which types of activities they prefer: """ + response4 + """ 
        What they spend their time doing: """ + response5 + """ Mind type: """ + response6 + """ 
        Favorite school subject: """ + response7 + """ Content watched: """ + response8 + """ 
        Specific Interests: """ + response9 + """ Current hobbies: """ + response12 + """ 
         Is Competitive: """ + response13 + """
        Answer all prompts as if you were this AI assistant.
        Be as friendly and helpful as possible.
        Always end your response with a complete sentence."""
        output = generate("Provide some suitable hobbies with the information given", context)
        return render_template('output.html', previous_text = output)
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
        context = """You are an AI Assistant designed to increase an user's productivity.
        They have provided you with some of their life information to help you increase your productivity.
        Number of social media apps they use: """ + response1 + """. How long they use their phone every day: """ + response2 + """
         If they use a calendar or schedule: """ + response3 + """ What they do in their free time: """ + response4 + """
         How long they currently spend working every day: """ + response5 + """ What they think the cause of their lack of productivity is: """ + response6 + """
         How much sleep they get every day: """ + response7 + """ If they feel overwhelmed by their work: """ + response8 + """
         If they find their work environment stressful or loud: """ + response10 + """
         Answer all prompts as if you were this AI assistant.
        Be as friendly and helpful as possible.
        Always end your response with a complete sentence."""
        output = generate("Provide this person with some tips to increase their productivity", context)
        return render_template('output.html', previous_text = output)
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
        context = """You are an AI Assistant designed to recommend volunteering opportunities based on responses to the following questions 
        What they are passionate about: """ + response1 + """
         Favorite School Subject: """ + response2 + """
         Activities they participate in: """ + response3 + """
         Desired level of activity during volunteering""" + response4 + """
         Do they want to be hands-on when volunteering""" + response5 + """
         Do they like interacting with others: """ + response6 + """
         The extent to which they like critical thinking: """ + response7 + """
         Their favorite activities: """ + response8 + """
         Time they desire to spend volunteering: """ + response9 + """
         Reason for volunteering: """ + response10 + """ Suggest them some volunteering activities based off of these responses.
        Answer all prompts as if you were this AI assistant.
        Be as friendly and helpful as possible.
        Always end your response with a complete sentence."""
        output = generate("Provide this person with some volunteering opportunities", context)
        return render_template('output.html', previous_text = output)
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
    if request.method == 'GET':
        return render_template('output.html')
    
def generate(p1, p2):
    with model.chat_session(p2, prompt_template):
       
        return model.generate(p1)