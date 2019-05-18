from flask import Flask,render_template, request
import os

app = Flask(__name__)

@app.route("/sarcasm_detection")
def sar_detection():
    return render_template('sar_layout.html')

@app.route("/sar_submit",methods=["POST","GET"])
def sar_submit():
    sentence = request.form.get("sentence")

    # If there's no sentence
    if not sentence:
        return render_template('sar_failure.html')

    return render_template('sar_successful.html',sentence=sentence)

@app.route("/")
def index():
    return "Hello Phat, you have wonderfully deployed this app on path1!"

if __name__ == '__main__':
  port = int(os.environ.get("PORT", 5000))
  app.run(debug=True, port=port)
