from flask import Flask, render_template

app = Flask(__name__)

@app.route('/<string:page_name>/')

def static_page(page_name):
    return render_template(page_name + "s.html")

if __name__ == '__main__':
    app.run()