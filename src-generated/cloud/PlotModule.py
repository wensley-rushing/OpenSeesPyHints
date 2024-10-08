import opensees.openseespy as ops

def xLabel(xLabel, yLabel, labels):
    """
   This command is used to reset the :doc:`PlotModule` with labels.



   ========================   ===========================================================================

   ``xLabel`` |str|           the string for the label of x axis.

   ``yLabel`` |str|           the string for the label of y axis.

   ``labels`` |lists|         a list of ticks to be shown instead of x values.

   ========================   ===========================================================================





.. note::



   This must be the first command to call in :doc:`PlotModule`.

    """
    uniqueArgs = []
    ops.reset_plot(xLabel, yLabel, labels, *uniqueArgs)

def x(x, y, label, color):
    """
   This command is used to add a line in the :doc:`PlotModule`.



   ========================   ===================================================================================

   ``x`` |listf|              a list of x values

   ``y`` |listf|              a list of y values

   ``label`` |str|            the label name for the line in the legend

   ``color`` |str|            the color for the line, the value could be:



                              - rgb values as ``'rgb(r,g,b)'`` betwen ``[0, 255]``.

                              - a color name such as ``'white'``, ``'black'``, ``'blue'``, etc.

   ``bgColor`` |str|          the color for filling the area below the line, if ``fill`` is set to ``True``.

   ``lineWidth`` |int|        the line width

   ``lineStyle`` |str|        the line style, valid values include:



                              - ``'solid'``

                              - ``'dotted'``

                              - ``'dashed'``

                              - ``'long-dashed'``

                              - ``'dashed-dotted'``

                              - ``'dashed-dotted-dotted'``

                              - ``'dotted-dashed-dotted'``

   ``fill`` |bool|            whether to fill the area below the line

   ``pointStyle`` |str|       the point style, valid values include:



                              - ``'circle'``

                              - ``'cross'``

                              - ``'crossRot'``

                              - ``'dash'``

                              - ``'line'``

                              - ``'rect'``

                              - ``'rectRounded'``

                              - ``'rectRot'``

                              - ``'star'``

                              - ``'triangle'``

   ``pointSize`` |int|        the point size

   ``pointColor`` |str|       the point border color, if = ``''``, the line color is used

   ``pointBgColor`` |str|     the point fill color

   ``lineTension`` |float|    if ``0.0``, straight lines are drawn, otherwise, Bezier curves are drawn.

   ========================   ===================================================================================



    """
    uniqueArgs = []
    ops.plot_line(x, y, label, color, *uniqueArgs)

