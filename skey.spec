Summary:	S/Key suite of programs
Name:		skey
Version:	2.2
Release:	1
Copyright:	GPL
Group:		Libraries
Source:		%{name}-%{version}.tar.gz
Patch:		skey-shared.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The S/Key suite of programs.

S/Key provides one-time password-based authentication using the 
RSA Data Security, Inc. MD5 Message-Digest Algorithm (licensed for 
redistribution by RSA). This technology is based on key-challenge
authentication via key checksums and does not contain any strong-encryption 
algorithms. This code may be exported freely out of the United States.

%package devel
Summary:	libraries and headers for developing S/Key enabled programs
Group:		Development/Libraries

%description devel
Libraries and headers for developing S/Key enabled programs.

%prep
%setup -q
%patch -p1

%build
make CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/{%{_bindir},%{_mandir}/man{1,5},%{_libdir},%{_includedir}/security}

install -s key/key   $RPM_BUILD_ROOT/%{_bindir}
install -s keyinit/keyinit   $RPM_BUILD_ROOT/%{_bindir}
install keyinfo/keyinfo $RPM_BUILD_ROOT/%{_bindir}
install libskey/skey.h $RPM_BUILD_ROOT/%{_includedir}/security
install libskey/libskey.a $RPM_BUILD_ROOT/%{_libdir}
install -s libskey/libskey.so.%{version} $RPM_BUILD_ROOT/%{_libdir}

ln -s libskey.so.%{version} $RPM_BUILD_ROOT/%{_libdir}/libskey.so

install -m644 key/*.1 $RPM_BUILD_ROOT/%{_mandir}/man1/
install -m644 keyinfo/*.1 $RPM_BUILD_ROOT/%{_mandir}/man1/
install -m644 keyinit/*.1 $RPM_BUILD_ROOT/%{_mandir}/man1/
install -m644 libskey/*.1 $RPM_BUILD_ROOT/%{_mandir}/man1/
install -m644 libskey/*.5 $RPM_BUILD_ROOT/%{_mandir}/man5/

gzip -9nf $RPM_BUILD_ROOT/%{_mandir}/man{1,5}/*

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%attr(755, root, root) %{_bindir}/key
%attr(755, root, root) %{_bindir}/keyinfo
%attr(755, root, root) %{_bindir}/keyinit
%attr(755, root, root) %{_libdir}/lib*.so.*.*
%{_mandir}/man1/*
%{_mandir}/man5/*

%files devel
%defattr(644, root, root, 755)
%{_includedir}/security/skey.h
%{_libdir}/lib*.so
%{_libdir}/lib*.a
