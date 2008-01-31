%include	/usr/lib/rpm/macros.php
%define		_class		Image
%define		_subclass	Barcode
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - render barcodes
Summary(pl.UTF-8):	%{_pearname} - rysowanie kodów kreskowych
Name:		php-pear-%{_pearname}
Version:	1.1.0
Release:	2
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	6fb0c657f71a75331be9c4b4310d07ae
URL:		http://pear.php.net/package/Image_Barcode/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php(gd)
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	'pear(PHP/Compat.*)'

%description
With PEAR::Image_Barcode class you can create a barcode representation
of description a given string. This class uses GD functions because of
this the generated graphic can be any of GD supported supported image
types.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Przy pomocy klasy PEAR::Image_Barcode można tworzyć reprezentację
danego łańcucha w postaci kodu kreskowego. Ta klasa używa funkcji GD,
dzięki czemu generowana grafika może być w dowolnym formacie
obsługiwanym przez GD.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f %{_docdir}/%{name}-%{version}/optional-packages.txt ]; then
	cat %{_docdir}/%{name}-%{version}/optional-packages.txt
fi

%files
%defattr(644,root,root,755)
%doc install.log optional-packages.txt
%doc docs/%{_pearname}/docs/*
%{php_pear_dir}/.registry/*.reg
%dir %{php_pear_dir}/%{_class}/%{_subclass}
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/*.php
