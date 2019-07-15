%undefine _hardened_build

Name: editline
Version: 1.16.1
Release: 1%{?dist}

Summary: A readline() replacement for UNIX without termcap (ncurses)

License: LGPLv2+
Group: Applications/System
Url: https://github.com/troglobit/editline
Source: https://github.com/troglobit/editline/releases/download/%{version}/editline-%{version}.tar.xz

BuildRequires: gcc-c++ 
BuildRequires: autoconf 
BuildRequires: make 
BuildRequires: libtool

%description
A readline() replacement for UNIX without termcap (ncurses).

%package        devel
Summary:        Development files for nix
Requires:       %{name} = %{version}-%{release}

%description   devel
Devel of editline

%prep
%autosetup -n %{name}-%{version} 

%build

%configure --enable-gc --disable-static

%make_build

%install
%make_install
rm -f %{buildroot}/%{_libdir}/*.la

%files
%{_libdir}/libeditline.so.1
%{_libdir}/libeditline.so.1.0.1

%{_docdir}/editline/LICENSE
%{_docdir}/editline/README.md
%{_mandir}/man3/editline.*.gz


%files devel
%{_includedir}/editline.h
%{_libdir}/pkgconfig/libeditline.pc
%{_libdir}/libeditline.so

%changelog

* Thu Jul 11 2019 David Va <davidva AT tuta DOT io> 1.16.1-1 
- Initial build
