include $(top_srcdir)/Makefile.decl

NULL =

AM_CPPFLAGS = \
	-I$(top_srcdir)/gee \
	$(GLIB_CFLAGS) \
	$(NULL)

noinst_PROGRAMS = $(TEST_PROGS)

progs_ldadd = $(GLIB_LIBS) ../gee/libgee.la

TEST_PROGS += testarraylist
testarraylist_VALASOURCES = testarraylist.vala
testarraylist_SOURCES = testarraylist.c testarraylist.h
$(testarraylist_SOURCES): $(testarraylist_VALASOURCES)
	$(VALAC) -C --vapidir $(top_srcdir)/gee/gee --pkg gdom3-1.0-gee $^
	touch $@
testarraylist_LDADD = $(progs_ldadd)
EXTRA_DIST += $(testarraylist_VALASOURCES)

TEST_PROGS += testhashmap
testhashmap_VALASOURCES = testhashmap.vala
testhashmap_SOURCES = testhashmap.c testhashmap.h
$(testhashmap_SOURCES): $(testhashmap_VALASOURCES)
	$(VALAC) -C --vapidir $(top_srcdir)/gee/gee --pkg gdom3-1.0-gee $^
	touch $@
testhashmap_LDADD = $(progs_ldadd)
EXTRA_DIST += $(testhashmap_VALASOURCES)

TEST_PROGS += testhashset
testhashset_VALASOURCES = testhashset.vala
testhashset_SOURCES = testhashset.c testhashset.h
$(testhashset_SOURCES): $(testhashset_VALASOURCES)
	$(VALAC) -C --vapidir $(top_srcdir)/gee/gee --pkg gdom3-1.0-gee $^
	touch $@
testhashset_LDADD = $(progs_ldadd)
EXTRA_DIST += $(testhashset_VALASOURCES)

