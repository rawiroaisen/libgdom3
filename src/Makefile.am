include $(top_srcdir)/Makefile.decl

NULL =

AM_CPPFLAGS = \
	-I$(top_srcdir)/gee \
	$(GLIB_CFLAGS) \
	$(NULL)

BUILT_SOURCES = dom.vala.stamp

lib_LTLIBRARIES = \
	libgdom3.la
	$(NULL)

libgdom3_la_VALASOURCES = \
		dom-error.vala \
		dom-node.vala \
		dom-attr.vala \
		dom-characterdata.vala \
		dom-text.vala \
		dom-extended.vala \
		dom-comment.vala \
		dom-element.vala \
		dom-document.vala \
		dom-documentfragment.vala \
		dom-visitor.vala \
		dom-serializer.vala \
	$(NULL)


libgdom3_la_SOURCES = \
	dom.vala.stamp \
	$(libgdom3_la_VALASOURCES:.vala=.c) \
	$(libgdom3_la_VALASOURCES:.vala=.h) \
	$(NULL)

domincludedir = $(includedir)/gdom3-1.0

dominclude_HEADERS = \
	$(libgdom3_la_VALASOURCES:.vala=.h) \
	$(NULL)

gdom3-1.0.vapi gdom3-1.0.deps dom.vala.stamp: $(libgdom3_la_VALASOURCES)
	$(VALAC) -C --vapidir $(top_srcdir)/gee/gee --pkg gdom3-1.0-gee --basedir $(top_srcdir)/src --library gdom3-1.0 $^
	bash patch.sh 
	echo gdom3-1.0-gee > gdom3-1.0.deps
	touch $@

libgdom3_la_LIBADD = \
	$(GLIB_LIBS) \
	$(top_builddir)/gee/gee/libgee.la \
	$(NULL)

libgdom3_la_LDFLAGS = -version-info 0:0:0 -no-undefined

vapidir = $(datadir)/vala/vapi

dist_vapi_DATA = \
	gdom3-1.0.vapi \
	gdom3-1.0.deps \
	$(NULL)

EXTRA_DIST += $(libgdom3_la_VALASOURCES) gdom3-1.0.vapi dom.vala.stamp patch.sh gdom3-1.0.deps
