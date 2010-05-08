# -*- coding: utf-8 -*-
import numpy as np
import re
from os.path import join as joinpath

# section example
sec_rectangular=[(0, 0), (0, -2), (10, -2), (10, 0)]
sec_rectangular2=sec_rectangular[1:]
sec_rectangular2=sec_rectangular.insert(-1, sec_rectangular[-1])
#print sec_rectangular
#print sec_rectangular2
rect=np.array(sec_rectangular)
rect2=np.array(sec_rectangular2)
rect_y=np.array([i[0] for i in sec_rectangular])
rect_z=np.array([i[1] for i in sec_rectangular])
#print rect,  rect2

import csv

class Section:
    """            print m.group('sez_name')
    It defines attributes and methods for a river cross-section.
    It's possible to define sub-segments of the section,
    each one with a different roughness.
    Example of usage:

    coord = [[0,10],[0,0],[10,0],[20,0],[20,10]]
    sect = Section(0, coord)
    sect.addSegment(sect.yzcoord[0:2], 35)
    sect.addSegment(sect.yzcoord[2:], 40)
    """
    def __init__(self, name=None, data=None,
                 first=0,  last=-1,  erodible=True,
                 roughness=None, discontinuity=False,
                 subsection=False, watersurface=None,
                 variotype = None,  d90=None,  variolenght=None, varioexcav=None):
        self.name = name
        self.data =  np.array(data)
        self.xcoord = self.data.T[0]
        self.yzcoord = self.data.T[1:3]
        self.first = first
        self.last = last
        minimum = self.yzcoord[1].argmin()
        self.min = self.yzcoord[minimum][1]

        self.erodible = erodible
        self.roughness = roughness
        self.discontinuity = discontinuity
        self.subsection = subsection
        self.segment = []

        # Add this attributs to support vario format
        self.d90 =d90
        self.variotype = variotype
        self.varioLenght = variolenght
        self.varioexcav = varioexcav

        self.watersurf = watersurface


    def __str__(self):
        return str(self.name)

    def addSegment(self, yzcoordSegm=None,
            roughness=None):
        self.segment.append(Section(yzcoord=yzcoordSegm, roughness=roughness, subsection=True))

    def firstPointAfter_h(self, points, h):
        """Return index of the first

        >>> points=np.array([ 742.73,  742.75,  742.77,  742.79,  747.27])

        >>> section.firstPointAfter_h(points, 745)
        4

        >>> section.firstPointAfter_h(points, 742)
        Traceback (innermost last):
          ...
        ValueError: h outside section
         h < min

        >>> section.firstPointAfter_h(points, 748)
        Traceback (innermost last):
          ...
        ValueError: h outside section
         h > max
        """
        if h > points.max():
            raise ValueError("h outside section\n h > max")
        elif h < points.min():
            raise ValueError("h outside section\n h < min")
        else:
            #print 'points:', points,  h
            for i, p in enumerate(points):
                #print i,  p
                if p > h:
                    return i

    def intersection(self, pn1, pn2, h):
        """Returnurn intersection between 2 points and height

            >>> section.intersection((0,5),(0,0),3)
            (0, 3)

        (h-y0)/(y1-y0) = (x-x0)/(x1-x0)
        x=(x1-x0)/(y1-y0)*(h-y0)+x0
        return x,h"""
        #print "intersectionection:", pn1, pn2, h
        #print "z: ", (pn2[0]-pn1[0])/(pn2[1]-pn1[1])*(h-pn1[1])+pn1[0]
        return (pn2[0]-pn1[0])/(pn2[1]-pn1[1])*(h-pn1[1])+pn1[0], h

    def getSect(self, h):
        """Return section only from left intersection to right intersection

            >>> section.getSect(745)
            array([[  4.71227679e-01,   7.45000000e+02],
                   [  9.30000000e-01,   7.42790000e+02],
                   [  7.19000000e+00,   7.42770000e+02],
                   [  1.25900000e+01,   7.42750000e+02],
                   [  1.80800000e+01,   7.42730000e+02],
                   [  1.89100000e+01,   7.42730000e+02],
                   [  1.94887253e+01,   7.45000000e+02]])

        """
        lefttomin=self.yzcoord[1][:self.min+1]
        # left point
        lpnt = self.firstPointAfter_h(lefttomin[::-1], h)
        # find index of left point
        l_pnt = self.min - lpnt
        # find left intersection
        l_intersect = self.intersection(self.yzcoord.T[l_pnt], self.yzcoord.T[l_pnt+1], h)
        # right point
        rpnt = self.firstPointAfter_h(self.yzcoord[1][self.min:], h)
        # find index of right point
        r_pnt = self.min + rpnt
        # find right intersection
        r_intersect = self.intersection(self.yzcoord.T[r_pnt], self.yzcoord.T[r_pnt-1], h)
        # make new section geometries
        sez = self.yzcoord.T[l_pnt+1:r_pnt]
        # Add left intersection on the top
        sez=np.insert(sez, [0,], l_intersect,axis=0)
        # Add rightht intersection on the bottom
        sez=np.append(sez,[r_intersect],axis=0)
        return sez

    def area(self, sez):
        """Return area given a section take from getSect

            >>> section.area(yzcoordT)
            41.448496630204318
        """
        # find area below water line
        area_h2o = (sez[-1][0]-sez[0][0])*sez[0][1]
        # find area bellow section
        area_sez = np.trapz(sez.T[1],x=sez.T[0])
        return area_h2o - area_sez

    def wetBorder(self,  sez):
        """Calculate web border from a given section

            >>> section.wetBorder(yzcoordT)
            23.557497620999964

        """
        # calculate with pitagora: sqrt(dx²+dy²)
        sez1=np.delete(sez, 0, axis=0)
        sez2=np.delete(sez, -1, axis=0)
        delta=sez1-sez2
        return np.sum(np.sqrt(delta * delta))

    def rh(self, h):
        """Return thee idraulic radius given height

            >>> section.rh(745)
            1.7594609288533762
        """
        sez=self.getSect(h)
        area=self.area(sez)
        wetborder = self.wetBorder(sez)
        return area/wetborder

class Reach:
    """
    It defines the geometric properties of a river reach.
    It is composed by sections and sections can be subdivided in
    segments.
    """
    def __init__(self,  sections = []):
        self.sections = sections
        self.workingpath = None

    def __str__(self):
        slist = []
        for s in self.sections:
            separetor = '='*50
            sectname = s.name + ': ' + str(len(s.yzcoord))
            data = str(s.data)
            slist.append("\n".join([separetor, sectname, data]))
        return "\n".join(slist)

    def recursiveReadVario(self, datalist):
        """This function append section to reach.sections"""
        index = 0
        # read first line section
        xcoord,e,d = datalist[index]
        xcoord = float(xcoord)
        erodible = True if e == 't' else False
        discontinuity= False if d == 'f' else True
        # go to the second line
        index+=1
        # read and trasform str value in integer
        npoints, nsegments = map(int, datalist[index])

        #initialize locals variables
        yzcoord = []
        segmens = []
        endpoints=index+npoints+1
        endsegments = endpoints+nsegments
        index+=1

        # start a cicle between points
        for e in datalist[index:endpoints]:
            # trasform string in float
            yz=map(float, e[:2])
            #print e[:2]
            # add new coordinates to yzcoordinates list
            yzcoord.append(yz)

        # add x column to the data array
        data = np.ones(shape=(len(yzcoord),1))
        data = data  * xcoord

        # transform list in a numpy array because in this way is easier
        # to assign value for ks
        yzcoord = np.array(yzcoord)
        #print yzcoord
        # add yzcoord to the data array
        data = np.append(data,yzcoord,axis=1)
        # add roughnes column default it is 0
        kscolumn = np.zeros(shape=(len(yzcoord),1))
        data = np.append(data,kscolumn,axis=1)

        # assign KS = 3 to have more readable source
        KS = 3
        for e in datalist[endpoints:endsegments]:
            # trasform string in integer and assign start end and ks
            start, end, ks = map(int, e)
            start -= 1
            data.T[KS][start:end] = ks

        index = endsegments

        # check if discontinuity == True
        if discontinuity:
            [[type], [d90], [l], [excavation]] = datalist[index:index+4]
            index = index + 4
            type, d90, l, excavation= int(type), int(d90), float(l), float(excavation)
            #print "type: %d, d90: %d, l: %f, excav: %f" % (type, d90, l, excavation)

        # make new section and append to the reach list
        self.sections.append(Section(data = data,
                                     erodible = erodible,
                                     discontinuity = discontinuity,
                                     variotype = None if discontinuity == False  else type,
                                     d90 = None if discontinuity == False  else d90,
                                     variolenght = None if discontinuity == False  else l,
                                     varioexcav = None if discontinuity == False  else excavation,))

        newline = datalist[index]
        # check if new line is the end of file.
        if newline == ['-100', '-100', '-100']:
            print "Finish to import."
        else:
            self.recursiveReadVario(datalist[index:])

    def importFileVario(self, filename):
        """
        >>> river = Reach()
        >>> river.importFileVario('../test/importexport/variosection.geo')
        Finish to import.
        """
        datalist = []
        geometryFile = open(filename, "r")
        # make a list of list from the file.
        for row in geometryFile:
            datalist.append(row.split())
        self.recursiveReadVario(datalist)


    def exportFileVario(self, filename):
        """
        Return a vario file of sections
        >>> river = Reach()
        >>> river.importFileVario('../test/importexport/variosection.geo')
        Finish to import.
        >>> river.exportFileVario('../test/importexport/variosectionTEST.geo')
        Finish to export.
        """
        sectionVarioFile = open(filename, "w")
        for s in self.sections:
            # Vario take just one x coordinates so we take the first one
            x = float(s.xcoord[0])
            erod = 't' if s.erodible else 'f'
            disc = 't' if s.discontinuity else 'f'
            npoints = int(len(s.data))
            kslist = s.data.T[3][:-1]
            segmentslist = []
            index = 0
            # initialize segment start and end
            s_start=0
            s_end =1
            while s_end != len(kslist):
                ks = kslist[s_start]
                ksnext = kslist[s_end]
                #print ks, ksnext,  s_start, s_end
                if ks == ksnext:
                    s_end += 1
                else:
                    segmentslist.append('%d %d %d' % (s_start+1, s_end+1, ks))
                    s_start = s_end
                    s_end += 1
            segmentslist.append('%d %d %d' % (s_start+1, s_end+1, kslist[s_start]))

            nsegments = int(len(segmentslist))
            #print s.yzcoord.T
            yzcoordstr = "\n".join(["%f %f" % tuple(c) for c in s.yzcoord.T])
            segmentstr = "\n".join(segmentslist)

            # Define the string that will be write in the file for each section
            variosection = """%f %s %s
%d %d
%s
%s
""" % (x, erod, disc,
                     npoints, nsegments,
                     yzcoordstr,
                     segmentstr, )
            # check if there are discontinuity
            if s.discontinuity:
                dis_str = "%d\n%d\n%f\n%f\n" % (s.variotype, s.d90, s.varioLenght, s.varioexcav)
                variosection +=dis_str

            # then write section string to the output file
            sectionVarioFile.write(variosection)
        sectionVarioFile.close()
        print "Finish to export."


    def importFileOri(self, sectionfilename, pointsfilename):
        """section.ori
        -------------------------
        301
        4  sez0001
        1  100.00000   4  100.00000
        4  sez0002
        1  100.00000   4  100.00000
        4  sez0003
        1  100.00000   4  100.00000

        points.ori
        -------------------------
        0.00000  10.00000 100.00000 100.00000
        0.00000  10.00000   0.00000 100.00000
        0.00000  50.00000   0.00000 100.00000
        0.00000  50.00000 100.00000 100.00000
        5.00000  10.00000 100.00000 100.00000
        5.00000  10.00000   0.00000 100.00000
        5.00000  50.00000   0.00000 100.00000
        5.00000  50.00000 100.00000 100.00000

        >>> river = Reach()
        >>> river.importFileOri('../test/importexport/sections.ori', '../test/importexport/points.ori')
        >>> len(river.sections)
        301

        """
        sectionFile = open(sectionfilename, "r")
        pointsFile = open(pointsfilename, "r")

        # define regexp
        restr = r"""^\s*(?P<points_num>\d+)\s+(?P<sez_name>[sez]+\d+)\s*\n^\s*(?P<first_point>\d+)\s+(?P<first_point_h>[0-9.]+)\s+(?P<last_point>\d+)\s+(?P<last_point_h>[0-9.]+)\s*\n"""
        regexp = re.compile(restr, re.MULTILINE)

        # find all section informations
        matches = [m.groupdict() for m in regexp.finditer(sectionFile.read())]

        # take all data from points.ori
        allcoord = []
        for row in pointsFile:
            allcoord.append([float(x) for x in row.split()])

        # make the list of sections
        sectionlist = []
        first = 0
        last = 0
        for m in matches:
            # make a Section obj
            #print 'Numero punti sezione: %s\nSezione: %s\nPrimoPunto: %s\nPrimoPuntoH: %s\nUltimoPunto: %s\nUltimoPuntoH: %s\n' % (m['points_num'], m['sez_name'], m['first_point'],m['first_point_h'], m['last_point'],m['last_point_h'])
            first += int(m['first_point']) - 1
            last +=  int(m['last_point'])
            sectionlist.append(Section(name=m['sez_name'], data=allcoord[first:last], first=int(m['first_point'])-1, last=int(m['last_point'])))
            first = last
        # asign sections attribute
        self.sections = sectionlist
        return



    def exportFileOri(self, sectionfilename, pointsfilename):
        """
        >>> river = Reach()
        >>> river.importFileOri('../test/importexport/sections.ori', '../test/importexport/points.ori')
        >>> river.exportFileOri('../test/importexport/sectionsTEST.ori', '../test/importexport/pointsTEST.ori')
        Start writing: ../test/importexport/sectionsTEST.ori
        Start writing: ../test/importexport/pointsTEST.ori
        Finish
        """

        sectionFile = open(sectionfilename, "w")
        print "Start writing: %s" % sectionfilename
        sectionFile.write('%s\n' % len(self.sections))
        for sect in self.sections:
            #301
            #4  sez0001
            #1  100.00000   4  100.00000
            #print sect.data
            rows = '%s %s\n%s %s %s %s\n' % (len(sect.data),
                                             sect.name,
                                             sect.first +1,
                                             sect.data[sect.first][2],
                                             sect.last,
                                             sect.data[sect.last-1][2])
            #print rows
            sectionFile.write(rows)
        sectionFile.close()
        print "Start writing: %s" % pointsfilename
        pointsFile = open(pointsfilename, "w")
        for section in self.sections:
            rowlist = []
            for row in section.data:
                rowlist.append(" ".join(['%9.5f' % x for x in row]))
            pointsFile.write('%s\n' % "\n".join([' %s' % r for r in rowlist]))
        pointsFile.close()
        print "Finish"


    def addSection(self, section=None):
        self.sections.append(section)

    def length(self, sectlist = None,  dim = 3):
        """
        >>> river = Reach()
        >>> river.importFileOri('../test/test1/sections.ori', '../test/test1/points.ori')

        to calculate length just only 1D long x
        >>> river.length(dim = 1)
        1500.0

        to calculate length just only 2D long x and y
        >>> river.length(dim = 2)
        1585.0

        to calculate length just only 3D long x, y and z
        >>> river.length(dim = 3)
        1607.1999999999994

        """
        # check input
        if not sectlist:
            sectlist = self.sections

        if dim <= 3:
            dim = int(dim)
        else:
            raise ValueError("dim must be <= 3")

        l = []
        for sez in sectlist:
            #print 'sez.first:', sez.first
            #print 'sez.last:', sez.last
            #print '-', sez.data[sez.first:sez.last]
            data = sez.data[sez.first:sez.last]
            x = dim -4
            l.append(data[0][0:x])
        array = np.array(l)
        #print array
        a1 = np.delete(array, 0, axis=0)
        a2 = np.delete(array, -1, axis=0)
        #print a1, a2
        delta = a2 - a1
        #print delta
        return np.sum(np.sqrt(delta * delta))

    def readSimulation(self):
        pass


if __name__ == "__main__":
    import doctest
    yzcoordT=np.array([[  4.71227679e-01,   7.45000000e+02],\
                      [  9.30000000e-01,   7.42790000e+02],\
                      [  7.19000000e+00,   7.42770000e+02],\
                      [  1.25900000e+01,   7.42750000e+02],\
                      [  1.80800000e+01,   7.42730000e+02],\
                      [  1.89100000e+01,   7.42730000e+02],\
                      [  1.94887253e+01,   7.45000000e+02]])
    sezdata=np.array([[   0.  ,    0.  ,  747.27,   50.  ],
                      [   0.  ,    0.93,  742.79,   50.  ],
                      [   0.  ,    7.19,  742.77,   50.  ],
                      [   0.  ,   12.59,  742.75,   50.  ],
                      [   0.  ,   18.08,  742.73,   50.  ],
                      [   0.  ,   18.91,  742.73,   50.  ],
                      [   0.  ,   20.07,  747.28,   50.  ]])
    section=Section(data=sezdata)
    doctest.testmod()

