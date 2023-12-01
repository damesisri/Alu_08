from App import app

@app.routes('/')
def index():
    return 'Hello Flask App'