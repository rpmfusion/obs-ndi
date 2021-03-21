Name:           obs-ndi
Version:        4.9.1
Release:        1%{?dist}
Summary:        Network A/V in OBS Studio with NewTek's NDI technology

License:        GPLv2+
URL:            https://github.com/Palakis/obs-ndi
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

ExclusiveArch:  i686 x86_64 armv7hl

BuildRequires:  cmake
BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  obs-studio-devel
Requires:       obs-studio
# A libndi.so.4 implementation is meant to be dlopen
Requires: ndi-sdk%{?isa}

%description
* NDI Source : receive NDI video and audio in OBS
* NDI Output : transmit video and audio from OBS to NDI
* NDI Filter (a.k.a NDI Dedicated Output) : transmit a single source or
scene to NDI


%prep
%autosetup -p1

# Where to find the libndi.so.4 library
sed -i -e 's|/usr/lib|%{_libdir}|' src/obs-ndi.cpp

# Remove tuning
sed -i -e 's/-mtune=core2 -Ofast//' CMakeLists.txt


%build
%cmake

%cmake_build


%install
%cmake_install


%files
%license LICENSE
%doc README.md
%{_libdir}/obs-plugins/obs-ndi.so
%{_datadir}/obs/obs-plugins/obs-ndi


%changelog
* Wed Feb 24 2021 Nicolas Chauvet <kwizart@gmail.com> - 4.9.1-1
- Initial spec file
