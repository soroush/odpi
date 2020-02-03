AC_PREREQ([2.69])
AC_INIT([libodpic], [3.3.0], [])
LT_INIT
AC_LANG([C])

AM_INIT_AUTOMAKE
AM_SILENT_RULES([yes])
AC_CONFIG_MACRO_DIR([m4])
AC_CONFIG_HEADERS([config.h])

# Checks for programs.
AC_PROG_AWK
AC_PROG_CC
AC_PROG_CPP
AC_PROG_INSTALL
AC_PROG_LN_S
AC_PROG_MAKE_SET
AC_PROG_LIBTOOL

AC_TYPE_SIZE_T
AC_CHECK_HEADER_STDBOOL

# Checks for header files.
AC_CHECK_HEADERS([float.h inttypes.h limits.h stdint.h stdlib.h string.h sys/time.h unistd.h])

# Checks for typedefs, structures, and compiler characteristics.
AC_CHECK_HEADER_STDBOOL
AC_TYPE_INT16_T
AC_TYPE_INT32_T
AC_TYPE_INT64_T
AC_TYPE_INT8_T
AC_TYPE_PID_T
AC_TYPE_SIZE_T
AC_TYPE_UINT16_T
AC_TYPE_UINT32_T
AC_TYPE_UINT64_T
AC_TYPE_UINT8_T

# Checks for library functions.
AC_FUNC_ERROR_AT_LINE
AC_FUNC_MALLOC
AC_FUNC_REALLOC
AC_CHECK_FUNCS([atexit gettimeofday localtime_r memset strchr strrchr strtol])

AX_CHECK_COMPILE_FLAG([-std=c11],
    [CFLAGS+=" -std=c11"],
    [
        echo "C compiler cannot compile C11 code"
        exit -1
    ]
)

AC_CONFIG_FILES([Makefile
                 include/Makefile
                 src/Makefile
                 test/Makefile
                 libodpic.pc])

AC_SUBST([LIBODPIC_API_VERSION], [3.3.0])

AC_OUTPUT
