%{!?directory:%define directory /usr}

Summary:	Tcl interface to the Apache Kafka distributed messaging system
Name:		kafkatcl
Version:	2.4.3
Release:	1
License:	BSD-3-Clause
Group:		Development/Languages/Tcl
Source0:	https://github.com/flightaware/kafkatcl/releases/%{name}-%{version}.tar.gz
URL:		https://github.com/flightaware/kafkatcl
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	librdkafka-devel >= 0.9.0
BuildRequires:	tcl-devel >= 8.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KafkaTcl provides a Tcl interface to the Kafka C language API "librdkafka".

%prep
%setup -q

%build
%{__autoconf}
%configure --with-tcl=/usr/lib64 --prefix=%{directory} \
	       --exec-prefix=%{directory} \
           --libdir=%tcl_archdir

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
    pkglibdir=%{directory}/%{_lib}/tcl/%{name}%{version} \
	DESTDIR="$RPM_BUILD_ROOT"

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%{directory}/%{_lib}/tcl/%{name}%{version}

