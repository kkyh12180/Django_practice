import pymysql
import re
from django.shortcuts import render
from django.db import connection
import base64
from io import BytesIO

# Create your views here.

def show_image_posts(request) :
    image_post_list = []
    try :
        cursor = connection.cursor()
        post_list_sql = "SELECT ImgPostID, Thumbnail_image from Image_Post order by Post_time asc;"
        cursor.execute(post_list_sql)
        image_post_list = [list(item) for item in cursor.fetchmany(size=10)]
        
        for i in range (0, len(image_post_list)):
            image_post_list[i][1] = image_post_list[i][1].decode("UTF-8")

    except Exception as e:
        print(e)
        connection.rollback()
        print("Failed selecting in Image_Post")
    
    return render(request, 'image_post_app/image_post_list.html', context={'image_post_list': image_post_list})

def show_image_content(request, IPID) :
    ipid = {
        'ImgPostID' : IPID,
    }

    image_id_list = []
    image_list = []
    try :
        cursor = connection.cursor()
        image_list_sql = f'SELECT ImgID FROM Image_In_Post WHERE ImgPostID="{IPID}"'
        cursor.execute(image_list_sql)
        image_id_list = cursor.fetchall()

        # print(image_id_list)

        for image_id in image_id_list :
            image_sql = f'SELECT * FROM Image_Table WHERE ImgID="{image_id[0]}"'
            cursor.execute(image_sql)
            image = list(cursor.fetchone())
            # print(image)
            image[2] = image[2].decode("UTF-8")
            image_list.append(image)

    except Exception as e:
        print(e)
        connection.rollback()

    return render(request, 'image_post_app/image_post_content.html', context={'IPID':ipid, 'image_list': image_list})