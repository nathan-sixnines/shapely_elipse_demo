demo of shapely finding intersection between elipses

To use:

pip install -r requirements.txt

python elipses.py


It will draw some plots in the local directory and print out some points

If you take this further, be aware shapely functions like intersect can return different types of objects depending on what the intersection actually is.

Be prepared to handle them differently with some sort of filter like described here:

https://stackoverflow.com/questions/39142876/check-if-a-polygon-is-a-multipolygon-in-shapely

The general methods page linked there moved:

https://shapely.readthedocs.io/en/latest/manual.html?highlight=general%20attributes#geometric-objects
