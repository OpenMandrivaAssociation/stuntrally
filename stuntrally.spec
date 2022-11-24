Summary:	Racing game with Track Editor, based on VDrift and OGRE
Name:		stuntrally
Version:	2.7
Release:	1
License:	GPLv3+
Group:		Games/Arcade
URL:            https://stuntrally.tuxfamily.org
Source0:        https://github.com/stuntrally/stuntrally/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:	cmake
BuildRequires:  boost-devel
BuildRequires:  pkgconfig(bullet)
BuildRequires:	pkgconfig(libenet)
BuildRequires:	pkgconfig(MYGUI) >= 3.2
BuildRequires:	pkgconfig(ogg)
BuildRequires:  pkgconfig(openal)
BuildRequires:	pkgconfig(uuid)
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	pkgconfig(OGRE) >= 1.8.0
BuildRequires:	pkgconfig(OIS)
BuildRequires:	pkgconfig(sdl2)
BuildRequires:	pkgconfig(xcursor)

Requires:	ogre
Requires: %{name}-data = %{version}-%{release}
Requires: %{name}-tracks >= %{version}

# ogre-cg-plugin is in non-free
Suggests:	ogre-cg-plugin

%description
Rally game with Stunt elements, based on VDrift and OGRE.
The game features 49 tracks in 6 sceneries, 7 cars and a Track Editor.
It focuses on closed rally tracks with possible stunt elements (jumps,
loops, pipes).


%package        data
Summary:        Stunt Rally game with Track Editor, based on VDrift and OGRE
Group:          Games/Sports
BuildArch:      noarch

%description    data
Data files for Stunt Rally.


%prep
%autosetup -p1

%build
#export CC=gcc
#export CXX=g++

# /usr/include/OGRE/OgreException.h:311:120: error: invalid conversion from
# 'int' to 'Ogre::Exception::ExceptionCodes' [-fpermissive]
export CXXFLAGS="%{optflags} -fpermissive"
%cmake -DBUILD_SHARED_LIBS=OFF
%make_build

%install
%make_install -C build

%files
%doc Readme.txt
%{_gamesbindir}/%{name}
%{_gamesbindir}/sr-editor
%{_datadir}/applications/*.desktop
%{_iconsdir}/hicolor/64x64/apps/*.png

%files          data
%{_gamesdatadir}/%{name}/
