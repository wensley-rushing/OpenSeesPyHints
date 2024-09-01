import opensees.openseespy as ops

def eleTag(eleTag, secNum):
    """
   Returns the locations of integration points of a section for a beam-column element.



   ========================   ===========================================================================

   ``eleTag`` |int|           element tag.

   ``secNum`` |int|           section number, i.e. the Gauss integration number

   ========================   ===========================================================================

    """
    uniqueArgs = []
    ops.sectionLocation(eleTag, secNum, *uniqueArgs)

