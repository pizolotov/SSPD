from phidl import Device
from phidl import quickplot as qp # Rename "quickplot()" to the easier "qp()"
import phidl.geometry as pg

Markhorizontal = Device()

xpts = (0   , 137,  137,    0,  0,   27,    27,     87,     87,     27,     27,     0,      0)
ypts = (2613, 2613, 2887, 2887, 2837, 2837, 2777,   2777,   2723,   2723,   2663,   2663,   2613)
Markhorizontal.add_polygon( [xpts, ypts], layer = 0)
#markleft = Marks.add_polygon( [xpts, ypts], layer = 0)




Markvertical = Device()

xpts = (1323,   1323,   1637,   1637,   1587,   1587,   1527,   1527,   1473,   1473,   1373,   1373)
ypts = (4000,   3863,   3863,   4000,   4000,   3973,   3973,   3913,   3913,   3973,   3973,   4000)
Markvertical.add_polygon( [xpts, ypts], layer = 0)
#marktop = Marks.add_polygon( [xpts, ypts], layer = 0)


#marktop2 = Marks.add_ref(markleft)
#mark.move([100,0])

#qp(Marks)




Markslayot = Device()

marktop = Markslayot.add_ref(Markvertical)
markbot = Markslayot.add_ref(Markvertical)
markbot.mirror(p1 = [0,2000], p2 = [1500,2000]) # Reflects across the line formed by p1 and p2


markleft = Markslayot.add_ref(Markhorizontal)
markright = Markslayot.add_ref(Markhorizontal)
markright.mirror(p1 = [1500,0], p2 = [1500,4000]) # Reflects across the line formed by p1 and p2






Groundcontact = Device()
xpts = (250, 250,2750,2750,2160,2160,1967,1578,1422,1033, 840,840)
ypts = (250,3750,3750, 250, 250,3160,3160,2825,2825,3160,3160,250)
#                               structure connect^
Groundcontact.add_polygon( [xpts, ypts], layer = 0)





Centralcontact = Device()
xpts = (1033,1967,1967,1578,1422,1033)
ypts = ( 250, 250,2340,2675,2675,2340)
#           structure connect^
Centralcontact.add_polygon( [xpts, ypts], layer = 0)




Chip_prelim = Device()
Centralcontact = Chip_prelim.add_ref(Centralcontact)
Groundcontact = Chip_prelim.add_ref(Groundcontact)
Markslayot = Chip_prelim.add_ref(Markslayot)



qp(Chip_prelim)



#Chip_prelim.write_gds(filename = 'triple-bend.gds')
