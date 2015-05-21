
Name:			geneet
Version:		76262
Release:		0.1
Summary:	Generator for EFL's pickler/unpickler library, EET
License:	BSD
Group:		Development/Utilities
URL:		https://git.enlightenment.org/tools/geneet.git/
Source0:	%{name}-%{version}.tar.xz

BuildRequires:	pkgconfig(python2)

Requires:	python
BuildRequires:  python-distribute
Requires:       python-pyparsing
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Given a simple description about a data structure, geneet will
generate the C source code so it can be serialized/deserialized
by using the EET library

%prep
%setup -q -n %{name}-%{version}

%build
python setup.py build

%install
#rm -rf %{buildroot}
python setup.py install --prefix=%{_prefix} --root=%{buildroot}

#rm -f %{buildroot}%{py_puresitedir}/%{name}-%{version}*


%clean
rm -rf %{buildroot}


#%files -f %{name}.lang
%defattr(-,root,root,-)
#%doc doc/*
%{_bindir}/*


#%{_datadir}/applications/*
#%{_datadir}/pixmaps/*
