Name:           libodpic
Version:        3.3.0
Release:        1%{?dist}
Summary:        Oracle Database Programming Interface for C (ODPI-C)

Group:          System Environment/Libraries
License:        Apache
URL:            https://github.com/soroush/odpi
Source0:        %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


# Prevent strip binaries (bugfix)
%global __strip /bin/true

# Declare dependencies
BuildRequires: gcc

# Uses Oracle OCCI 19.5 (Though we don't link against any of these libs)
BuildRequires: oracle-instantclient19.5-devel >= 19.5
BuildRequires: oracle-instantclient19.5-basic >= 19.5

# Uses pkgconfig
BuildRequires: pkgconfig

Requires: oracle-instantclient19.5-devel >= 19.5
Requires: oracle-instantclient19.5-basic >= 19.5

%description
Oracle Database Programming Interface for C (ODPI-C) is an open source
library of C code that simplifies access to Oracle Database for
applications written in C or C++. It is a wrapper over Oracle Call
Interface (OCI) that makes applications and language interfaces easier
to develop.

ODPI-C supports basic and advanced features of Oracle Database and
Oracle Client.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       oracle-instantclient19.5-devel >= 19.5
Requires:       oracle-instantclient19.5-basic >= 19.5

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q

%build
%configure \
    --disable-static \
    LDFLAGS=-L/usr/lib/oracle/19.5/client64/lib/ \
    CPPFLAGS=-I/usr/include/oracle/19.5/client64/ \
    LD_LIBRARY_PATH=/usr/lib/oracle/19.5/client64/lib/
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%{_libdir}/libodpic-%{version}.so

%files devel
%doc NEWS
# odb folder is created/owned by libodb package
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/libodpic.pc


%changelog
* Mon Feb 03 2020 Soroush Rabiei <soroush@tidm.ir> 3.3.0-1
- Add buildsystem and packaging
