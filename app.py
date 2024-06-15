from flask import Flask, render_template, jsonify

app = Flask(__name__)
JOBS = [

    {
        'id':1,
        'title': 'Data Analyst',
        'location': 'Tema, Ghana',
        'salary': 'GHC5,000,000'
    },
    {
        'id':2,
        'title': 'Compu. Analyst',
        'location': 'Accra, Ghana',
        'salary': 'GHC8,000,000'
    },
    {
        'id':3,
        'title': 'Graphic De',
        'location': 'Spintex, Ghana',
        'salary': 'GHC2,000,000'
    },
]

@app.route("/")
def hello_world():
    return render_template('home.html', jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run(host='0.0.0.0' , debug=True)