# from api_webserver.resources import account
import flask
from flask import request,jsonify
from flask.wrappers import Response
from flask_restful import Api,Resource
import pymysql
# from resources.test_user import Users,User
from flask import render_template


app = flask.Flask(__name__)
app.config['DEBUG'] = True
api = Api(app)

@app.route("/", methods=["get"])
def home():
    return render_template('index.html')

@app.route("/stock", methods=["get"])
def counts() :
    db, cursor = db_init()
    sql = """
           SELECT DATE_FORMAT(date,'%Y-%m-%d') date,stock_count,close_price FROM stock_database.table_02;
          """
    cursor.execute(sql)
    count_data = cursor.fetchall()
    db.close()
    return jsonify(count_data)


@app.route("/all", methods=["get"])
def all() :
    db, cursor = db_init()
    # sql = """
    #        SELECT DATE_FORMAT(date,'%Y-%m-%d') 1_date,open_price 2_open_price,close_price 3_close_price
    #        ,low_price 4_low_price,high_price 5_high_price
    #        FROM stock_database.table_02;
    #       """
    sql = """
        SELECT DATE_FORMAT(date,'%Y-%m-%d') date,open_price,close_price,low_price,high_price,FORMAT(stock_count,'no')
        FROM stock_database.stock_date;
        """
    cursor.execute(sql)
    count_data = cursor.fetchall()
    db.close()
    return jsonify(count_data)
    

def db_init():
        db = pymysql.connect('192.168.56.102','eason','671106','stock_database')
        cursor = db.cursor(pymysql.cursors.DictCursor)
        return db,cursor

if __name__ == '__main__':
    # app.run(port = 5555)
    app.run(host = '0.0.0.0' , port = 5555)