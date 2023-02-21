from flask import Flask, render_template

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': 'Web developer',
  'location': 'mogdisho, somalia',
  'salary': 12300
}, {
  'id': 2,
  'title': 'mobile developer',
  'location': 'hargiesa, somalia',
  'salary': 9300
}, {
  'id': 3,
  'title': 'data analysist',
  'location': 'baydhabo, somalia',
  'salary': 7300
}, {
  'id': 4,
  'title': 'full stack developer',
  'location': 'mogdisho, somalia',
  'salary': 'remote'
}]


@app.route('/')
def home():
  return render_template('home.html', jobs=JOBS, company_name='abdirsaq')


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
