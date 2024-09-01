import opensees.openseespy as ops

def eleTag(eleTag):
    """
   Get nodes in an element



   ========================   ===========================================================================

   ``eletag`` |int|           element tag.

   ========================   ===========================================================================

    """
    uniqueArgs = []
    ops.eleNodes(eleTag, *uniqueArgs)

