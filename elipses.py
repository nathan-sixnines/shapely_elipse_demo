#source: https://gis.stackexchange.com/questions/243459/drawing-ellipse-with-shapely

from matplotlib import pyplot
from shapely.geometry.point import Point
import shapely.affinity
from descartes import PolygonPatch
# Note: download figures.py manually from shapely github repo, put it in shapely install directory
from figures import SIZE, GREEN, GRAY, set_limits


# 1st elem = center point (x,y) coordinates
# 2nd elem = the two semi-axis values (along x, along y)
# 3rd elem = angle in degrees between x-axis of the Cartesian base
#            and the corresponding semi-axis
ellipse = ((0, 0),(7, 4),36)

# Let create a circle of radius 1 around center point:
circ = shapely.geometry.Point(ellipse[0]).buffer(1)

# Let create the ellipse along x and y:
ell  = shapely.affinity.scale(circ, int(ellipse[1][0]), int(ellipse[1][1]))

# Let rotate the ellipse (clockwise, x axis pointing right):
ellr = shapely.affinity.rotate(ell,ellipse[2])

# If one need to rotate it clockwise along an upward pointing x axis:
elrv = shapely.affinity.rotate(ell,90-ellipse[2])
# According to the man, a positive value means a anti-clockwise angle,
# and a negative one a clockwise angle.


ellipse2 = ((-4, -4),(7, 4),140)
circ2 = shapely.geometry.Point(ellipse2[0]).buffer(1)
ell2  = shapely.affinity.scale(circ2, int(ellipse2[1][0]), int(ellipse2[1][1]))
ellr2 = shapely.affinity.rotate(ell2,ellipse2[2])
elrv2 = shapely.affinity.rotate(ell2,90-ellipse2[2])

inter = elrv.intersection(elrv2)

fig = pyplot.figure()
fig2 = pyplot.figure()
ax = fig.add_subplot(111)
ax2 = fig2.add_subplot(111)
patch = PolygonPatch(elrv, fc=GREEN, ec=GRAY, alpha=0.5, zorder=2)
patch2 = PolygonPatch(elrv2, fc=GREEN, ec=GRAY, alpha=0.5, zorder=2)
ax.add_patch(patch)
ax.add_patch(patch2)

interPatch = PolygonPatch(inter, fc=GREEN, ec=GRAY, alpha=0.5, zorder=2)
ax2.add_patch(interPatch)

set_limits(ax, -10, 10, -10, 10)
set_limits(ax2, -10, 10, -10, 10)

fig.savefig('elipses.png')
fig2.savefig('intersection.png')
