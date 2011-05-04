# This file was automatically generated by SWIG (http://www.swig.org).
# Version 1.3.39
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.
# This file is compatible with both classic and new-style classes.

from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_maestroFunctions', [dirname(__file__)])
        except ImportError:
            import _maestroFunctions
            return _maestroFunctions
        if fp is not None:
            try:
                _mod = imp.load_module('_maestroFunctions', fp, pathname, description)
            finally:
                fp.close()
                return _mod
    _maestroFunctions = swig_import_helper()
    del swig_import_helper
else:
    import _maestroFunctions
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0



def py_maestro_open(*args):
  return _maestroFunctions.py_maestro_open(*args)
py_maestro_open = _maestroFunctions.py_maestro_open

def py_maestro_setupimaging(*args):
  return _maestroFunctions.py_maestro_setupimaging(*args)
py_maestro_setupimaging = _maestroFunctions.py_maestro_setupimaging

def py_maestro_shutter_open():
  return _maestroFunctions.py_maestro_shutter_open()
py_maestro_shutter_open = _maestroFunctions.py_maestro_shutter_open

def py_maestro_shutter_close():
  return _maestroFunctions.py_maestro_shutter_close()
py_maestro_shutter_close = _maestroFunctions.py_maestro_shutter_close

def py_maestro_setcolor(*args):
  return _maestroFunctions.py_maestro_setcolor(*args)
py_maestro_setcolor = _maestroFunctions.py_maestro_setcolor

def py_maestro_unlock():
  return _maestroFunctions.py_maestro_unlock()
py_maestro_unlock = _maestroFunctions.py_maestro_unlock

def py_maestro_lock():
  return _maestroFunctions.py_maestro_lock()
py_maestro_lock = _maestroFunctions.py_maestro_lock

def py_maestro_darkfield_on():
  return _maestroFunctions.py_maestro_darkfield_on()
py_maestro_darkfield_on = _maestroFunctions.py_maestro_darkfield_on

def py_maestro_darkfield_off():
  return _maestroFunctions.py_maestro_darkfield_off()
py_maestro_darkfield_off = _maestroFunctions.py_maestro_darkfield_off

def py_maestro_goto_image(*args):
  return _maestroFunctions.py_maestro_goto_image(*args)
py_maestro_goto_image = _maestroFunctions.py_maestro_goto_image

def py_maestro_hometheta():
  return _maestroFunctions.py_maestro_hometheta()
py_maestro_hometheta = _maestroFunctions.py_maestro_hometheta

def py_maestro_unlocktheta():
  return _maestroFunctions.py_maestro_unlocktheta()
py_maestro_unlocktheta = _maestroFunctions.py_maestro_unlocktheta

def py_maestro_locktheta():
  return _maestroFunctions.py_maestro_locktheta()
py_maestro_locktheta = _maestroFunctions.py_maestro_locktheta

def maestro_open(*args):
  return _maestroFunctions.maestro_open(*args)
maestro_open = _maestroFunctions.maestro_open

def consume_bytes(*args):
  return _maestroFunctions.consume_bytes(*args)
consume_bytes = _maestroFunctions.consume_bytes

def maestro_setflag(*args):
  return _maestroFunctions.maestro_setflag(*args)
maestro_setflag = _maestroFunctions.maestro_setflag

def maestro_resetflag(*args):
  return _maestroFunctions.maestro_resetflag(*args)
maestro_resetflag = _maestroFunctions.maestro_resetflag

def maestro_getflag(*args):
  return _maestroFunctions.maestro_getflag(*args)
maestro_getflag = _maestroFunctions.maestro_getflag

def maestro_setupimaging(*args):
  return _maestroFunctions.maestro_setupimaging(*args)
maestro_setupimaging = _maestroFunctions.maestro_setupimaging

def maestro_setcolor(*args):
  return _maestroFunctions.maestro_setcolor(*args)
maestro_setcolor = _maestroFunctions.maestro_setcolor

def maestro_thetadone(*args):
  return _maestroFunctions.maestro_thetadone(*args)
maestro_thetadone = _maestroFunctions.maestro_thetadone

def maestro_thetahoming(*args):
  return _maestroFunctions.maestro_thetahoming(*args)
maestro_thetahoming = _maestroFunctions.maestro_thetahoming

def maestro_stageinmotion(*args):
  return _maestroFunctions.maestro_stageinmotion(*args)
maestro_stageinmotion = _maestroFunctions.maestro_stageinmotion

def maestro_unlock(*args):
  return _maestroFunctions.maestro_unlock(*args)
maestro_unlock = _maestroFunctions.maestro_unlock

def maestro_lock(*args):
  return _maestroFunctions.maestro_lock(*args)
maestro_lock = _maestroFunctions.maestro_lock

def maestro_autofocus_on(*args):
  return _maestroFunctions.maestro_autofocus_on(*args)
maestro_autofocus_on = _maestroFunctions.maestro_autofocus_on

def maestro_shutteropen(*args):
  return _maestroFunctions.maestro_shutteropen(*args)
maestro_shutteropen = _maestroFunctions.maestro_shutteropen

def maestro_shutterclose(*args):
  return _maestroFunctions.maestro_shutterclose(*args)
maestro_shutterclose = _maestroFunctions.maestro_shutterclose

def maestro_readresponse(*args):
  return _maestroFunctions.maestro_readresponse(*args)
maestro_readresponse = _maestroFunctions.maestro_readresponse

def maestro_readresponse2(*args):
  return _maestroFunctions.maestro_readresponse2(*args)
maestro_readresponse2 = _maestroFunctions.maestro_readresponse2

def maestro_stop(*args):
  return _maestroFunctions.maestro_stop(*args)
maestro_stop = _maestroFunctions.maestro_stop

def maestro_get_scan_status(*args):
  return _maestroFunctions.maestro_get_scan_status(*args)
maestro_get_scan_status = _maestroFunctions.maestro_get_scan_status

def maestro_darkfield_on(*args):
  return _maestroFunctions.maestro_darkfield_on(*args)
maestro_darkfield_on = _maestroFunctions.maestro_darkfield_on

def maestro_darkfield_off(*args):
  return _maestroFunctions.maestro_darkfield_off(*args)
maestro_darkfield_off = _maestroFunctions.maestro_darkfield_off

def maestro_hometheta(*args):
  return _maestroFunctions.maestro_hometheta(*args)
maestro_hometheta = _maestroFunctions.maestro_hometheta

def maestro_unlocktheta(*args):
  return _maestroFunctions.maestro_unlocktheta(*args)
maestro_unlocktheta = _maestroFunctions.maestro_unlocktheta

def maestro_locktheta(*args):
  return _maestroFunctions.maestro_locktheta(*args)
maestro_locktheta = _maestroFunctions.maestro_locktheta

def maestro_getstatus(*args):
  return _maestroFunctions.maestro_getstatus(*args)
maestro_getstatus = _maestroFunctions.maestro_getstatus

def maestro_setTDI(*args):
  return _maestroFunctions.maestro_setTDI(*args)
maestro_setTDI = _maestroFunctions.maestro_setTDI

def maestro_debug(*args):
  return _maestroFunctions.maestro_debug(*args)
maestro_debug = _maestroFunctions.maestro_debug

def maestro_setWL(*args):
  return _maestroFunctions.maestro_setWL(*args)
maestro_setWL = _maestroFunctions.maestro_setWL

def maestro_setfocus(*args):
  return _maestroFunctions.maestro_setfocus(*args)
maestro_setfocus = _maestroFunctions.maestro_setfocus

def maestro_getfocus(*args):
  return _maestroFunctions.maestro_getfocus(*args)
maestro_getfocus = _maestroFunctions.maestro_getfocus

def maestro_homing(*args):
  return _maestroFunctions.maestro_homing(*args)
maestro_homing = _maestroFunctions.maestro_homing

def maestro_writefocus(*args):
  return _maestroFunctions.maestro_writefocus(*args)
maestro_writefocus = _maestroFunctions.maestro_writefocus

def maestro_gotostagealign_position(*args):
  return _maestroFunctions.maestro_gotostagealign_position(*args)
maestro_gotostagealign_position = _maestroFunctions.maestro_gotostagealign_position

def maestro_snap(*args):
  return _maestroFunctions.maestro_snap(*args)
maestro_snap = _maestroFunctions.maestro_snap

def maestro_goto_image(*args):
  return _maestroFunctions.maestro_goto_image(*args)
maestro_goto_image = _maestroFunctions.maestro_goto_image

def maestro_reset(*args):
  return _maestroFunctions.maestro_reset(*args)
maestro_reset = _maestroFunctions.maestro_reset

def start_logger(*args):
  return _maestroFunctions.start_logger(*args)
start_logger = _maestroFunctions.start_logger

def close_logger():
  return _maestroFunctions.close_logger()
close_logger = _maestroFunctions.close_logger

def p_log(*args):
  return _maestroFunctions.p_log(*args)
p_log = _maestroFunctions.p_log

def p_log_simple(*args):
  return _maestroFunctions.p_log_simple(*args)
p_log_simple = _maestroFunctions.p_log_simple

def p_log_errorno(*args):
  return _maestroFunctions.p_log_errorno(*args)
p_log_errorno = _maestroFunctions.p_log_errorno

def set_disp(*args):
  return _maestroFunctions.set_disp(*args)
set_disp = _maestroFunctions.set_disp

cvar = _maestroFunctions.cvar
