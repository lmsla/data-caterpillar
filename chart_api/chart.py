import flask
from flask import request,jsonify,make_response
from flask_restful import Api,Resource
import pymysql
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
from flask import render_template
import decimal
import json
# import sqlite3
app = flask.Flask(__name__)
app.config["DEBUG"]=True
api =Api(app)


@app.route("/debtratio/<code>", methods=["get"])
def home(code):
    return render_template('debt_ratio.html',code_template = code)

@app.route("/eps/<code>", methods=["get"])
def eps(code):
    return render_template('eps.html',code_template = code)

@app.route('/revenue/<code>', methods=["get"])
def revenue(code):
    return render_template('revenue.html',code_template = code)

@app.route("/<code>", methods=["get"])
def home1(code):
    return render_template('index.html',code_template = code)

# ========================== GET DATA ====================================

@app.route('/getdebtratio/<code>', methods=["GET"])
def debt_ratio(code):
    db, cursor = db_init()
# json無法解析decimal格式，必須先將有小數的值轉為double
    sql = """  Select concat(年度,'-',季度) as labels, convert(( 負債總計/資產總計)*100,double(10,2)) as value From stock_database.balancesheet915
                    where code = '{}'
            """.format(code)
    cursor.execute(sql)
    one = cursor.fetchall()
    db.close()
    return jsonify(one)

def db_init():
    db = pymysql.connect('192.168.56.102','eason','671106','stock_database')
    cursor = db.cursor(pymysql.cursors.DictCursor)
    return db,cursor
  
@app.route('/geteps/<code>', methods=["GET"])
def geteps(code):
    db, cursor = db_init()
# json無法解析decimal格式，必須先將有小數的值轉為double
    sql = """   SELECT 年度 as labels , 基本每股盈餘 as value FROM stock_database.incomestatement913 where code = '{}' and 季度 = 4 
    or code = '{}' and 年度 = 109 and 季度= 3 order by 年度
            """.format(code,code)
    cursor.execute(sql)
    one = cursor.fetchall()
    db.close() 
    return jsonify(one)

@app.route('/getrevenue/<code>',methods=["GET"])
def getrevenue(code):
    db, cursor = db_init()
    sql = """
    SELECT concat(t1.年度,'-',t1.季度) as labels,  	
		IF (t1.季度=1, t1.營業收入,t1.營業收入-1- t2.營業收入) as value
    FROM stock_database.incomestatement913 t1 left JOIN stock_database.incomestatement913 t2 ON t1.id = t2.id+1  where t1.code='{}' order by t1.年度,t1.季度;
        """.format(code)

    cursor.execute(sql)
    one = cursor.fetchall()
    db.close()
    return jsonify(one)


@app.route("/all/<code>", methods=["get"])
def all(code) :
    db, cursor = db_init()
    sql = """
        SELECT DATE_FORMAT(date,'%Y-%m-%d') date,open_price,close_price,low_price,high_price,FORMAT(stock_count,'no')
        FROM stock_database.stock_date  where code = '{}';
        """.format(code)

    cursor.execute(sql)
    count_data = cursor.fetchall()
    db.close()
    return jsonify(count_data)

if __name__ == '__main__':
  app.run(host='0.0.0.0',port=8000)