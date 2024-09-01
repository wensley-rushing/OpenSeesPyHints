import opensees.openseespy as ops

def PFEM():
    """


   Create a PFEM Integrator.

    """
    uniqueArgs = []
    ops.integrator('PFEM', *uniqueArgs)

