from flask import Flask, render_template
import json
app=Flask(__name__)


with open('donut_description.json','r', encoding='utf-8') as donut_description:
    donuts=json.load(donut_description,)


@app.route('/')
def resp():
    return render_template('index.html', donuts=donuts["donuts"])


print(type(donuts["donuts"]))


@app.route('/sosi')
def res():
    return render_template('base.html',body='sosi')
app.run(debug=True)