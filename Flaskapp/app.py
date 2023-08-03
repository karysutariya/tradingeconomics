from flask import Flask, render_template
from indicator import real_data

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html', my_data = real_data[0], my_data2 = real_data[1])
 
if __name__ == "__main__":
    app.run(debug=False)
