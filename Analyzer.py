import cv2 as cv
import numpy as np
import math

def get_slope(line):
    return (line[1]-line[3])/(line[0]-line[2])

def get_yintercept(line):
    return line[1] - get_slope(line)*line[0]

def myround(x, base=5):
    return base * round(x/base)

class Analyzer():

    def __init__(self):
        self._image = None
        self._image_gray = None
        self._corners = np.array(list())
        self._suduts = []
        self._vertices = np.array(list())
        self._facts = []

    def _reset(self):
        self.__init__()

    def _read_file(self,file):
        self._image = cv.imread(file)
        self._image_gray = cv.cvtColor(self._image, cv.COLOR_BGR2GRAY)

    def _detect_corner(self):
        self._corners = np.array(list())
        self._vertices = np.array(list())
        if(True):
            ret,thresh = cv.threshold(self._image_gray,150,255,cv.THRESH_BINARY)
            contours, hierarchy = cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)

            contour = contours[0]
            size = cv.contourArea(contour)
            rect = cv.minAreaRect(contour)

            peri = cv.arcLength(contour, True)
            self._corners = cv.approxPolyDP(contour, 0.001 * peri, True)
            self._image = cv.drawContours(self._image, [self._corners], 0, (0,255,0), 3)
            

    def _find_vertices(self):
        for i in range(0,self._corners.shape[0]):
            v = self._corners[i] - self._corners[(i+1)%self._corners.shape[0]]

            magV = np.linalg.norm(v[0])

            self._vertices = np.append(self._vertices,magV)

    def _find_suduts(self):
        # Apply edge detection method on the image 
        edges = cv.Canny(self._image_gray,50,150,apertureSize = 3) 
        
        # This returns an array of r and theta values 
        lines = cv.HoughLines(edges,1,np.pi/180, 50) 

        line_abridged = []
        line_coordinates = []

        for line in lines:
            # The below for loop runs till r and theta values  
            # are in the range of the 2d array 
            for r,theta in line: 
                
                # Stores the value of cos(theta) in a 
                a = np.cos(theta) 
            
                # Stores the value of sin(theta) in b 
                b = np.sin(theta) 
                
                # x0 stores the value rcos(theta) 
                x0 = a*r 
                
                # y0 stores the value rsin(theta) 
                y0 = b*r 
                
                # x1 stores the rounded off value of (rcos(theta)-1000sin(theta)) 
                x1 = int(x0 + 1000*(-b)) 
                
                # y1 stores the rounded off value of (rsin(theta)+1000cos(theta)) 
                y1 = int(y0 + 1000*(a)) 
            
                # x2 stores the rounded off value of (rcos(theta)+1000sin(theta)) 
                x2 = int(x0 - 1000*(-b)) 
                
                # y2 stores the rounded off value of (rsin(theta)-1000cos(theta)) 
                y2 = int(y0 - 1000*(a)) 
                
                # cv2.line draws a line in img from the point(x1,y1) to (x2,y2). 
                # (0,0,255) denotes the colour of the line to be  
                #drawn. In this case, it is red.  
                # cv2.line(blank_img,(x1,y1), (x2,y2), (0,0,0),2)
                line_coordinates.append([x1,y1,x2,y2,theta])

        line_abridged = line_coordinates.copy()
        i = 0
        while (i < len(line_abridged)-1):
            j = i + 1
            while (j < len(line_abridged)):
                if ((abs(np.sin(line_abridged[i][4]) - np.sin(line_abridged[j][4])) < 0.2) or (abs(np.sin(line_abridged[i][4]) - np.sin(line_abridged[j][4])) > 1.8)) and ((abs(np.cos(line_abridged[i][4]) - np.cos(line_abridged[j][4])) < 0.2)) or (abs(np.cos(line_abridged[i][4]) - np.cos(line_abridged[j][4])) > 1.8):
                    if abs(line_abridged[i][0] - line_abridged[i][2]) > 100:
                        if abs(get_yintercept(line_abridged[i]) - get_yintercept(line_abridged[j])) < 100:
                    #if ((abs(line_abridged[i][0]-line_abridged[j][0])<10) and (abs(line_abridged[i][2]-line_abridged[j][2])<10)) or ((abs(line_abridged[i][1]-line_abridged[j][1])<10) and (abs(line_abridged[i][4]-line_abridged[j][4])<10)):
                            line_abridged.pop(j)
                        else:
                            j += 1
                    else:
                        if (abs(line_abridged[i][1]-line_abridged[j][1]) < 100) or (abs(line_abridged[i][3]-line_abridged[j][3]) < 100):
                            line_abridged.pop(j)
                        else:
                            j += 1
                else:
                    j += 1
            i += 1

        angles = []

        i = 0
        while i < len(line_abridged) -1:
            j = i + 1
            while j < len(line_abridged):
                if not(((abs(np.sin(line_abridged[i][4]) - np.sin(line_abridged[j][4])) < 0.2) or (abs(np.sin(line_abridged[i][4]) - np.sin(line_abridged[j][4])) > 1.8)) and ((abs(np.cos(line_abridged[i][4]) - np.cos(line_abridged[j][4])) < 0.2)) or (abs(np.cos(line_abridged[i][4]) - np.cos(line_abridged[j][4])) > 1.8)):
                    angles.append(np.degrees(line_abridged[i][4]) - np.degrees(line_abridged[j][4]))
                j += 1
            i += 1

        angles = list(map(int, angles))
        for i, angle in enumerate(angles):
            if(abs(angle) > 180):
                angles[i] = 360 - abs(myround(angle))
            else:
                angles[i] = abs(myround(angle))

        self._suduts = angles

    def _get_corners(self):
        return self._corners

    def _get_image(self):
        return self._image
    
    def _show_image(self):
        print(self._corners)
        print(self._suduts)
        print(self._vertices)
        cv.imshow('image', self._image)
        cv.waitKey(0)
        cv.destroyAllWindows

    def _get_facts(self):
        return self._facts

    def _extract_fact(self):

        self._facts = []
        # Jumlah Sudut
        self._facts.append("(jumlahsudut " + str(len(self._suduts)) + ")")

        # Jumlah Sudut Sama,Jumlah siku, Jumlah Tumpul, Jumlah Lancip
        jumlah_sudut_sama_terbanyak = 0
        jumlah_sudut_sama = 0
        jumlah_siku = 0
        jumlah_tumpul = 0
        jumlah_lancip = 0
        for sudut in self._suduts:
            jumlah_sudut_sama = 0
            for x in self._suduts:
                if x == sudut:
                    jumlah_sudut_sama = jumlah_sudut_sama + 1
            
            if jumlah_sudut_sama_terbanyak < jumlah_sudut_sama:
                jumlah_sudut_sama_terbanyak = jumlah_sudut_sama

            if sudut == 90:
                jumlah_siku = jumlah_siku + 1
            elif sudut < 90:
                jumlah_lancip = jumlah_lancip + 1
            else :
                jumlah_tumpul = jumlah_tumpul + 1
        
        self._facts.append("(jumlahsudutsama " + str(jumlah_sudut_sama_terbanyak) + ")")
        self._facts.append("(jumlahsudutsiku " + str(jumlah_siku) + ")")
        self._facts.append("(jumlahsudutlancip " + str(jumlah_lancip) + ")")
        self._facts.append("(jumlahsuduttumpul " + str(jumlah_tumpul) + ")")

        # Jumlah Sisi Sama
        jumlah_sisi_sama = 0
        jumlah_sisi_sama_terbanyak = 0
        for sudut in self._suduts:
            jumlah_sisi_sama = 0
            for x in self._suduts:
                if x == sudut:
                    jumlah_sisi_sama = jumlah_sisi_sama + 1
            
            if jumlah_sisi_sama_terbanyak < jumlah_sisi_sama:
                jumlah_sisi_sama_terbanyak = jumlah_sisi_sama
        
        self._facts.append("(jumlahsisisama " + str(jumlah_sisi_sama_terbanyak) + ")")

        print(self._facts)
        return self._facts