include $(top_srcdir)/Makefile.decl

NULL = 
VALASOURCES = \
	test-text.vala \
	test-node.vala \
	test-documentfragment.vala \
	test-element.vala \
	test-memory.vala \
	test-document.vala \
	test-serializer.vala \
	$(NULL)

TEST_PROGS+=$(VALASOURCES:.vala=)
#
#	test-attr.vala \
#	test-extended.vala \
#	test-comment.vala \
#	#(NULL)
AM_CPPFLAGS = \
	-g \
	-I$(top_srcdir)/gee \
	-I$(top_srcdir)/src \
	$(GLIB_CFLAGS) \
	$(NULL)

BUILT_SOURCES = test.vapi \
		test.c \
		test.h \
		$(VALASOURCES:.vala=.stamp) \
		$(VALASOURCES:.vala=.c) \
		$(VALASOURCES:.vala=.h)

noinst_LTLIBRARIES = libtest.la

libtest_la_SOURCES = test.c test.h

test.vapi:	test.vala

SUFFIXES = .vala .stamp
test.vapi: test.vala
	$(VALAC) -C --library test $^
	sed test.h -e '10i\ typedef void* GDataTestFunc;' > test.h.new; 
	mv test.h.new test.h
test.stamp: test.vapi
	touch $@

.vala.stamp:
	$(VALAC) -C --vapidir=. --vapidir=$(top_srcdir)/gee/gee --vapidir=$(top_srcdir)/src --pkg gdom3-1.0 --pkg test $(@:.stamp=.vala)
	touch $@

noinst_PROGRAMS = $(TEST_PROGS)
LDADD = ../src/libgdom3.la libtest.la
EXTRA_DIST += $(VALASOURCES) test.vala test.vapi $(BUILT_SOURCES)
