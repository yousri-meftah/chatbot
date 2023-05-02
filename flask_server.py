from flask import Flask, request ,render_template
from chatbot import chatbot_response,yousri, symptoms

app = Flask(__name__,template_folder='template')

@app.route('/chatbot', methods=['POST'])
def send_response():
    request_data = request.get_json()
    
    msg = request_data['msg']
    print(msg)
    return yousri(msg)

@app.route('/sympotoms', methods=['GET'])
def send_symp():
     return "symptoms"
 
@app.route('/', methods=['GET'])
def getindex():
      return render_template("index.html")
if __name__ == '__main__':
    app.run(debug=True, port=8000)