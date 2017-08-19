"""
TODO: main page
- Dashboard
- Generate Report Button
	- Filter reports
	- Select reports
"""

#TODO: create report

from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

def connect(database_name="safety"):
    """Connects to database"""
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        cursor = db.cursor()
        return db, cursor
    except:
        print ("<error message>")

@app.route('/')
@app.route('/dashboard/')
def dashboard():
	"""Loads the dashboard page"""
	db, cursor = connect()
    query = """
            SELECT articles.title, count(*) as num
                FROM log JOIN articles
                ON log.path = concat('/article/', articles.slug)
                GROUP BY articles.title
                ORDER BY num desc
                LIMIT 3;
            """
    cursor.execute(query)
    results = cursor.fetchall()
    return render_template('dasbhoard.html'query = query)
    db.close()

@app.route('/reports/')
def dashboard():
	return "Reports Page for incidents and audits"

@app.route('/newactionitem/')
def dashboard():
	return "New Action Item Page"

@app.route('/newincident/')
def dashboard():
	return "New Report Page"

@app.route('/newaudit/')
def dashboard():
	return "New Audit Page"

@app.route('/incident/edit/<int:id>')
def dashboard():
	return "Edit incident report %s" % id

@app.route('/aduit/edit/<int:id>')
def dashboard():
	return "Edit audit page %s" % id

@app.route('/actionitem/edit/<int:id>')
def dashboard():
	return "Edit action item %s" % id

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)