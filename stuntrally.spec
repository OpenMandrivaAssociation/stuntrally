%define		sname StuntRally

Name:		stuntrally
Summary:	Racing game with Track Editor, based on VDrift and OGRE
Version:	1.4
Release:	%mkrel 1
License:	GPLv3
Group:		Games/Arcade
URL:		http://code.google.com/p/vdrift-ogre/
Source0:	http://sourceforge.net/projects/stuntrally/files/%{version}/%{sname}-%{version}-sources.tar.bz2
BuildRequires:	cmake
BuildRequires:	mygui-devel >= 3.2
BuildRequires:	libogg-devel
BuildRequires:	libuuid-devel
BuildRequires:	libvorbis-devel
BuildRequires:	ogre-devel
BuildRequires:	ois-devel
BuildRequires:	SDL-devel
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
%setup -q -n %{name}

%build
%cmake
%make

%install
%__rm -rf %{buildroot}

%makeinstall_std -C build

%__install -d %{buildroot}%{_gamesbindir}
%__mv %{buildroot}%{_bindir}/%{name} %{buildroot}%{_gamesbindir}/
%__mv %{buildroot}%{_bindir}/sr-editor %{buildroot}%{_gamesbindir}/

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Readme.txt License.txt
%{_gamesbindir}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/sr-editor.desktop
%{_gamesdatadir}/%{name}
%{_iconsdir}/hicolor/*/apps/%{name}.png

