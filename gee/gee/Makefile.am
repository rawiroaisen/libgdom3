include $(top_srcdir)/Makefile.decl

NULL =

AM_CPPFLAGS = \
	-I$(top_srcdir)/gee \
	$(GLIB_CFLAGS) \
	$(NULL)

BUILT_SOURCES = gee.vala.stamp

noinst_LTLIBRARIES = \
	libgee.la \
	$(NULL)

libgee_la_VALASOURCES = \
	arraylist.vala \
	collection.vala \
	hashmap.vala \
	hashset.vala \
	iterable.vala \
	iterator.vala \
	list.vala \
	map.vala \
	readonlycollection.vala \
	readonlylist.vala \
	readonlymap.vala \
	readonlyset.vala \
	set.vala \
	$(NULL)

libgee_la_SOURCES = \
	gee.vala.stamp \
	$(libgee_la_VALASOURCES:.vala=.c) \
	$(libgee_la_VALASOURCES:.vala=.h) \
	$(NULL)

geeincludedir = $(includedir)/gdom3-1.0/gee

geeinclude_HEADERS = \
	$(libgee_la_VALASOURCES:.vala=.h) \
	$(NULL)

gdom3-1.0-gee.vapi gee.vala.stamp: $(libgee_la_VALASOURCES)
	$(VALAC) -C --basedir $(top_srcdir)/gee --library gdom3-1.0-gee $^
	touch $@

libgee_la_LIBADD = \
	$(GLIB_LIBS) \
	$(NULL)
libgee_la_LDFLAGS = -version-info 1:0:0 -no-undefined -release $(VERSION)

vapidir = $(datadir)/vala/vapi

dist_vapi_DATA = \
	gdom3-1.0-gee.vapi \
	$(NULL)

EXTRA_DIST += $(libgee_la_VALASOURCES) gdom3-1.0-gee.vapi gee.vala.stamp
