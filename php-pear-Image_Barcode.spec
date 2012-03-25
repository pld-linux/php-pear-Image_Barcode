%define		status		stable
%define		pearname	Image_Barcode
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - render barcodes
Summary(pl.UTF-8):	%{pearname} - rysowanie kodów kreskowych
Name:		php-pear-%{pearname}
Version:	1.1.3
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{pearname}-%{version}.tgz
# Source0-md5:	8df93161d954c6a2bc0fc2bbce02c208
URL:		http://pear.php.net/package/Image_Barcode/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.580
Requires:	php-gd
Requires:	php-pear
Suggests:	php-pear-PHP_Compat
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	pear(PHP/Compat.*)

%description
With PEAR::Image_Barcode class you can create a barcode representation
of description a given string. This class uses GD functions because of
this the generated graphic can be any of GD supported supported image
types.

In PEAR status of this package is: %{status}.

%description -l pl.UTF-8
Przy pomocy klasy PEAR::Image_Barcode można tworzyć reprezentację
danego łańcucha w postaci kodu kreskowego. Ta klasa używa funkcji GD,
dzięki czemu generowana grafika może być w dowolnym formacie
obsługiwanym przez GD.

Ta klasa ma w PEAR status: %{status}.

%prep
%pear_package_setup

mv .%{php_pear_dir}/data/Image_Barcode/README .
mv docs/%{pearname}/docs/examples .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f %{_docdir}/%{name}-%{version}/optional-packages.txt ]; then
	cat %{_docdir}/%{name}-%{version}/optional-packages.txt
fi

%files
%defattr(644,root,root,755)
%doc README
%doc install.log optional-packages.txt
%doc docs/%{pearname}/docs/*
%{php_pear_dir}/.registry/*.reg
%dir %{php_pear_dir}/Image/Barcode
%{php_pear_dir}/Image/*.php
%{php_pear_dir}/Image/Barcode/*.php
%{_examplesdir}/%{name}-%{version}
