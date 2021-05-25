from django.db import models
import cx_Oracle
# DAO
# Create your models here.
def getConnection():
    try:
        conn=cx_Oracle.connect("hr/happy@localhost:1521/xe")
    except Exception as e:
        print(e)
    return conn

def recipeListData(page):
    rowSize=12
    start=(rowSize*page)-(rowSize-1)
    end=(rowSize*page)
    #연결
    conn=getConnection()
    cursor=conn.cursor()
    sql=f"""
            SELECT no,title,poster,chef,num 
            FROM (SELECT no,title,poster,chef,rownum as num 
            FROM (SELECT /*+ INDEX_ASC(recipe recipe_no_pk) */ no,title,poster,chef
            FROM recipe))
            WHERE num BETWEEN {start} AND {end}
          """
    cursor.execute(sql)
    list=cursor.fetchall()
    print(list)
    cursor.close()
    conn.close()
    return list
'''
   NO          NOT NULL NUMBER         
RNO                  NUMBER         
POSTER      NOT NULL VARCHAR2(260)  
CHEF        NOT NULL VARCHAR2(200)  
CHEF_POSTER NOT NULL VARCHAR2(260)  
TITLE       NOT NULL VARCHAR2(2000) 
CONTENT     NOT NULL VARCHAR2(4000) 
INFO1       NOT NULL VARCHAR2(20)   
INFO2       NOT NULL VARCHAR2(20)   
INFO3       NOT NULL VARCHAR2(20)   
FOOD_MAKE   NOT NULL CLOB           
CHEF_INFO   NOT NULL VARCHAR2(1000)
'''
def recipeDetailData(rno):
    conn=getConnection()
    cursor=conn.cursor()
    sql=f"""
            SELECT no,poster,chef,chef_poster,title,content,info1,info2,info3,chef_info
            FROM recipe_make
            WHERE rno={rno}
          """
    cursor.execute(sql)

    detail=cursor.fetchone()

    cursor.close()
    conn.close()
    return detail

def recipeTotalPage():
    #데이터베이스 연결
    conn=getConnection()
    #cursor생성
    cursor=conn.cursor()
    # sql문장 제작
    sql="SELECT CEIL(COUNT(*)/12.0) FROM recipe"
    # 결과값 받기
    cursor.execute(sql)
    total=cursor.fetchone()
    print("totalPage:"+str(total[0]))
    # cursor,conn닫기
    cursor.close()
    conn.close()
    # 결과값 전송
    return total[0]

#recipeTotalPage()
#recipeListData(1)