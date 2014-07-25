Name:			libzorpll
Version:		5.0
Release:		1
URL:			https://www.balabit.com/network-security/zorp-gpl
#Source0:		https://www.balabit.com/downloads/files/zorp/5.0.0/source/libzorpll_5.0.0.0.tar.gz
Source0:		libzorpll_%{version}.0.0.tar.gz
#Patch0:			createdir.patch
Summary:		BalaBit Zorp proxy firewall low level library
License:		GPL-2.0
Group:			System/Daemons
BuildRequires:		libcap-devel
BuildRequires:		glib2-devel
BuildRequires:		zlib-devel
BuildRequires:		binutils-devel
BuildRequires:		automake
BuildRequires:		autoconf
BuildRequires:		gcc-c++


%if 0%{?fedora} || 0%{?centos}
BuildRequires:		openssl-devel
%else
BuildRequires:		libopenssl-devel
%endif


BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
BalaBit Zorp is a proxy based firewall

%package devel
Summary:		Headers for libzorpll
Group:			System/Daemons
Requires:		zlib-devel
Requires:		glibc-devel
Requires:		libcap-devel
Requires:		glib2-devel
Requires:		binutils-devel
Requires:		%{name} = %{version}

%if 0%{?fedora} || 0%{?centos}
Requires:		openssl-devel
%else
Requires:		libopenssl-devel
%endif


%description devel
This package provides header files for libzorpll

%prep
%setup -q -n libzorpll
# %patch0 -p1

%build
#./autogen.sh
#%{?suse_update_config:%{suse_update_config -f config}}
%configure --disable-werror --enable-debug

%install
make DESTDIR=${RPM_BUILD_ROOT} install
%if 0%{?fedora} || 0%{?centos}
rm %{buildroot}/usr/libexec/failure_notify5.0-0
%else
rm %{buildroot}/usr/lib/failure_notify5.0-0
%endif

%post
ldconfig

%postun
ldconfig

%files
%attr(755,root,root) %{_libdir}/libzorpll-*

%files devel
%dir %attr(755,root,root) /usr/include/zorp
%attr(664,root,root) /usr/include/zorp/*
%attr(664,root,root) %{_libdir}/pkgconfig/zorplibll.pc
%attr(664,root,root) %{_libdir}/libzorpll.*


%changelog
