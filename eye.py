from  picamera import PiCamera
from time import sleep
from datetime import datetime

#camera=PiCamera()
sleep(10)
x=0
while True:    
    try:
        camera=PiCamera() 
        camera.capture('/var/www/html/image.jpg')
        camera.close()
        sleep(20)
        time_lapse=True
        if time_lapse==True:
            x=x+1
#            how_long =3
            how_long=4320
            if x%how_long ==0:
                
                try:
                    time=str(datetime.now())
                    camera=PiCamera()
                    file_name="/var/www/html/time_lapse/image" + time+".jpg"
                    camera.capture(file_name)
                    camera.close()
                    print('image for time lapse was saved')
		    
                    with open('/var/www/html/time_lapse/list.csv', 'a') as f:
                        file_name="image" + time +".jpg"+"\n"
                        f.write(file_name)                   
 #sleep(0)
                except Exception as e:
                    camera.close()
                    print("Error taking picture for time lapse: ",str(e))
            
    except Exception as e:
        camera.close()
        print("Error taking picture: ",str(e))
        sleep(60)
    
        #from  picamera import PiCamera

