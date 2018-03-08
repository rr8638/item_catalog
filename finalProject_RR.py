from flask import Flask, render_template, request, redirect, jsonify, url_for
app = Flask(__name__)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup_RR import Company, Base, BoardGame
from flask_debugtoolbar import DebugToolbarExtension


engine = create_engine('sqlite:///gamemenu.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()
app.debug = True
app.config['SECRET_KEY'] = 'totallysecretkey'
toolbar = DebugToolbarExtension(app)

##########################################JSON
#@app.route('/company/<int:company_id>/boardgame/<int:boardgame_id>')
@app.route('/company/<int:company_id>/boardgame/JSON/')
def BoardGameListJSON(company_id):
    #company = session.query(Company).filter_by(id=company_id).one()

    items = session.query(BoardGame).filter_by(company_id= company_id)
    output = ''

    # for i in items:
    #     output += i.name
    #     output += '</br>'
    #     output += i.cost
    #     output += '</br>'
    #     output += i.description
    #     output += '</br>'
    # return output
    # print(items.serialize)
    return jsonify(BoardGames=[i.serialize for i in items])

@app.route('/company/JSON/')
def companyJSON():
    companies = session.query(Company).all()
    for i in companies:
        print(i.name)
    return jsonify(companies=[i.serialize for i in companies])

@app.route('/company/<int:company_id>/boardgame/<int:boardgame_id>/JSON/')
def BoardGameJSON(company_id,boardgame_id):
    item = session.query(BoardGame).filter_by(id = boardgame_id, company_id = company_id)
    return jsonify(BoardGames=[i.serialize for i in item])



#######################################crud

#Fake data goes here









@app.route('/')
@app.route('/company/')
def showCompanies():
    compList = session.query(Company).all()

    return render_template('companies.html',
    company_id = Company.id,
    companies = compList
    )

@app.route('/company/new/', methods = ['GET', 'POST'])
def newCompany():
    if request.method == 'POST':
        #<Request 'http://localhost:5000/restaurant/new/' [POST]>
        #<Request 'http://localhost:5000/company/new' [POST]>


        newCompany = Company(name = request.form['name'])
        session.add(newCompany)
        session.commit()
        return redirect(url_for('showCompanies'))
    else:
        return render_template('newCompany.html')

#fix below render_template code
@app.route('/company/<int:company_id>/boardgame/')
def showboardgame(company_id):

    items = session.query(BoardGame).filter_by(company_id = company_id)
    comp = session.query(Company).filter_by(id = company_id).one()

    return render_template('boardgame_menu.html',

    bgame = [i for i in items],
    company = comp.name)

@app.route('/company/<int:company_id>/edit/', methods = ['GET', 'POST'])
def editCompany(company_id):
    editedCompany = session.query(Company).filter_by(id=company_id).one()
    if request.method == 'POST':
         if request.form['name']:
             editedCompany.name = request.form['name']
             return redirect(url_for('showCompanies'))
    else:
        return render_template(
             'editCompany.html', company = editedCompany
         )

@app.route('/company/delete/')
def deleteCompany():
    compList = session.query(Company).all()
    return "4"


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
