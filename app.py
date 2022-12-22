from flask import Flask, request
import git

app = Flask(__name__)

@app.route('/update-code', methods=['POST'])
def update_code():
    if request.method == 'POST':
        repo = git.Repo('/home/scripts/python-events-handler')
        origin = repo.remotes.origin
        origin.pull()
        return 'Code successfully updated', 200
    else:
        return 'Wrong method', 500

@app.route('/')
def index():
    return 'OK', 200

@app.route('/metrics')
def get_metrics():
    return 'test:\t\ttest'