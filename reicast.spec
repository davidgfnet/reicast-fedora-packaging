%global appname %{name}

Name:       reicast
Version:    8.1
Release:    1%{?dist}
Summary:    Multiplaform Dreamcast emulator
License:    GPLv2
URL:        https://reicast.com
Source0:    https://github.com/reicast/reicast-emulator/archive/r%{version}.tar.gz

# It can run on ARM and potentially any platform without JIT though.
ExclusiveArch:	x86_64 i686

BuildRequires: bash
BuildRequires: gcc-c++
BuildRequires: gcc
BuildRequires: make
BuildRequires: libX11-devel
BuildRequires: alsa-lib-devel
BuildRequires: mesa-libGL-devel

%description
Reicast is a Sega Dreamcast emulator. It's an app that allows you to play your Dreamcast games on your computer or android phone. We've even baked in some magic to make things looks prettier than they did on the Dreamcast. Of course, not all games work, and the ones that do often have glitches

Reicast primarily aims for speed and to run on android. It is derived from the nullDC codebase. We work on it in our spare time, because we love working on complicated, headache-inducing projects. Development traces back to late 2003 and has been largely non-continuous.

Naturally, there are many other Dreamcast emulation projects, each with its own goals and priorities. Here's a non-exaustive list: Makaron, Demul, Redream, nullDC. If Reicast doesn't work for you, you may want to check these out.

%prep
%setup -qn reicast-emulator-r%{version}

%build
# Patch joystick tool, seems it is ambiguous about python version
sed -i 's/\/usr\/bin\/env python/\/usr\/bin\/python3/g' shell/linux/tools/reicast-joyconfig.py
cd shell/linux && %make_build

%install
cd shell/linux && %make_install PREFIX=%{_prefix}

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/reicast.desktop

%files
%{_bindir}/%{name}
%{_bindir}/%{name}-joyconfig
%{_datadir}/%{name}
%{_mandir}/man1/reicast.1.*
%{_mandir}/man1/reicast-joyconfig.1.*
%{_datadir}/applications/reicast.desktop
%{_datadir}/pixmaps/reicast.png

%changelog
* Thu May 09 18:00:00 CEST 2019 David Guillen Fandos <david@davidgf.net> - 8.1-1
- First Fedora released based on reicast-r8.1 version (1a09ccb)

