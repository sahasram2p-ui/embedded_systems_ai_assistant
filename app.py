from flask import Flask, render_template, request, jsonify
from google import genai
from config import GEMINI_API_KEY, GEMINI_MODEL

app=Flask(__name__)
client=genai.Client(api_key=GEMINI_API_KEY)
DOMAIN_PROMPT='You are Embedded Systems AI Assistant. Answer ONLY questions directly related to embedded-systems. Stay focused on the allowed domain topics and provide clear, educational, student-friendly explanations. Do not answer unrelated questions. For unrelated questions, reply exactly: "Sorry, I can answer only embedded-systems related questions." For physical hardware, use correct voltage/current ratings, datasheets and laboratory safety practices.'

@app.route("/")
def home(): return render_template("index.html")

@app.route("/api/chat",methods=["POST"])
def chat():
    try:
        data=request.get_json(silent=True) or {}
        msg=data.get("message","").strip()
        if not msg: return jsonify({"success":False,"error":"Please enter a message."}),400
        response=client.models.generate_content(model=GEMINI_MODEL,contents=f"{DOMAIN_PROMPT}\n\nUser question:\n{msg}")
        return jsonify({"success":True,"reply":(response.text or "").strip()})
    except Exception as e:
        print("ERROR:",repr(e))
        return jsonify({"success":False,"error":str(e)}),500

if __name__=="__main__": app.run(debug=True,host="127.0.0.1",port=5000)
