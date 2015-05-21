
Name:			geneet
Version:		76262
Release:		1
Summary:	Generator for EFL's pickler/unpickler library, EET
License:	BSD
Group:		Graphical desktop/Enlightenment
URL:		https://git.enlightenment.org/tools/geneet.git/
Source0:	%{name}-%{version}.tar.xz
Source100:	%{name}.rpmlintrc
BuildRequires:	pkgconfig(python2)
BuildRequires:  python-distribute
Requires:       python-parsing
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-build

%description
Given a simple description about a data structure, geneet will
generate the C source code so it can be serialized/deserialized
by using the EET library

%prep
%setup -q -n %{name}-%{version}

%build
python setup.py build

%install
python setup.py install --prefix=%{_prefix} --root=%{buildroot}

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root)
%{_bindir}/*
%{python_sitelib}/*

