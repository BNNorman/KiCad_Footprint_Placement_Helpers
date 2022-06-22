# KiCad_Footprint_Placement_Helpers

A KiCad script to put footprints into a circle - I might add other shapes if I need them.

This work is a derivative of the script found here:-
http://kevincuzner.com/2017/04/28/arranging-components-in-a-circle-with-kicad/

That script does not run because it uses Python 2.x print syntax (No brackets) also the KiCad method GetModuleByReference() has been replaced with the better named GetFootprintByReference().

I have used it with KiCad 6 this very day.

Here's a screen shot of a pcb (Work in progress) made for a busy friend. It shows an outer ring of switches and inner ring of WS2812 Leds. There are a couple of other parts but the switches and leds were positioned using the script.

![image](https://user-images.githubusercontent.com/15849181/175064998-c0fbd2fa-526c-452b-98ff-293a20f63809.png)

# Other script changes

The original script only accepted mils as dimensions (who works in mils?) so I renamed the method place_circle_mils and added place_circle_mm so I could use mm as my dimensions.

# Outstanding issues

The original script ends by asking to press F11 to referesh but that didn't work for me. I had to save-close and re-open the pcb to see the effects. When I find a better way (like an updateScreen() method I'll amend the script accordingly.

# Installing the script

On windows it needs to go in C:\Program Files\KiCad\6.0\share\kicad\scripting\plugins - you might need elevated permissions to put it there.

# Using the script

Open a scripting console (Tools->Scripting Console) and at the Python prompt (>>>) enter
```
>>> import placement_helpers
>>> placement_helpers.place_circle_mm(["SW1","SW2","SW3","SW4","SW5","SW6","SW7","SW8","SW9","SW10","SW11","SW12"],15,(127,127),34,0)
```

Assuming you have 12 switches and you want the first to start at 15 degrees, centred at (127,127) and 34mm radius

# Circle Method parameters
```
    refdes: List of component references, e.g. ["SW1", ...]
    start_angle: Starting angle
    center: Tuple of (x, y) mm of circle center
    radius: Radius of the circle in mm
    component_offset: Offset in degrees for each component to add to angle
    hide_ref: Hides the reference if true, leaves it be if None
    lock: Locks the footprint if true
```
placement_helpers.place_circle_mm(refdes, start_angle, center, radius, component_offset=0, hide_ref=True, lock=False)

Alternatively, using mils:-

placement_helpers.place_circle_mils(refdes, start_angle, center, radius, component_offset=0, hide_ref=True, lock=False)

