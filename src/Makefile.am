ACLOCAL_AMFLAGS = ${ACLOCAL_FLAGS} -I m4

AM_CPPFLAGS = \
    -I../include \
    -Wall -Wextra -Werror -Wno-implicit-function-declaration

lib_LTLIBRARIES = libodpic.la

libodpic_la_LDFLAGS = -release $(LIBODPIC_API_VERSION)

libodpic_la_LIBADD = \
    -ldl -lpthread

libodpic_la_SOURCES = \
    dpiConn.c \
    dpiContext.c \
    dpiData.c \
    dpiDebug.c \
    dpiDeqOptions.c \
    dpiEnqOptions.c \
    dpiEnv.c \
    dpiError.c \
    dpiErrorMessages.h \
    dpiGen.c \
    dpiGlobal.c \
    dpiHandleList.c \
    dpiHandlePool.c \
    dpiImpl.h \
    dpiLob.c \
    dpiMsgProps.c \
    dpiObjectAttr.c \
    dpiObject.c \
    dpiObjectType.c \
    dpiOci.c \
    dpiOracleType.c \
    dpiPool.c \
    dpiQueue.c \
    dpiRowid.c \
    dpiSodaColl.c \
    dpiSodaCollCursor.c \
    dpiSodaDb.c \
    dpiSodaDoc.c \
    dpiSodaDocCursor.c \
    dpiStmt.c \
    dpiSubscr.c \
    dpiUtils.c \
    dpiVar.c
