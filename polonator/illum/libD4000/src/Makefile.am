AM_CFLAGS = -lusb 
AM_CPPFLAGS = -DD4000_USB_BIN='"$(firmwaredir)/D4000_usb.bin"'
lib_LTLIBRARIES = libD4000.la
libD4000_la_SOURCES = libD4000.cpp porting.c porting.h
libD4000_ladir = $(includedir)
libD4000_la_HEADERS = libD4000.h
libD4000_la_LIBADD = -lusb
libD4000_la_LDFLAGS = -version-info 1:0:0

