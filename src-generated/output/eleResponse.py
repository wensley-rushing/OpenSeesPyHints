import opensees.openseespy as ops

def eleTag(eleTag, args):
    """
   This command is used to obtain the same element quantities as those obtained from the element recorder at a particular time step.



   ========================   ===========================================================================

   ``eletag`` |int|           element tag.

   ``args`` |list|                    same arguments as those specified in element recorder. These arguments are specific to the type of element being used.

   ========================   ===========================================================================

    """
    uniqueArgs = []
    ops.eleResponse(eleTag, *args, *uniqueArgs)

