import cv2
import numpy as np

#url = "https://www.bing.com/images/search?view=detailV2&ccid=eLytJ6nr&id=A3EDC93142FB65A02BAE2D576E964456E857B40B&thid=OIP.eLytJ6nr2GdWI3wPTmdcZgHaEo&mediaurl=http%3a%2f%2fwww.hqwalls.com%2fwp-content%2fuploads%2f2012%2f08%2fBing_wallpapers_China-7.jpg&exph=1200&expw=1920&q=bing+walls&simid=608036344935154266&selectedIndex=1&ajaxhist=0"
from urllib.request import urlopen

def do_wallpaper():
        with urlopen("http://s0.geograph.org.uk/photos/40/57/405725_b17937da.jpg") as conn:
            imgarr =np.array(bytearray(conn.read()),dtype=np.uint8)
            img = cv2.imdecode(imgarr,-1)
            cv2.imshow('Wallpaper of the day',img)
            print('Wallpaper is printed on cv2 window')
            cv2.waitKey()
            cv2.destroyAllWindows()

