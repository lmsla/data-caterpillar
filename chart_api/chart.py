import flask
from flask import request,jsonify,make_response
from flask_restful import Api,Resource
# from resource1.chart1 import One
import pymysql
# from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template
import decimal
import json
# import sqlite3
app = flask.Flask(__name__)
app.config["DEBUG"]=True
api =Api(app)
# api.add_resource(All,'/All')
# api.add_resource(One,'/One/1101')
# api.add_resource(Select,'/select/Taiwan')
# api.add_resource(Death,'/death/5000')
# api.add_resource(User,'/user/<id>')
# api.add_resource(Accounts,'/Accounts')
# api.add_resource(Account,'/Account/<id>')


@app.route('/hi' , methods = ['GET'])
def hi():
  return '<h3>hello!<h3>'

@app.route("/debtratio/<code>", methods=["get"])
def home(code):
    return render_template('debt_ratio.html',code_template = code)

@app.route("/eps/<code>", methods=["get"])
def eps(code):
    return render_template('eps.html',code_template = code)

@app.route('/re/<code>', methods=["get"])
def re(code):
    return render_template('res.html',a = code)

# def db_init():
#     db = pymysql.connect('192.168.56.104','russell','pn12345','STOCK')
#     cursor = db.cursor(pymysql.cursors.DictCursor)
#     return db,cursor


@app.route('/getdebtratio/<code>', methods=["GET"])
def debt_ratio(code):
    db, cursor = db_init()
# json無法解析decimal格式，必須先將有小數的值轉為double
    sql = """  Select concat(年度,'-',季度) as labels, convert(( 負債總計/資產總計)*100,double(10,2)) as value From STOCK.balancesheet915
                    where code = '{}'
            """.format(code)
    cursor.execute(sql)
    one = cursor.fetchall()
    db.close()
    # response={
    #     'data':one
    # }    
    return jsonify(one)

def db_init():
    db = pymysql.connect('192.168.56.104','russell','pn12345','STOCK')
    cursor = db.cursor(pymysql.cursors.DictCursor)
    return db,cursor
  
@app.route('/geteps/<code>', methods=["GET"])

def geteps(code):
    db, cursor = db_init()
# json無法解析decimal格式，必須先將有小數的值轉為double
    sql = """   SELECT 年度 as labels , 基本每股盈餘 as value FROM STOCK.incomestatement913 where code = '{}' and 季度 = 4 
    or code = '{}' and 年度 = 109 and 季度= 3 order by 年度
            """.format(code,code)
    cursor.execute(sql)
    one = cursor.fetchall()
    db.close()
    # response={
    #     'data':one
    # }    
    return jsonify(one)

@app.route('/get/<code>',methods=["GET"])

def getrevenue(code):
    db, cursor = db_init()
    sql = """
    SELECT concat(t1.年度,'-',t1.季度) as labels,  	
		IF (t1.季度=1, t1.營業收入,t1.營業收入-1- t2.營業收入) as value
FROM STOCK.`8888` t1 left JOIN STOCK.`8888` t2 ON t1.id = t2.id+1  where t1.code='{}' order by t1.年度,t1.季度;
        """.format(code)

    cursor.execute(sql)
    one = cursor.fetchall()
    db.close()
    return jsonify(one)

# def db_init():
#     db = pymysql.connect('192.168.56.104','russell','pn12345','STOCK')
#     cursor = db.cursor(pymysql.cursors.DictCursor)
#     return db,cursor
# def db_init():
#     db = pymysql.connect('192.168.56.104','russell','pn12345','STOCK')
#     cursor = db.cursor(pymysql.cursors.DictCursor)
#     return db,cursor
    

if __name__ == '__main__':
  app.run(host='0.0.0.0',port=8000)