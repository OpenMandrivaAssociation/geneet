
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

Requires:	python
BuildRequires:  python-distribute
Requires:       python-pyparsing
#Below is broken enable and only src file will be built
#BuildArch:	noarch
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
#python setup.py install --root=%{buildroot}
#rm -f %{buildroot}%{py_puresitedir}/%{name}-%{version}*


%clean
rm -rf %{buildroot}


#%files -f %{name}.lang
%defattr(-,root,root,-)
#%doc doc/*
%{_bindir}/*


#%{_datadir}/applications/*
#%{_datadir}/pixmaps/*
