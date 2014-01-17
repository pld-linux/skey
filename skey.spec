Summary:	S/Key suite of programs
Summary(pl.UTF-8):	Zestaw programów do S/Key
Name:		skey
Version:	2.2
Release:	15
License:	GPL
Group:		Base/Authentication and Authorization
Source0:	ftp://sunsite.unc.edu/pub/Linux/system/security/%{name}-%{version}.tar.gz
# Source0-md5:	c6ac90d37ac4b847e96a0a9ea8f34a6e
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

%description -l pl.UTF-8
Zestaw programów do S/Key.

S/Key daje system autentykacji bazujący na hasłach jednorazowych przy
użyciu algorytmu skrótu MD5 RSA Data Security. Ta technologia bazuje
na autentykacji key-challenge poprzez sumy kontrolne kluczy i nie
zawiera silnej kryptografii - tak więc kod może być eksportowany poza
USA.

%package devel
Summary:	Headers for developing S/Key enabled programs
Summary(pl.UTF-8):	Pliki nagłówkowe do tworzenia programów używających S/Key
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	filesystem >= 3.0-11

%description devel
Headers for developing S/Key enabled programs.

%description devel -l pl.UTF-8
Pliki nagłówkowe do tworzenia programów używających S/Key.

%package static
Summary:	Static S/Key libraries
Summary(pl.UTF-8):	Statyczne biblioteki S/Key
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static S/Key libraries.

%description static -l pl.UTF-8
Statyczne biblioteki S/Key.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man{1,5},%{_libdir},%{_includedir}/security}

install key/key keyinit/keyinit keyinfo/keyinfo $RPM_BUILD_ROOT%{_bindir}
install libskey/skey.h $RPM_BUILD_ROOT%{_includedir}/security
install libskey/libskey.a $RPM_BUILD_ROOT%{_libdir}
install libskey/libskey.so.*.* $RPM_BUILD_ROOT%{_libdir}

ln -sf libskey.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libskey.so
ln -sf libskey.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libskey.so.2

install {key,keyinfo,keyinit,libskey}/*.1 $RPM_BUILD_ROOT%{_mandir}/man1
install libskey/*.5 $RPM_BUILD_ROOT%{_mandir}/man5

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%attr(755,root,root) %ghost %{_libdir}/lib*.so.2
%{_mandir}/man1/*
%{_mandir}/man5/*

%files devel
%defattr(644,root,root,755)
%{_includedir}/security/skey.h
%attr(755,root,root) %{_libdir}/lib*.so

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
