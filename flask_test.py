from flask import Flask,request,jsonify

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return ("<h1>Home Page</h1>")

@app.route('/test',methods = ['POST'])
def test():
    inputStr = request.get_json()
    inputStr = inputStr["string_to_cut"]
    outputStr = ""
    for i in range(len(inputStr)):
        if (i + 1)%3 == 0:
            outputStr += inputStr[i]
    outjson = {"return_string":outputStr}
    return (jsonify(outjson))


if __name__ == '__main__':
   app.run(debug = True)