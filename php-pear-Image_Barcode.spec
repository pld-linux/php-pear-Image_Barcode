%include	/usr/lib/rpm/macros.php
%define		_class		Image
%define		_subclass	Barcode
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - render barcodes
Summary(pl):	%{_pearname} - rysowanie kodów kreskowych
Name:		php-pear-%{_pearname}
Version:	1.0.4
Release:	2
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	f029193037c9e0942f03440217bc676b
URL:		http://pear.php.net/package/Image_Barcode/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-gd
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

%description -l pl
Przy pomocy klasy PEAR::Image_Barcode mo¿na tworzyæ reprezentacjê
danego ³añcucha w postaci kodu kreskowego. Ta klasa u¿ywa funkcji GD,
dziêki czemu generowana grafika mo¿e byæ w dowolnym formacie
obs³ugiwanym przez GD.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup
install -d docs/%{_pearname}
mv ./%{php_pear_dir}/Image/docs/examples docs/%{_pearname}

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
%doc docs/%{_pearname}/examples
%{php_pear_dir}/.registry/*.reg
%dir %{php_pear_dir}/%{_class}/%{_subclass}
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/*.php
