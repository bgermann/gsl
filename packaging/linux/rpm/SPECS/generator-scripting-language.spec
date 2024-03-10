%define revision 0
%undefine _debugsource_packages

Summary:	imatix GSL is a code construction tool
Name:		generator-scripting-language
Version:	4.1.5
Release:	%{revision}%{?dist}
License:	GPL-3.0-or-later
Group:		Libraries
Source0:	http://download.zeromq.org/%{name}-%{version}.tar.gz
URL:		http://zeromq.org/
BuildRequires:	pcre-devel

BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GSL/4.1 is a code construction tool. It will generate code in all languages
and for all purposes. If this sounds too good to be true, welcome to 1996,
when we invented these techniques. Magic is simply technology that is twenty
years ahead of its time. In addition to code construction, GSL has been used
to generate database schema definitions, user interfaces, reports, system
administration tools and much more.

%prep
%setup -q -n %{name}-%{version}
%build
make %{?_smp_mflags}
%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT PREFIX=/usr
%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/denormalizing.md
%doc doc/denormalizing.txt
%doc doc/modules/*
%doc README.md
%doc README.txt
%{_mandir}/man1/*
%attr(755,root,root) %{_bindir}/gsl

%package -n %{name}-examples
Summary:        imatix GSL is a code construction tool
Requires:       %{name} = %{version}

%description -n %{name}-examples
This package contains examples to get started with gsl.

%files -n %{name}-examples
%defattr(-,root,root)
%doc examples/*
%doc doc/examples/*

%changelog
* Wed Dec 31 2014 GSL Developers <zeromq-dev@lists.zeromq.org
- Initial packaging.
