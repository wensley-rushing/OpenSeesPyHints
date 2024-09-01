import opensees.openseespy as ops

def flag(flag):
    """
   Set the initial state analysis to ``'on'`` or ``'off'``



   ========================   ===========================================================================

   ``flag`` |str|             ``'on'`` or ``'off'``

   ========================   ===========================================================================

    """
    uniqueArgs = []
    ops.InitialStateAnalysis(flag, *uniqueArgs)

