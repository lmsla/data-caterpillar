from flask_restful import Resource , reqparse
from flask import jsonify , make_response
import pymysql

parser = reqparse.RequestParser()
parser.add_argument('代號')
parser.add_argument('年度')
parser.add_argument('季度')
parser.add_argument('流動資產')
parser.add_argument('非流動資產')
parser.add_argument('資產總計')
parser.add_argument('流動負債')
parser.add_argument('非流動負債')
parser.add_argument('負債總計')
parser.add_argument('股本')
parser.add_argument('資本公積')
parser.add_argument('保留盈餘')
parser.add_argument('其他權益')
parser.add_argument('庫藏股票')
parser.add_argument('權益總計')
parser.add_argument('每股淨值')

# class All(Resource):
#     def db_init(self):
#         db = pymysql.connect('localhost','root','pn123456','web_API')
#         cursor = db.cursor(pymysql.cursors.DictCursor)
#         return db , cursor
#     def get(self):
#         db = pymysql.connect('localhost','root','pn123456','web_API')
#         cursor = db.cursor(pymysql.cursors.DictCursor)
#         sql = """ Select * From web_API.covid19_activity where deleted = False """

#         cursor.execute(sql)
#         All = cursor.fetchall()
#         db.close()
#         response={
#             'data' : All
#         }
#         return jsonify(response)
        
    # def post(self):
    #     db,cursor = self.db_init()
    #     arg = parser.parse_args()
    #     One ={
    #         'PEOPLE_POSITIVE_CASES_COUNT' : arg['PEOPLE_POSITIVE_CASES_COUNT'],
    #         'COUNTY_NAME' : arg['COUNTY_NAME'],
    #         'PROVINCE_STATE_NAME':arg['PROVINCE_STATE_NAME'],
    #         'REPORT_DATE' : arg['REPORT_DATE'],
    #         'CONTINENT_NAME' : arg['CONTINENT_NAME'],
    #         'DATA_SOURCE_NAME' : arg['DATA_SOURCE_NAME'],
    #         'PEOPLE_DEATH_NEW_COUNT' : arg['PEOPLE_DEATH_NEW_COUNT'],
    #         'COUNTY_FIPS_NUMBER' : arg['COUNTY_FIPS_NUMBER'],
    #         'COUNTRY_ALPHA_3_CODE' : arg['COUNTRY_ALPHA_3_CODE'],
    #         'COUNTRY_SHORT_NAME' : arg['COUNTRY_SHORT_NAME'],
    #         'COUNTRY_ALPHA_2_CODE' : arg['COUNTRY_ALPHA_2_CODE'],
    #         'PEOPLE_POSITIVE_NEW_CASES_COUNT' : arg['PEOPLE_POSITIVE_NEW_CASES_COUNT'],
    #         'PEOPLE_DEATH_COUNT' : arg['PEOPLE_DEATH_COUNT'],
    #     }
    #     sql = """
    #         Insert into web_API.covid19_activity
    #         (PEOPLE_POSITIVE_CASES_COUNT,COUNTY_NAME,PROVINCE_STATE_NAME,REPORT_DATE,
    #         CONTINENT_NAME,DATA_SOURCE_NAME,PEOPLE_DEATH_NEW_COUNT,
    #         COUNTY_FIPS_NUMBER,COUNTRY_ALPHA_3_CODE,COUNTRY_SHORT_NAME,
    #         COUNTRY_ALPHA_2_CODE,PEOPLE_POSITIVE_NEW_CASES_COUNT,
    #         PEOPLE_DEATH_COUNT)values('{}','{}','{}','{}','{}','{}','{}',
    #         '{}','{}','{}','{}','{}','{}') """.format(One['PEOPLE_POSITIVE_CASES_COUNT'],One['COUNTY_NAME'],
    #         One['PROVINCE_STATE_NAME'],One['REPORT_DATE'],One['CONTINENT_NAME'],One['DATA_SOURCE_NAME'],One['PEOPLE_DEATH_NEW_COUNT'],
    #         One['COUNTY_FIPS_NUMBER'],One['COUNTRY_ALPHA_3_CODE'],One['COUNTRY_SHORT_NAME'],
    #         One['COUNTRY_ALPHA_2_CODE'],One['PEOPLE_POSITIVE_NEW_CASES_COUNT'],One['PEOPLE_DEATH_COUNT'])
        
    #     result = cursor.execute(sql)
    #     db.commit()
    #     db.close()
    #     response={
    #         'result':True
    #     }
    #     return jsonify(response)

class One(Resource):
    def db_init(self):
        db = pymysql.connect('192.168.56.104','russell','pn12345','STOCK')
        cursor = db.cursor(pymysql.cursors.DictCursor)
        return db,cursor
    def get(self):
        db,cursor = self.db_init()
        sql = """ Select 季度 as labels, 資產總計 as value From STOCK.balancesheet915
                    where code = 1101;
            """
        cursor.execute(sql)
        One = cursor.fetchall()
        db.close()
        response={
            'data':One
        }
        return jsonify(response)
    

    
    # def patch(self,id):
    #     db,cursor=self.db_init()
    #     arg = parser.parse_args()
    #     One ={
    #         'PEOPLE_POSITIVE_CASES_COUNT' : arg['PEOPLE_POSITIVE_CASES_COUNT'],
    #         'COUNTY_NAME' : arg['COUNTY_NAME'],
    #         'REPORT_DATE' : arg['REPORT_DATE'],
    #         'CONTINENT_NAME' : arg['CONTINENT_NAME'],
    #         'DATA_SOURCE_NAME' : arg['DATA_SOURCE_NAME'],
    #         'PEOPLE_DEATH_NEW_COUNT' : arg['PEOPLE_DEATH_NEW_COUNT'],
    #         'COUNTY_FIPS_NUMBER' : arg['COUNTY_FIPS_NUMBER'],
    #         'COUNTRY_ALPHA_3_CODE' : arg['COUNTRY_ALPHA_3_CODE'],
    #         'COUNTRY_SHORT_NAME' : arg['COUNTRY_SHORT_NAME'],
    #         'COUNTRY_ALPHA_2_CODE' : arg['COUNTRY_ALPHA_2_CODE'],
    #         'PEOPLE_POSITIVE_NEW_CASES_COUNT' : arg['PEOPLE_POSITIVE_NEW_CASES_COUNT'],
    #         'PEOPLE_DEATH_COUNT' : arg['PEOPLE_DEATH_COUNT']
    #     }
    #     query=[]
    #     for key,value in One.items():
    #         if value != None:
    #             query.append(key + '='+" '{}' ".format(value))
    #     query = ",".join(query)
    #     sql=""" Update web_API.covid19_activity Set {} where id = "{}"
    #             """.format(query,id)
    #     cursor.execute(sql)
    #     db.commit()
    #     db.close()
    #     response={
    #         'result':True
    #     }
    #     return jsonify(response)

    # def delete(self,id):
    #     db,cursor=self.db_init()
    #     sql=""" Update web_API.covid19_activity Set deleted = True where id = "{}"
    #             """.format(id)
    #     cursor.execute(sql)
    #     db.commit()
    #     db.close()
    #     response={
    #         'result':True
    #     }
    #     return jsonify(response)
    
# class Select(Resource):
#     def db_init(self):
#         db = pymysql.connect('localhost','root','pn123456','web_API')
#         cursor = db.cursor(pymysql.cursors.DictCursor)
#         return db,cursor

#     def get(self):
#         db = pymysql.connect('localhost','root','pn123456','web_API')
#         cursor = db.cursor(pymysql.cursors.DictCursor)
#         sql = """ Select * From web_API.covid19_activity where COUNTRY_SHORT_NAME = 'Taiwan' """

#         cursor.execute(sql)
#         All = cursor.fetchall()
#         db.close()
#         response={
#             'data' : All
#         }
#         return jsonify(response)
        
# class Death(Resource):

#     def db_init(self):
#         db = pymysql.connect('localhost','root','pn123456','web_API')
#         cursor = db.cursor(pymysql.cursors.DictCursor)
#         return db,cursor    
#     def get(self):
#         db = pymysql.connect('localhost','root','pn123456','web_API')
#         cursor = db.cursor(pymysql.cursors.DictCursor)
        
#         sql = """ Select * From web_API.covid19_activity
#                     where PEOPLE_DEATH_COUNT > 5000
#             """
#         cursor.execute(sql)
#         One = cursor.fetchall()
#         db.close()
#         response={
#             'data':people_death_count
#         }
#         return jsonify(response)

        