Summary:	S/Key suite of programs
Name:		skey
Version:	2.2
Release:	4
License:	GPL
Group:		Networking/Daemons
Group(de):	Netzwerkwesen/Server
Group(pl):	Sieciowe/Serwery
Source0:	ftp://sunsite.unc.edu/pub/Linux/system/security/%{name}-%{version}.tar.gz
Patch0:		%{name}-shared.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The S/Key suite of programs.

S/Key provides one-time password-based authentication using the RSA
Data Security, Inc. MD5 Message-Digest Algorithm (licensed for
redistribution by RSA). This technology is based on key-challenge
authentication via key checksums and does not contain any
strong-encryption algorithms. This code may be exported freely out of
the United States.

%package devel
Summary:	libraries and headers for developing S/Key enabled programs
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Libraries and headers for developing S/Key enabled programs.

%package static
Summary:	static S/Key libraries
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}


%description static
Static S/Key libraries.

%prep
%setup -q
%patch -p1

%build
%{__make} CFLAGS="%{?debug:-O0 -g}%{!?debug:$RPM_OPT_FLAGS}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{%{_bindir},%{_mandir}/man{1,5},%{_libdir},%{_includedir}/security}

install key/key keyinit/keyinit keyinfo/keyinfo $RPM_BUILD_ROOT%{_bindir}
install libskey/skey.h $RPM_BUILD_ROOT%{_includedir}/security
install libskey/libskey.a $RPM_BUILD_ROOT%{_libdir}
install libskey/libskey.so.*.* $RPM_BUILD_ROOT%{_libdir}

ln -s libskey.so.%{version} $RPM_BUILD_ROOT/%{_libdir}/libskey.so

install {key,keyinfo,keyinit,libskey}/*.1 $RPM_BUILD_ROOT%{_mandir}/man1/
install libskey/*.5 $RPM_BUILD_ROOT%{_mandir}/man5/

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_mandir}/man1/*
%{_mandir}/man5/*

%files devel
%defattr(644,root,root,755)
%{_includedir}/security/skey.h
%attr(755,root,root) %{_libdir}/lib*.so

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
