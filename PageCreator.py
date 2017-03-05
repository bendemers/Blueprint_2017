from flask import Flask, render_template
import urllib

app = Flask(__name__)

@app.route('/<path:realLink>/')
def pass_data(realLink):
    return realLink

if __name__ == '__main__':
    app.run()