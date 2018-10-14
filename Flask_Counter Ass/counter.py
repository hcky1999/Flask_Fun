from flask import Flask, render_template, request, redirect, session
app=Flask(__name__)
app.secret_key ='aabbccdd'

@app.route('/')
def index():
    if "count" in session:
        session["count"] += 1
        print("*"*80,"count")
    else:
        session ["count"] = 1
        print ("#"*80,"COUNT")
    return render_template('index.html',count=session["count"])

@app.route("/destroy_session")
def clearSession():
    session.clear()
    print("#"*80,"COUNT")
    return redirect("/")

@app.route('/plusTwo', methods=['POST'])
def plusTwo():
    session['count'] += 1
    print("@"*80,"count")
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session['count'] = 0
    print("$"*80,"count")
    return redirect('/')


app.run(debug=True)
