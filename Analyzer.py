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
        self._angle = np.array(list())
        self._vertices = np.array(list())
        self._facts = []

    def _reset(self):
        self.__init__()

    def _read_file(self,file):
        self._image = cv.imread(file)
        self._image_gray = cv.cvtColor(self._image, cv.COLOR_BGR2GRAY)

    def _calculate_angle(self):
        # Calculate Angle
        for i in range(0,self._corners.shape[0]):
            print("i= " + str(i))
            vectorA = self._corners[i] - self._corners[(i-1)%self._corners.shape[0]]
            # print("self._corners.shape[0]")
            # print(self._corners.shape[0])
            # print("self._corners[(i-1) mod self._corners.shape[0]]")
            # print(self._corners[(i-1)%self._corners.shape[0]])
            # print("vectorA")
            # print(vectorA)
            # print("vectorA type")
            # print(type(vectorA))
            vectorB = self._corners[i] - self._corners[(i+1)%self._corners.shape[0]]
            # print("self._corners.shape[0]")
            # print(self._corners.shape[0])
            # print("self._corners[(i+1) mod self._corners.shape[0]]")
            # print(self._corners[(i+1)%self._corners.shape[0]])
            # print("vB")
            # print(vectorB)
            # print("vectorB type")
            # print(type(vectorB))
            dotProduct_vectorA_vectorB = vectorA[0].dot(vectorB[0])

            vectorA_magnitude = np.linalg.norm(vectorA[0])
            vectorB_magnitude = np.linalg.norm(vectorB[0])
            
            # angle = arccos(dot(A,B) / (|A|* |B|))
            angle = math.degrees(np.arccos(dotProduct_vectorA_vectorB/(vectorA_magnitude*vectorB_magnitude)))
            self._angle = np.append(self._angle, angle)
        
        # print(self._angle)

    def _detect_sudut(self):
        self._corners = np.array(list())
        self._angle = np.array(list())
        self._vertices = np.array(list())
        if(True):
            ret,thresh = cv.threshold(self._image_gray,150,255,cv.THRESH_BINARY)
            contours, hierarchy = cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE) 
            print(contours)

            contour = contours[0]
            size = cv.contourArea(contour)
            rect = cv.minAreaRect(contour)

            peri = cv.arcLength(contour, True)
            self._corners = cv.approxPolyDP(contour, 0.002 * peri, True) 
            print(self._corners)
            self._image = cv.drawContours(self._image, [self._corners], 0, (0,255,0), 3)
            
            self._calculate_angle()

    def _find_simpul(self):
        for i in range(0,self._corners.shape[0]):
            v = self._corners[i] - self._corners[(i+1)%self._corners.shape[0]]

            magV = np.linalg.norm(v[0])

            self._vertices = np.append(self._vertices,magV)

    def _get_corners(self):
        return self._corners
    
    def _get_angles(self):
        return self._angle

    def _get_image(self):
        return self._image
    
    def _show_image(self):
        print(self._corners)
        print(self._angle)
        print(self._vertices)
        cv.imshow('image', self._image)
        cv.waitKey(0)
        cv.destroyAllWindows

    def _get_facts(self):
        return self._facts

    def _extract_fact(self):

        self._facts = []
        # Jumlah Sudut
        self._facts.append("(jumlahsudut " + str(len(self._corners)) + ")")

        # Jumlah Sudut Sama,Jumlah siku, Jumlah Tumpul, Jumlah Lancip
        jumlah_sudut_sama_terbanyak = 0
        jumlah_sudut_sama = 0
        jumlah_siku = 0
        jumlah_tumpul = 0
        jumlah_lancip = 0
        for sudut in self._angle:
            jumlah_sudut_sama = 0
            for x in self._angle:
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
        for sisi in self._vertices:
            jumlah_sisi_sama = 0
            for x in self._vertices:
                if x == sisi:
                    jumlah_sisi_sama = jumlah_sisi_sama + 1
            
            if jumlah_sisi_sama_terbanyak < jumlah_sisi_sama:
                jumlah_sisi_sama_terbanyak = jumlah_sisi_sama
        
        self._facts.append("(jumlahsisisama " + str(jumlah_sisi_sama_terbanyak) + ")")

        print(self._facts)
        return self._facts