import urllib2

import urllib
import imutils
import time
from imutils import paths
import json 
from io import BytesIO
#import paths
#from PIL import Image, ImageDraw
#from scipy.spatial import distance
import dlib
#import matplotlib.pyplot as plt
import cv2
import argparse

file1 = open("labels_ibug_300W_train_eyes.xml", "a")
detect = dlib.get_frontal_face_detector()

# passing the arguements
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--images", type=str, required=True,
	help="path to input directory of images to stitch")
args = vars(ap.parse_args())

# grab the paths to the input images and initialize our images list
print("[INFO] loading images...")
imagePaths = sorted(list(paths.list_images(args["images"])))
images = []


def draw_face(filepath, rectangle):


    http_url = 'https://api-us.faceplusplus.com/facepp/v3/detect'

    key = "zCJBuhRTzYk1NhLthHdbXY2ykdPeRjlD"

    secret = "u9DeE1zyP-Gq68Wt88cVVtHnTu048ccH"




    boundary = '----------%s' % hex(int(time.time() * 1000))

    data = []

    data.append('--%s' % boundary)

    data.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_key')

    data.append(key)



    data.append('--%s' % boundary)

    data.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_secret')

    data.append(secret)

    data.append('--%s' % boundary)

    data.append('Content-Disposition: form-data; name="%s"\r\n' % 'return_landmark')

    data.append('1')

    data.append('--%s' % boundary)



    fr=open(filepath,'rb')

    data.append('Content-Disposition: form-data; name="%s"; filename="co33.jpg"' % 'image_file')

    data.append('Content-Type: %s\r\n' % 'application/octet-stream')

    data.append(fr.read())

    fr.close()

    data.append('--%s--\r\n' % boundary)



    http_body='\r\n'.join(data)

    #print(http_body)

    #buld http request

    req=urllib2.Request(http_url)

    #header

    req.add_header('Content-Type', 'multipart/form-data; boundary=%s' % boundary)

    req.add_data(http_body)
    #print(faces)

    try:

	#post data to server

        resp = urllib2.urlopen(req, timeout=5)

	#get response
        qrcont=resp.read()
        #print(qrcont)
        res = json.loads(qrcont)
        a= (res["faces"][0])
        file1.write("  <image file='"+filepath+"'>\n")
        file1.write("    <box top='"+str(rectangle.top())+"' left='"+str(rectangle.left())+"' width='"+str(rectangle.right()-rectangle.left())+"' height='"+str(rectangle.bottom()-rectangle.top())+"'>\n")
        file1.write("      <part name='1' x='"+str(int(a['landmark']['mouth_upper_lip_left_contour2']['x']))+"' y='"+str(int(a['landmark']['mouth_upper_lip_left_contour2']['y']))+"'/>\n")
        file1.write("      <part name='2' x='"+str(int(a['landmark']['contour_chin']['x']))+"' y='"+str(int(a['landmark']['contour_chin']['y']))+"'/>\n")
        file1.write("      <part name='3' x='"+str(int(a['landmark']['mouth_lower_lip_right_contour3']['x']))+"' y='"+str(int(a['landmark']['mouth_lower_lip_right_contour3']['y']))+"'/>\n")
        file1.write("      <part name='4' x='"+str(int(a['landmark']['contour_right9']['x']))+"' y='"+str(int(a['landmark']['contour_right9']['y']))+"'/>\n")
        file1.write("      <part name='5' x='"+str(int(a['landmark']['mouth_upper_lip_left_contour1']['x']))+"' y='"+str(int(a['landmark']['mouth_upper_lip_left_contour1']['y']))+"'/>\n")
        file1.write("      <part name='6' x='"+str(int(a['landmark']['right_eyebrow_lower_middle']['x']))+"' y='"+str(int(a['landmark']['right_eyebrow_lower_middle']['y']))+"'/>\n")
        file1.write("      <part name='7' x='"+str(int(a['landmark']['left_eyebrow_lower_middle']['x']))+"' y='"+str(int(a['landmark']['left_eyebrow_lower_middle']['y']))+"'/>\n")
        file1.write("      <part name='8' x='"+str(int(a['landmark']['mouth_upper_lip_left_contour3']['x']))+"' y='"+str(int(a['landmark']['mouth_upper_lip_left_contour3']['y']))+"'/>\n")
        file1.write("      <part name='9' x='"+str(int(a['landmark']['left_eyebrow_lower_left_quarter']['x']))+"' y='"+str(int(a['landmark']['left_eyebrow_lower_left_quarter']['y']))+"'/>\n")
        file1.write("      <part name='10' x='"+str(int(a['landmark']['right_eyebrow_lower_left_quarter']['x']))+"' y='"+str(int(a['landmark']['right_eyebrow_lower_left_quarter']['y']))+"'/>\n")
        file1.write("      <part name='11' x='"+str(int(a['landmark']['right_eyebrow_lower_right_quarter']['x']))+"' y='"+str(int(a['landmark']['right_eyebrow_lower_right_quarter']['y']))+"'/>\n") 
        file1.write("      <part name='12' x='"+str(int(a['landmark']['nose_contour_left1']['x']))+"' y='"+str(int(a['landmark']['nose_contour_left1']['y']))+"'/>\n")
        file1.write("      <part name='13' x='"+str(int(a['landmark']['left_eyebrow_upper_left_quarter']['x']))+"' y='"+str(int(a['landmark']['left_eyebrow_upper_left_quarter']['y']))+"'/>\n")
        file1.write("      <part name='14' x='"+str(int(a['landmark']['mouth_lower_lip_bottom']['x']))+"' y='"+str(int(a['landmark']['mouth_lower_lip_bottom']['y']))+"'/>\n")
        file1.write("      <part name='15' x='"+str(int(a['landmark']['contour_right7']['x']))+"' y='"+str(int(a['landmark']['contour_right7']['y']))+"'/>\n")
        file1.write("      <part name='16' x='"+str(int(a['landmark']['left_eyebrow_left_corner']['x']))+"' y='"+str(int(a['landmark']['left_eyebrow_left_corner']['y']))+"'/>\n")
        file1.write("      <part name='17' x='"+str(int(a['landmark']['contour_right6']['x']))+"' y='"+str(int(a['landmark']['contour_right6']['y']))+"'/>\n")
        file1.write("      <part name='18' x='"+str(int(a['landmark']['contour_left7']['x']))+"' y='"+str(int(a['landmark']['contour_left7']['y']))+"'/>\n")
        file1.write("      <part name='19' x='"+str(int(a['landmark']['contour_left6']['x']))+"' y='"+str(int(a['landmark']['contour_left6']['y']))+"'/>\n")
        file1.write("      <part name='20' x='"+str(int(a['landmark']['contour_left5']['x']))+"' y='"+str(int(a['landmark']['contour_left5']['y']))+"'/>\n")
        file1.write("      <part name='21' x='"+str(int(a['landmark']['contour_left4']['x']))+"' y='"+str(int(a['landmark']['contour_left4']['y']))+"'/>\n")
        file1.write("      <part name='22' x='"+str(int(a['landmark']['contour_left3']['x']))+"' y='"+str(int(a['landmark']['contour_left3']['y']))+"'/>\n")
        file1.write("      <part name='23' x='"+str(int(a['landmark']['contour_left2']['x']))+"' y='"+str(int(a['landmark']['contour_left2']['y']))+"'/>\n")
        file1.write("      <part name='24' x='"+str(int(a['landmark']['contour_left1']['x']))+"' y='"+str(int(a['landmark']['contour_left1']['y']))+"'/>\n")
        file1.write("      <part name='25' x='"+str(int(a['landmark']['contour_right1']['x']))+"' y='"+str(int(a['landmark']['contour_right1']['y']))+"'/>\n")
        file1.write("      <part name='26' x='"+str(int(a['landmark']['contour_right2']['x']))+"' y='"+str(int(a['landmark']['contour_right2']['y']))+"'/>\n")
        file1.write("      <part name='27' x='"+str(int(a['landmark']['contour_right3']['x']))+"' y='"+str(int(a['landmark']['contour_right3']['y']))+"'/>\n")
        file1.write("      <part name='28' x='"+str(int(a['landmark']['contour_right4']['x']))+"' y='"+str(int(a['landmark']['contour_right4']['y']))+"'/>\n")
        file1.write("      <part name='29' x='"+str(int(a['landmark']['contour_right5']['x']))+"' y='"+str(int(a['landmark']['contour_right5']['y']))+"'/>\n")
        file1.write("      <part name='30' x='"+str(int(a['landmark']['contour_left9']['x']))+"' y='"+str(int(a['landmark']['contour_left9']['y']))+"'/>\n")
        file1.write("      <part name='31' x='"+str(int(a['landmark']['contour_left8']['x']))+"' y='"+str(int(a['landmark']['contour_left8']['y']))+"'/>\n")
        file1.write("      <part name='32' x='"+str(int(a['landmark']['nose_right']['x']))+"' y='"+str(int(a['landmark']['nose_right']['y']))+"'/>\n")
        file1.write("      <part name='33' x='"+str(int(a['landmark']['nose_contour_right3']['x']))+"' y='"+str(int(a['landmark']['nose_contour_right3']['y']))+"'/>\n")
        file1.write("      <part name='34' x='"+str(int(a['landmark']['nose_contour_lower_middle']['x']))+"' y='"+str(int(a['landmark']['nose_contour_lower_middle']['y']))+"'/>\n")
        file1.write("      <part name='35' x='"+str(int(a['landmark']['mouth_upper_lip_right_contour1']['x']))+"' y='"+str(int(a['landmark']['mouth_upper_lip_right_contour1']['y']))+"'/>\n")
        file1.write("      <part name='36' x='"+str(int(a['landmark']['mouth_upper_lip_right_contour2']['x']))+"' y='"+str(int(a['landmark']['mouth_upper_lip_right_contour2']['y']))+"'/>\n")
        file1.write("      <part name='37' x='"+str(int(a['landmark']['mouth_upper_lip_right_contour3']['x']))+"' y='"+str(int(a['landmark']['mouth_upper_lip_right_contour3']['y']))+"'/>\n")
        file1.write("      <part name='38' x='"+str(int(a['landmark']['mouth_right_corner']['x']))+"' y='"+str(int(a['landmark']['mouth_right_corner']['y']))+"'/>\n")
        file1.write("      <part name='39' x='"+str(int(a['landmark']['mouth_lower_lip_right_contour1']['x']))+"' y='"+str(int(a['landmark']['mouth_lower_lip_right_contour1']['y']))+"'/>\n")
        file1.write("      <part name='40' x='"+str(int(a['landmark']['contour_right8']['x']))+"' y='"+str(int(a['landmark']['contour_right8']['y']))+"'/>\n")
        file1.write("      <part name='41' x='"+str(int(a['landmark']['left_eyebrow_right_corner']['x']))+"' y='"+str(int(a['landmark']['left_eyebrow_right_corner']['y']))+"'/>\n")
        file1.write("      <part name='42' x='"+str(int(a['landmark']['mouth_upper_lip_top']['x']))+"' y='"+str(int(a['landmark']['mouth_upper_lip_top']['y']))+"'/>\n")
        file1.write("      <part name='43' x='"+str(int(a['landmark']['nose_left']['x']))+"' y='"+str(int(a['landmark']['nose_left']['y']))+"'/>\n")
        file1.write("      <part name='44' x='"+str(int(a['landmark']['mouth_lower_lip_top']['x']))+"' y='"+str(int(a['landmark']['mouth_lower_lip_top']['y']))+"'/>\n")
        file1.write("      <part name='45' x='"+str(int(a['landmark']['right_eyebrow_right_corner']['x']))+"' y='"+str(int(a['landmark']['right_eyebrow_right_corner']['y']))+"'/>\n")
        file1.write("      <part name='46' x='"+str(int(a['landmark']['mouth_lower_lip_left_contour1']['x']))+"' y='"+str(int(a['landmark']['mouth_lower_lip_left_contour1']['y']))+"'/>\n")
        file1.write("      <part name='47' x='"+str(int(a['landmark']['mouth_left_corner']['x']))+"' y='"+str(int(a['landmark']['mouth_left_corner']['y']))+"'/>\n")
        file1.write("      <part name='48' x='"+str(int(a['landmark']['right_eyebrow_upper_left_quarter']['x']))+"' y='"+str(int(a['landmark']['right_eyebrow_upper_left_quarter']['y']))+"'/>\n")
        file1.write("      <part name='49' x='"+str(int(a['landmark']['nose_tip']['x']))+"' y='"+str(int(a['landmark']['nose_tip']['y']))+"'/>\n")
        file1.write("      <part name='50' x='"+str(int(a['landmark']['left_eyebrow_upper_middle']['x']))+"' y='"+str(int(a['landmark']['left_eyebrow_upper_middle']['y']))+"'/>\n")
        file1.write("      <part name='51' x='"+str(int(a['landmark']['mouth_lower_lip_right_contour2']['x']))+"' y='"+str(int(a['landmark']['mouth_lower_lip_right_contour2']['y']))+"'/>\n")
        file1.write("      <part name='52' x='"+str(int(a['landmark']['mouth_lower_lip_left_contour3']['x']))+"' y='"+str(int(a['landmark']['mouth_lower_lip_left_contour3']['y']))+"'/>\n")
        file1.write("      <part name='53' x='"+str(int(a['landmark']['nose_contour_left2']['x']))+"' y='"+str(int(a['landmark']['nose_contour_left2']['y']))+"'/>\n")
        file1.write("      <part name='54' x='"+str(int(a['landmark']['nose_contour_left3']['x']))+"' y='"+str(int(a['landmark']['nose_contour_left3']['y']))+"'/>\n")
        file1.write("      <part name='55' x='"+str(int(a['landmark']['nose_contour_right1']['x']))+"' y='"+str(int(a['landmark']['nose_contour_right1']['y']))+"'/>\n")
        file1.write("      <part name='56' x='"+str(int(a['landmark']['nose_contour_right2']['x']))+"' y='"+str(int(a['landmark']['nose_contour_right2']['y']))+"'/>\n")
        file1.write("      <part name='57' x='"+str(int(a['landmark']['mouth_lower_lip_left_contour2']['x']))+"' y='"+str(int(a['landmark']['mouth_lower_lip_left_contour2']['y']))+"'/>\n")
        file1.write("      <part name='58' x='"+str(int(a['landmark']['mouth_lower_lip_left_contour2']['x']))+"' y='"+str(int(a['landmark']['mouth_lower_lip_left_contour2']['y']))+"'/>\n")
        file1.write("      <part name='59' x='"+str(int(a['landmark']['right_eyebrow_upper_right_quarter']['x']))+"' y='"+str(int(a['landmark']['right_eyebrow_upper_right_quarter']['y']))+"'/>\n")
        file1.write("      <part name='60' x='"+str(int(a['landmark']['right_eyebrow_upper_middle']['x']))+"' y='"+str(int(a['landmark']['right_eyebrow_upper_middle']['y']))+"'/>\n")
        file1.write("      <part name='61' x='"+str(int(a['landmark']['left_eyebrow_lower_right_quarter']['x']))+"' y='"+str(int(a['landmark']['left_eyebrow_lower_right_quarter']['y']))+"'/>\n")
        file1.write("      <part name='62' x='"+str(int(a['landmark']['left_eyebrow_upper_right_quarter']['x']))+"' y='"+str(int(a['landmark']['left_eyebrow_upper_right_quarter']['y']))+"'/>\n")
        file1.write("      <part name='63' x='"+str(int(a['landmark']['mouth_upper_lip_bottom']['x']))+"' y='"+str(int(a['landmark']['mouth_upper_lip_bottom']['y']))+"'/>\n")
        file1.write("      <part name='64' x='"+str(int(a['landmark']['left_eye_left_corner']['x']))+"' y='"+str(int(a['landmark']['left_eye_left_corner']['y']))+"'/>\n")
        file1.write("      <part name='65' x='"+str(int(a['landmark']['left_eye_upper_left_quarter']['x']))+"' y='"+str(int(a['landmark']['left_eye_upper_left_quarter']['y']))+"'/>\n")
        file1.write("      <part name='66' x='"+str(int(a['landmark']['left_eye_top']['x']))+"' y='"+str(int(a['landmark']['left_eye_top']['y']))+"'/>\n")
        file1.write("      <part name='67' x='"+str(int(a['landmark']['left_eye_upper_right_quarter']['x']))+"' y='"+str(int(a['landmark']['left_eye_upper_right_quarter']['y']))+"'/>\n")
        file1.write("      <part name='68' x='"+str(int(a['landmark']['left_eye_right_corner']['x']))+"' y='"+str(int(a['landmark']['left_eye_right_corner']['y']))+"'/>\n")
        file1.write("      <part name='69' x='"+str(int(a['landmark']['left_eye_lower_right_quarter']['x']))+"' y='"+str(int(a['landmark']['left_eye_lower_right_quarter']['y']))+"'/>\n")
        file1.write("      <part name='70' x='"+str(int(a['landmark']['left_eye_bottom']['x']))+"' y='"+str(int(a['landmark']['left_eye_bottom']['y']))+"'/>\n")
        file1.write("      <part name='71' x='"+str(int(a['landmark']['left_eye_lower_left_quarter']['x']))+"' y='"+str(int(a['landmark']['left_eye_lower_left_quarter']['y']))+"'/>\n")
        file1.write("      <part name='72' x='"+str(int(a['landmark']['left_eye_center']['x']))+"' y='"+str(int(a['landmark']['left_eye_center']['y']))+"'/>\n")
        file1.write("      <part name='73' x='"+str(int(a['landmark']['left_eye_pupil']['x']))+"' y='"+str(int(a['landmark']['left_eye_pupil']['y']))+"'/>\n")
        file1.write("      <part name='74' x='"+str(int(a['landmark']['right_eye_left_corner']['x']))+"' y='"+str(int(a['landmark']['right_eye_left_corner']['y']))+"'/>\n")
        file1.write("      <part name='75' x='"+str(int(a['landmark']['right_eye_upper_left_quarter']['x']))+"' y='"+str(int(a['landmark']['right_eye_upper_left_quarter']['y']))+"'/>\n")
        file1.write("      <part name='76' x='"+str(int(a['landmark']['right_eye_top']['x']))+"' y='"+str(int(a['landmark']['right_eye_top']['y']))+"'/>\n")
        file1.write("      <part name='77' x='"+str(int(a['landmark']['right_eye_upper_right_quarter']['x']))+"' y='"+str(int(a['landmark']['right_eye_upper_right_quarter']['y']))+"'/>\n")
        file1.write("      <part name='78' x='"+str(int(a['landmark']['right_eye_right_corner']['x']))+"' y='"+str(int(a['landmark']['right_eye_right_corner']['y']))+"'/>\n")
        file1.write("      <part name='79' x='"+str(int(a['landmark']['right_eye_lower_right_quarter']['x']))+"' y='"+str(int(a['landmark']['right_eye_lower_right_quarter']['y']))+"'/>\n")
        file1.write("      <part name='80' x='"+str(int(a['landmark']['right_eye_bottom']['x']))+"' y='"+str(int(a['landmark']['right_eye_bottom']['y']))+"'/>\n")
        file1.write("      <part name='81' x='"+str(int(a['landmark']['right_eye_lower_left_quarter']['x']))+"' y='"+str(int(a['landmark']['right_eye_lower_left_quarter']['y']))+"'/>\n")
        file1.write("      <part name='82' x='"+str(int(a['landmark']['right_eye_center']['x']))+"' y='"+str(int(a['landmark']['right_eye_center']['y']))+"'/>\n")
        file1.write("      <part name='83' x='"+str(int(a['landmark']['right_eye_pupil']['x']))+"' y='"+str(int(a['landmark']['right_eye_pupil']['y']))+"'/>\n")
        file1.write("    </box>\n")
        file1.write("  </image>\n")

    except urllib2.HTTPError as e:

        print (e.read())

index = 0
key = 0
flag = 1

for image_path in imagePaths:

    '''if(index % 40 ==0 and index>1):
        time.sleep(60)
    if(index % 20 ==0 and index>1):
        temp = key
        key = flag
        flag = temp
    image_path = "set/image"+str(index)+".jpg"'''
    frame = cv2.imread(image_path)
    print(index)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    subjects = detect(gray, 0)

    for subject in subjects:
        image = draw_face(image_path,subject)
    index = index+1
    #image.show()

file1.write("</images>\n")
file1.write("</dataset>")
file1.close()
