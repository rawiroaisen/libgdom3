Name:		libgdom3
Version:	0.0.1
Release:	1%{?dist}
Summary:	GLib Implementation of DOM3. Written in Vala.

Group:		Development
License:	LGPL
URL:		http://libgdom3.googlecode.com
Source0:	http://libgdom3.googlecode.com/files/libgdom3-%{version}.tar.gz

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	glib2-devel
Requires:	glib2

%description
libgdom3 is the (incomplete) GLib implementaion of DOM3. It is written in Vala.

%package devel
Summary: development headers and documentation for libgdom3
Group:		Development
Requires: glib2-devel
%description devel
Development headers and documentation for libgdom3.

%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%{_libdir}/libgdom3-0.0.1.so.0
%{_libdir}/libgdom3-0.0.1.so.0.0.0
%{_libdir}/libgdom3.so

%files devel
%defattr(-,root,root,-)
%{_includedir}/gdom3-1.0
%{_libdir}/pkgconfig
%{_libdir}/libgdom3.la
%{_datadir}/vala/vapi
%doc

%changelog

