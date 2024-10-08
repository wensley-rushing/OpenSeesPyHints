import opensees.openseespy as ops

def file(filename):
    """
   print the right hand side of a FullGeneral system that the integrator creates to the screen or a file if the ``'-file'`` option is used.



   ===========================   =====================================================================================================================================================

   ``filename`` |str|            name of file to which output is sent, by default, print to the screen. (optional)

   ``'-ret'`` |str|              return the B vector as a list. (optional)

   ===========================   =====================================================================================================================================================

    """
    uniqueArgs = []
    if '-ret':
        uniqueArgs.append('-ret')
    ops.printB('-file', filename, *uniqueArgs)

