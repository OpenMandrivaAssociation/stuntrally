%define		sname StuntRally

Name:		stuntrally
Summary:	Racing game with Track Editor, based on VDrift and OGRE
Version:	1.4
Release:	%mkrel 1
License:	GPLv3
Group:		Games/Arcade
URL:		http://code.google.com/p/vdrift-ogre/
Source0:	http://sourceforge.net/projects/stuntrally/files/1.3/%{sname}-%{version}-sources.tar.bz2
BuildRequires:	cmake
BuildRequires:	libmygui-devel
BuildRequires:	libogg-devel
BuildRequires:	libuuid-devel
BuildRequires:	libvorbis-devel
BuildRequires:	ogre-devel
BuildRequires:	ois-devel
BuildRequires:	SDL-devel
Requires:	ogre
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Rally game with Stunt elements, based on VDrift and OGRE.
The game features 49 tracks in 6 sceneries, 7 cars and a Track Editor.
It focuses on closed rally tracks with possible stunt elements (jumps,
loops, pipes).

%prep
%setup -q -n %{name}

%build
%cmake
%make

%install
rm -rf %{buildroot}

%makeinstall_std -C build

install -d %{buildroot}%{_gamesbindir}
mv %{buildroot}%{_bindir}/%{name} %{buildroot}%{_gamesbindir}/
mv %{buildroot}%{_bindir}/sr-editor %{buildroot}%{_gamesbindir}/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Readme.txt License.txt
%{_gamesbindir}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/sr-editor.desktop
%{_gamesdatadir}/%{name}
%{_iconsdir}/hicolor/*/apps/%{name}.png

