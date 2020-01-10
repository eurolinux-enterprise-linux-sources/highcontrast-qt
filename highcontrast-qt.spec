Name:           highcontrast-qt
Version:        0.1
Release:        2%{?dist}
License:        GPLv2+ and MIT
Summary:        HighContrast theme for Qt-based applications

Url:            https://github.com/MartinBriza/highcontrast-qt
Source0:        https://github.com/MartinBriza/highcontrast-qt/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  qt4-devel
BuildRequires:  qt5-qtbase-devel

Requires:       highcontrast-qt5

%description
Theme to let Qt applications fit nicely into the GNOME desktop


%package -n highcontrast-qt4
Summary:        HighContrast Qt4 theme
Requires:       qt5-qtbase

%package -n highcontrast-qt5
Summary:        HighContrast Qt5 theme
Requires:       qt5-qtbase


%description -n highcontrast-qt4
HighContrast theme variant for applications utilizing Qt4

%description -n highcontrast-qt5
HighContrast theme variant for applications utilizing Qt5


%prep
%setup -q -n %{name}-%{version}


%build
mkdir -p "%{_target_platform}-qt4"
pushd "%{_target_platform}-qt4"
%{cmake} -DUSE_QT4=true ..
popd

mkdir -p "%{_target_platform}-qt5"
pushd "%{_target_platform}-qt5"
%{cmake} ..
popd

make %{?_smp_mflags} -C "%{_target_platform}-qt4"
make %{?_smp_mflags} -C "%{_target_platform}-qt5"


%install
make install/fast DESTDIR=%{buildroot} -C "%{_target_platform}-qt4"
make install/fast DESTDIR=%{buildroot} -C "%{_target_platform}-qt5"


%files -n highcontrast-qt4
%license LICENSE.GPL2
%doc README.md
%{_qt4_plugindir}/styles/highcontrast.so

%files -n highcontrast-qt5
%license LICENSE.GPL2
%doc README.md
%{_qt5_plugindir}/styles/highcontrast.so

%files

%changelog
* Wed Oct 11 2017 Martin Bříza <mbriza@redhat.com> - 0.1-2
- Fix trademark

* Thu Jan 05 2017 Martin Briza <mbriza@redhat.com> - 0.1-1
- Initial build
- Resolves: #1479347
