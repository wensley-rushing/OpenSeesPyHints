import opensees.openseespy as ops

def patternTag(patternTag, paramTag):
    """
   Returns the current load factor sensitivity to a parameter in a load pattern.



   ========================   ===========================================================================

   ``patternTag`` |int|       load pattern tag

   ``paramTag`` |int|         parameter tag

   ========================   ===========================================================================

    """
    uniqueArgs = []
    ops.sensLambda(patternTag, paramTag, *uniqueArgs)

