Name:          hello
Version:       0.1
Release:       1
Summary:       hello
License:       GPL
URL:           https://github.com
Distribution:  Tizen
Vendor:        Private
Source0:       %{name}-%{version}.tar.gz

BuildRequires:  python
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  pkgconfig(tensorflow)

%description
hello world example

%prep
%setup -q

%build
%cmake . -DCMAKE_INSTALL_PREFIX=%{_prefix}
make

%install
rm -rf %{buildroot}
%make_install

%files
%{_bindir}/hello
