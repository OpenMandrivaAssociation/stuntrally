Name:		stuntrally
Summary:	Racing game with Track Editor, based on VDrift and OGRE
Version:	1.7
Release:	1
License:	GPLv3
Group:		Games/Arcade
URL:		http://code.google.com/p/vdrift-ogre/
# re-pack from git
# 1. https://github.com/stuntrally/stuntrally
# 2. https://github.com/stuntrally/tracks
Source0:	%{name}-%{version}.tar.xz
BuildRequires:	cmake
BuildRequires:	pkgconfig(libenet)
BuildRequires:	pkgconfig(MYGUI) >= 3.2
BuildRequires:	pkgconfig(ogg)
BuildRequires:	pkgconfig(uuid)
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	pkgconfig(OGRE) >= 1.8.0
BuildRequires:	pkgconfig(OIS)
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(xcursor)
Requires:	ogre
# ogre-cg-plugin is in non-free
Suggests:	ogre-cg-plugin

%description
Rally game with Stunt elements, based on VDrift and OGRE.
The game features 49 tracks in 6 sceneries, 7 cars and a Track Editor.
It focuses on closed rally tracks with possible stunt elements (jumps,
loops, pipes).

Warning! You need ogre-cg-plugin from Non-Free repository to run this game.

%prep
%setup -q

%build
%cmake
%make

%install
%makeinstall_std -C build

install -d %{buildroot}%{_gamesbindir}
mv %{buildroot}%{_bindir}/%{name} %{buildroot}%{_gamesbindir}/
mv %{buildroot}%{_bindir}/sr-editor %{buildroot}%{_gamesbindir}/

%files
%doc Readme.txt License.txt
%{_gamesbindir}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/sr-editor.desktop
%{_gamesdatadir}/%{name}
%{_iconsdir}/hicolor/*/apps/%{name}.png

%changelog
* Mon Jan 23 2012 Andrey Bondrov <abondrov@mandriva.org> 1.4-1mdv2012.0
+ Revision: 767224
- Add ogre-cg-plugin to Suggests (as we cannot Require stuff from non-free)
- Update BuildRequires (1.4 needs MyGUI 3.2)

  + Zombie Ryushu <ryushu@mandriva.org>
    - Upgrade to 1.4

* Thu Nov 17 2011 Andrey Bondrov <abondrov@mandriva.org> 1.3-1
+ Revision: 731411
- imported package stuntrally

