from flask import Flask
import git

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    repo = git.Repo('/home/scripts/python-events-handler')
    origin = repo.remotes.origin
    origin.pull()
    return 'Ok'