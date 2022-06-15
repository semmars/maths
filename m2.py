__all__ = ['m2']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *

# setting scope
var = Scope(JS_BUILTINS)
set_global_object(var)

# Code follows:
var.registers(['y', 'x', 'cellArea', 'xCoordinate', 'yCoordinate', 'result'])
Js('use strict')
var.put('cellArea', ((Js(8.0) / Js(100000.0)) * (Js(4.0) / Js(50000.0))))
var.put('result', Js(0.0))
var.get('console').callprop('time', Js('Operating time'))
# for JS loop
var.put('x', Js(0.0))
while (var.get('x') < Js(100000.0)):
    try:
        # for JS loop
        var.put('y', Js(0.0))
        while (var.get('y') < Js(50000.0)):
            try:
                var.put('xCoordinate', ((var.get('x') / Js(100000.0)) * Js(8.0)))
                var.put('yCoordinate', ((var.get('y') / Js(50000.0)) * Js(4.0)))
                if (((var.get('xCoordinate') <= Js(4.0)) and (
                        (var.get('yCoordinate') / var.get('xCoordinate')) <= Js(0.5))) and (
                        var.get('Math').callprop('sqrt', (var.get('Math').callprop('pow',
                                                                                   var.get('Math').callprop('abs', (
                                                                                           var.get('xCoordinate') - Js(
                                                                                           4.0))), Js(2.0)) + var.get(
                                'Math').callprop('pow',
                                                 var.get('Math').callprop('abs', (var.get('yCoordinate') - Js(4.0))),
                                                 Js(2.0)))) >= Js(4.0))):
                    var.put('result', var.get('cellArea'), '+')
            finally:
                (var.put('y', Js(var.get('y').to_number()) + Js(1)) - Js(1))
    finally:
        (var.put('x', Js(var.get('x').to_number()) + Js(1)) - Js(1))
var.get('console').callprop('log', (Js('The area under the curve is：') + var.get('result')))
var.get('console').callprop('timeEnd', Js('Operating time'))
pass

# Add lib to the module scope
m2 = var.to_python()
