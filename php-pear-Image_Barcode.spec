%include	/usr/lib/rpm/macros.php
%define		_class		Image
%define		_subclass	Barcode
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - render barcodes
Summary(pl):	%{_pearname} - rysowanie kodów kreskowych
Name:		php-pear-%{_pearname}
Version:	1.0.1
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	eb7aee7fd64a2cc344c449d6eccbe5b0
URL:		http://pear.php.net/package/Image_Barcode/
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

In PEAR status of this package is: %{_status}.

%description -l pl
Przy pomocy klasy PEAR::Image_Barcode mo¿na tworzyæ reprezentacjê
danego ³añcucha w postaci kodu kreskowego. Ta klasa u¿ywa funkcji GD,
dziêki czemu generowana grafika mo¿e byæ w dowolnym formacie
obs³ugiwanym przez GD.

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
