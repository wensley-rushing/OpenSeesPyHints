import opensees.openseespy as ops

def nodeTag(nodeTag):
    """
   Returns the DOF numbering of a node.



   ========================   ===========================================================================

   ``nodeTag`` |int|          node tag.

   ========================   ===========================================================================

    """
    uniqueArgs = []
    ops.nodeDOFs(nodeTag, *uniqueArgs)

