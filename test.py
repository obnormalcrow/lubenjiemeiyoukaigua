num = 1
from flask import Flask

app = Flask(__name__)

@app.route("\index")
def index():
    return "index page"
if __name__ == "__main__"
    app.run(Debug=True)
        

