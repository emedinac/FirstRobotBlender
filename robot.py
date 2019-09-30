import bpy
import os
def Draw_Base_Plate(): #This function will draw base plate
    #Added two cubes for cutting sides of base plate
    bpy.ops.mesh.primitive_cube_add(radius=0.05, location=(0.175,0,0.09))
    bpy.ops.mesh.primitive_cube_add(radius=0.05, location=(-0.175,0,0.09))
    #Adding base plate
    bpy.ops.mesh.primitive_cylinder_add(radius=0.15,depth=0.005, location=(0,0,0.09))
    #Adding booleab difference modifier from first cube
    bpy.ops.object.modifier_add(type='BOOLEAN')
    bpy.context.object.modifiers["Boolean"].operation = 'DIFFERENCE'
    bpy.context.object.modifiers["Boolean"].object = bpy.data.objects["Cube"]
    bpy.ops.object.modifier_apply(modifier="Boolean")

    #Adding booleab difference modifier from second cube
    bpy.ops.object.modifier_add(type='BOOLEAN')
    bpy.context.object.modifiers["Boolean"].operation = 'DIFFERENCE'
    bpy.context.object.modifiers["Boolean"].object = bpy.data.objects["Cube.001"]
    bpy.ops.object.modifier_apply(modifier="Boolean")
    
    #Deselect cylinder and delete cubes
    bpy.ops.object.select_pattern(pattern="Cube")
    bpy.ops.object.select_pattern(pattern="Cube.001")
    bpy.data.objects['Cylinder'].select = False
    bpy.ops.object.delete(use_global=False)
    
def Draw_Motors_Wheels(): #This function will draw motors and wheels  
    #Create first Wheel
    bpy.ops.mesh.primitive_cylinder_add(radius=0.045,depth=0.01, location=(0,0,0.07))
    #Rotate
    bpy.context.object.rotation_euler[1] = 1.5708
    #Transalation
    bpy.context.object.location[0] = 0.135
    #Create second wheel
    bpy.ops.mesh.primitive_cylinder_add(radius=0.045,depth=0.01, location=(0,0,0.07))
    #Rotate
    bpy.context.object.rotation_euler[1] = 1.5708
    #Transalation
    bpy.context.object.location[0] = -0.135

    #Adding motors    
    bpy.ops.mesh.primitive_cylinder_add(radius=0.018,depth=0.06, location=(0.075,0,0.075))
    bpy.context.object.rotation_euler[1] = 1.5708
    
    bpy.ops.mesh.primitive_cylinder_add(radius=0.018,depth=0.06, location=(-0.075,0,0.075))
    bpy.context.object.rotation_euler[1] = 1.5708
   
    #Adding motor shaft
    bpy.ops.mesh.primitive_cylinder_add(radius=0.006,depth=0.04, location=(0.12,0,0.075))
    bpy.context.object.rotation_euler[1] = 1.5708
    
    bpy.ops.mesh.primitive_cylinder_add(radius=0.006,depth=0.04, location=(-0.12,0,0.075))
    bpy.context.object.rotation_euler[1] = 1.5708
    
    #Addubg Caster Wheel
    bpy.ops.mesh.primitive_cylinder_add(radius=0.015,depth=0.05, location=(0,0.125,0.065))
    bpy.ops.mesh.primitive_cylinder_add(radius=0.015,depth=0.05, location=(0,-0.125,0.065))
    
    #Adding Kinect
    bpy.ops.mesh.primitive_cube_add(radius=0.02, location=(0,0,0.147))    
 
def Draw_Plates():
    bpy.ops.mesh.primitive_cylinder_add(radius=0.15,depth=0.005, location=(0,0,0.125)) # middle plate
    bpy.ops.mesh.primitive_cylinder_add(radius=0.15,depth=0.005, location=(0,0,0.167)) # top plate

#Adding support tubes
def Draw_Support_Tubes(): #Cylinders
    bpy.ops.mesh.primitive_cylinder_add(radius=0.007,depth=0.10, location=(0.09,0.09,0.12))
    bpy.ops.mesh.primitive_cylinder_add(radius=0.007,depth=0.10, location=(-0.09,0.09,0.12))
    bpy.ops.mesh.primitive_cylinder_add(radius=0.007,depth=0.10, location=(-0.09,-0.09,0.12))
    bpy.ops.mesh.primitive_cylinder_add(radius=0.007,depth=0.10, location=(0.09,-0.09,0.12))

def Save_to_STL():
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.export_mesh.stl(check_existing=True, filepath="./wheelrobot.stl", filter_glob="*.stl", ascii=False, use_mesh_modifiers=True, axis_forward='Y', axis_up='Z', global_scale=1.0)

if __name__ == "__main__":
    Draw_Base_Plate()
    Draw_Motors_Wheels()
    Draw_Plates()
    Draw_Support_Tubes()
    Save_to_STL()