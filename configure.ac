AC_INIT(libgdom3, [0.0.1], [rainwoodman@gmail.com], [libgdom3])

AM_INIT_AUTOMAKE([1.9 tar-ustar])
AC_CONFIG_SRCDIR([Makefile.am])
AC_CONFIG_HEADERS(config.h)

# Checks for programs.
AC_PROG_CC
AM_PROG_CC_C_O
AC_DISABLE_STATIC
AC_PROG_LIBTOOL

# Check for Vala
AC_SUBST(VALA_REQUIRED, [0.5.1])

AC_CACHE_CHECK([checking for vala = $VALA_REQUIRED],
		[ac_cv_path_VALAC],
		[AC_PATH_PROGS_FEATURE_CHECK([VALAC], 
			[valac valac [`pwd`/vala$PATH_SEPARATOR$PATH]],
			[[
			$ac_path_VALAC --version | grep $VALA_REQUIRED &&
				ac_cv_path_VALAC=$ac_path_VALAC ac_path_VALAC_found=: 
			]],
			[AC_MSG_ERROR([could not find vala version $VALA_REQUIRED])]
			)]
		)
AC_SUBST(VALAC)

AC_SUBST(CFLAGS)
AC_SUBST(CPPFLAGS)
AC_SUBST(LDFLAGS)

GLIB_REQUIRED=2.10.0

PKG_CHECK_MODULES(GLIB, glib-2.0 >= $GLIB_REQUIRED gobject-2.0 >= $GLIB_REQUIRED)
AC_SUBST(GLIB_CFLAGS)
AC_SUBST(GLIB_LIBS)

AC_CONFIG_FILES([Makefile
			gee/Makefile
           gee/gee/Makefile
           gee/tests/Makefile
		   gdom3-1.0.pc
		   src/Makefile
		   tests/Makefile
		   ])

AC_OUTPUT
