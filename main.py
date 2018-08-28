from flask import Flask, request, redirect, render_template


app = Flask(__name__)
app.config['DEBUG'] = True


tasks = []

@app.route('/', methods=['POST', 'GET'])
def index():

    if request.method == 'POST':

        return redirect('/')
        

    return render_template('inputs.html',title="Signups", tasks = tasks)

if __name__ == '__main__':
    app.run()