# Random placement helpers because I'm tired of using spreadsheets for doing this
#
# Kevin Cuzner
#
# install at C:\Program Files\KiCad\6.0\share\kicad\scripting\plugins
 
import math
from pcbnew import *
 

mm_to_mils=39.37007874015748
 
def place_circle_mm(refdes, start_angle, center, radius, component_offset=0, hide_ref=True, lock=False):
    """
    Places components in a circle
    refdes: List of component references
    start_angle: Starting angle
    center: Tuple of (x, y) mm of circle center
    radius: Radius of the circle in mm
    component_offset: Offset in degrees for each component to add to angle
    hide_ref: Hides the reference if true, leaves it be if None
    lock: Locks the footprint if true
    """
    cx,cy=center
    cx=cx*mm_to_mils
    cy=cy*mm_to_mils
    radius=radius*mm_to_mils
    place_circle_mils(refdes, start_angle, (cx,cy), radius, component_offset, hide_ref, lock)

	
def place_circle_mils(refdes, start_angle, center, radius, component_offset=0, hide_ref=True, lock=False):
    """
    Places components in a circle
    refdes: List of component references
    start_angle: Starting angle
    center: Tuple of (x, y) mils of circle center
    radius: Radius of the circle in mils
    component_offset: Offset in degrees for each component to add to angle
    hide_ref: Hides the reference if true, leaves it be if None
    lock: Locks the footprint if true
    """
    pcb = GetBoard()
    deg_per_idx = 360 / len(refdes)
    for idx, rd in enumerate(refdes):
        part = pcb.FindFootprintByReference(rd)
        angle = (deg_per_idx * idx + start_angle) % 360;
        print ("{0}: {1}".format(rd, angle))
        xmils = center[0] + math.cos(math.radians(angle)) * radius
        ymils = center[1] + math.sin(math.radians(angle)) * radius
        print ("{0}: {1} ({2:.6f},{3:.6f})".format(rd, angle,xmils,ymils))
        part.SetPosition(wxPoint(FromMils(xmils), FromMils(ymils)))
        part.SetOrientation(angle * -10)
        if hide_ref is not None:
            part.Reference().SetVisible(not hide_ref)
    print ("Placement finished. Press F11 to refresh.")