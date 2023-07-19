from flask import Flask, request, Response, redirect
import os
import jinja2
app = Flask(__name__)

dictionary = { 'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s',
               'g':'t', 'h':'u', 'i':'v', 'j':'w', 'k':'x', 'l':'y',
               'm':'z', 'n':'a', 'o':'b', 'p':'c', 'q':'d', 'r':'e',
               's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k',
               'y':'l', 'z':'m' }

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

def rot(text):
    rot13 = ''
    for symbol in text:
        if symbol.isupper():
            symbol = symbol.lower()
            rot13 = rot13 + dictionary.get(symbol).upper()
        elif symbol.islower():
            rot13 = rot13 + dictionary.get(symbol)
        if symbol not in dictionary:
            rot13 = rot13 + symbol
    return rot13

# @app.route("/rot13", methods=['GET'])
# def get():
#     t = jinja_env.get_template("textarea.html")
#     return t.render()

@app.route("/rot13", methods=['GET', 'POST'])
def page():
    t = jinja_env.get_template("textarea.html")
    text = ''
    if request.method == "POST":
        text = request.form["text"]
        if text != None:
            text = rot(text)
    return t.render(text=text)


# if __name__ == "__main__":
#     app.run()