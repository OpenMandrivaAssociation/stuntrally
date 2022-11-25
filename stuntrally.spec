Summary:	Racing game with Track Editor, based on VDrift and OGRE
Name:		stuntrally
Version:	2.7
Release:	2
License:	GPLv3+
Group:		Games/Arcade
URL:            https://stuntrally.tuxfamily.org
Source0:        https://github.com/stuntrally/stuntrally/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        https://github.com/stuntrally/tracks/archive/%{version}/tracks-%{version}.tar.gz

BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:  boost-devel
BuildRequires:  ogre
BuildRequires:  ogre-samples
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
BuildRequires:  pkgconfig(tinyxml)
BuildRequires:  pkgconfig(tinyxml2)
BuildRequires:	pkgconfig(xcursor)

Requires:	ogre
Requires: %{name}-data = %{version}-%{release}

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

pushd data
rm -rf tracks
tar xf %{SOURCE1}
mv tracks-%{version} tracks
popd

# /usr/include/OGRE/OgreException.h:311:120: error: invalid conversion from
# 'int' to 'Ogre::Exception::ExceptionCodes' [-fpermissive]
#export CXXFLAGS="%{optflags} -fpermissive"
%cmake -DBUILD_SHARED_LIBS=OFF -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%{_bindir}/%{name}
%{_bindir}/sr-editor
%{_bindir}/sr-translator
%{_datadir}/applications/*.desktop
%{_iconsdir}/hicolor/*/apps/*.png

%files          data
%{_gamesdatadir}/%{name}/
