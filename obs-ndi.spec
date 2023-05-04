Name:           obs-ndi
Version:        4.11.1
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
# A libndi.so.5 implementation is meant to be dlopen
Requires: ndi-sdk%{?isa}

%description
* NDI Source : receive NDI video and audio in OBS
* NDI Output : transmit video and audio from OBS to NDI
* NDI Filter (a.k.a NDI Dedicated Output) : transmit a single source or
scene to NDI


%prep
%autosetup -p1

# Where to find the libndi.so.5 library
sed -i -e 's|/usr/lib|%{_libdir}|' src/obs-ndi.cpp
sed -i -e 's|/usr/local/lib|/usr/local/%{_lib}|' src/obs-ndi.cpp


%build
%cmake \
  -DLINUX_PORTABLE=off

%cmake_build


%install
%cmake_install


%files
%license LICENSE
%doc README.md
%{_libdir}/obs-plugins/obs-ndi.so
%{_datadir}/obs/obs-plugins/obs-ndi


%changelog
* Thu May 04 2023 Nicolas Chauvet <kwizart@gmail.com> - 4.11.1-1
- Update to 4.11.1

* Mon Aug 08 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 4.9.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Wed Feb 16 2022 Nicolas Chauvet <kwizart@gmail.com> - 4.9.1-5
- rebuilt

* Thu Feb 10 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 4.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Aug 04 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 4.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Mar 21 2021 Nicolas Chauvet <kwizart@gmail.com> - 4.9.1-2
- Don't enforce c++11

* Wed Feb 24 2021 Nicolas Chauvet <kwizart@gmail.com> - 4.9.1-1
- Initial spec file
