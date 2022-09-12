import bpy
from animation_nodes.ui.node_menu import insertNode

class TestExtensionMenu(bpy.types.Menu):
    bl_idname = "an_psd_texture"
    bl_label = "PSD Texture"

    def draw(self, context):
        layout = self.layout
        insertNode(layout, "an_psd_texture", "PSD Texture")

def drawMenu(self, context):
    if context.space_data.tree_type != "an_psd_texture": return

    layout = self.layout
    layout.operator_context = "INVOKE_DEFAULT"

    layout.separator()
    layout.menu("an_psd_texture", text = "PSD Texture", icon = "SCRIPTPLUGINS")

def register():
    bpy.types.NODE_MT_add.append(drawMenu)

def unregister():
    bpy.types.NODE_MT_add.remove(drawMenu)
