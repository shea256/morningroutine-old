import os
from flask import Flask, render_template, send_from_directory

#----------------------------------------
# initialization
#----------------------------------------

app = Flask(__name__)

app.config.update(
    DEBUG = True,
)

app.config["SECRET_KEY"] = 'e2d01e58a1d829c5cefbc5e98dfc91d3e4da62ab6a522de3'

#----------------------------------------
# controllers
#----------------------------------------

@app.route("/")
def index():
    return render_template('index.html')

#----------------------------------------
# handlers
#----------------------------------------

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'ico/favicon.ico')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

#----------------------------------------
# launch
#----------------------------------------

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)