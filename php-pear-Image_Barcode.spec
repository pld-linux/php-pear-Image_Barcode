%include	/usr/lib/rpm/macros.php
%define		_class		Image
%define		_subclass	Barcode
%define		_status		beta

%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - render barcodes
Summary(pl):	%{_pearname} - rysowanie kod�w kreskowych
Name:		php-pear-%{_pearname}
Version:	0.4
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
# Source0-md5:	f8281132f8c4a6273ca1595abd6ada93
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/package/%{_pearname}/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-gd
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
With PEAR::Image_Barcode class you can create a barcode representation
of description a given string. This class uses GD functions because of
this the generated graphic can be any of GD supported supported image
types.

This class has in PEAR status: %{_status}.

%description -l pl
Przy pomocy klasy PEAR::Image_Barcode mo�na tworzy� reprezentacj�
danego �a�cucha w postaci kodu kreskowego. Ta klasa u�ywa funkcji GD,
dzi�ki czemu generowana grafika mo�e by� w dowolnym formacie
obs�ugiwanym przez GD.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

install %{_pearname}-%{version}/%{_subclass}.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/
install %{_pearname}-%{version}/%{_subclass}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/{*.txt,ChangeLog,*test*.php,barcode_img.php}
%dir %{php_pear_dir}/%{_class}/%{_subclass}
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/*.php
