#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xC1A60EACE707FDA5 (wl@gnu.org)
#
Name     : freetype
Version  : 2.7.1
Release  : 33
URL      : http://savannah.spinellicreations.com/freetype/freetype-2.7.1.tar.gz
Source0  : http://savannah.spinellicreations.com/freetype/freetype-2.7.1.tar.gz
Source99 : http://savannah.spinellicreations.com/freetype/freetype-2.7.1.tar.gz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : FTL GPL-2.0 GPL-2.0+ MIT Zlib
Requires: freetype-bin
Requires: freetype-lib
Requires: freetype-doc
BuildRequires : bzip2
BuildRequires : bzip2-dev
BuildRequires : cmake
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : harfbuzz-dev
BuildRequires : libpng-dev
BuildRequires : libpng-dev32
BuildRequires : zlib-dev32
Patch1: cve-2017-8105.patch

%description
FreeType 2.7.1
==============
Homepage: http://www.freetype.org
FreeType is a freely available software library to render fonts.

%package bin
Summary: bin components for the freetype package.
Group: Binaries

%description bin
bin components for the freetype package.


%package dev
Summary: dev components for the freetype package.
Group: Development
Requires: freetype-lib
Requires: freetype-bin
Provides: freetype-devel

%description dev
dev components for the freetype package.


%package dev32
Summary: dev32 components for the freetype package.
Group: Default
Requires: freetype-lib32
Requires: freetype-bin
Requires: freetype-dev

%description dev32
dev32 components for the freetype package.


%package doc
Summary: doc components for the freetype package.
Group: Documentation

%description doc
doc components for the freetype package.


%package lib
Summary: lib components for the freetype package.
Group: Libraries

%description lib
lib components for the freetype package.


%package lib32
Summary: lib32 components for the freetype package.
Group: Default

%description lib32
lib32 components for the freetype package.


%prep
%setup -q -n freetype-2.7.1
%patch1 -p1
pushd ..
cp -a freetype-2.7.1 build32
popd

%build
export LANG=C
export SOURCE_DATE_EPOCH=1493426347
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -fno-semantic-interposition "
%configure --disable-static
make V=1  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export CFLAGS="$CFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
export LDFLAGS="$LDFLAGS -m32"
%configure --disable-static  --with-harfbuzz=no  --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make V=1  %{?_smp_mflags}
popd
%install
export SOURCE_DATE_EPOCH=1493426347
rm -rf %{buildroot}
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/freetype-config

%files dev
%defattr(-,root,root,-)
/usr/include/freetype2/freetype/config/ftconfig.h
/usr/include/freetype2/freetype/config/ftheader.h
/usr/include/freetype2/freetype/config/ftmodule.h
/usr/include/freetype2/freetype/config/ftoption.h
/usr/include/freetype2/freetype/config/ftstdlib.h
/usr/include/freetype2/freetype/freetype.h
/usr/include/freetype2/freetype/ftadvanc.h
/usr/include/freetype2/freetype/ftautoh.h
/usr/include/freetype2/freetype/ftbbox.h
/usr/include/freetype2/freetype/ftbdf.h
/usr/include/freetype2/freetype/ftbitmap.h
/usr/include/freetype2/freetype/ftbzip2.h
/usr/include/freetype2/freetype/ftcache.h
/usr/include/freetype2/freetype/ftcffdrv.h
/usr/include/freetype2/freetype/ftchapters.h
/usr/include/freetype2/freetype/ftcid.h
/usr/include/freetype2/freetype/fterrdef.h
/usr/include/freetype2/freetype/fterrors.h
/usr/include/freetype2/freetype/ftfntfmt.h
/usr/include/freetype2/freetype/ftgasp.h
/usr/include/freetype2/freetype/ftglyph.h
/usr/include/freetype2/freetype/ftgxval.h
/usr/include/freetype2/freetype/ftgzip.h
/usr/include/freetype2/freetype/ftimage.h
/usr/include/freetype2/freetype/ftincrem.h
/usr/include/freetype2/freetype/ftlcdfil.h
/usr/include/freetype2/freetype/ftlist.h
/usr/include/freetype2/freetype/ftlzw.h
/usr/include/freetype2/freetype/ftmac.h
/usr/include/freetype2/freetype/ftmm.h
/usr/include/freetype2/freetype/ftmodapi.h
/usr/include/freetype2/freetype/ftmoderr.h
/usr/include/freetype2/freetype/ftotval.h
/usr/include/freetype2/freetype/ftoutln.h
/usr/include/freetype2/freetype/ftpfr.h
/usr/include/freetype2/freetype/ftrender.h
/usr/include/freetype2/freetype/ftsizes.h
/usr/include/freetype2/freetype/ftsnames.h
/usr/include/freetype2/freetype/ftstroke.h
/usr/include/freetype2/freetype/ftsynth.h
/usr/include/freetype2/freetype/ftsystem.h
/usr/include/freetype2/freetype/fttrigon.h
/usr/include/freetype2/freetype/ftttdrv.h
/usr/include/freetype2/freetype/fttypes.h
/usr/include/freetype2/freetype/ftwinfnt.h
/usr/include/freetype2/freetype/t1tables.h
/usr/include/freetype2/freetype/ttnameid.h
/usr/include/freetype2/freetype/tttables.h
/usr/include/freetype2/freetype/tttags.h
/usr/include/freetype2/freetype/ttunpat.h
/usr/include/freetype2/ft2build.h
/usr/lib64/libfreetype.so
/usr/lib64/pkgconfig/freetype2.pc
/usr/share/aclocal/*.m4

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libfreetype.so
/usr/lib32/pkgconfig/32freetype2.pc
/usr/lib32/pkgconfig/freetype2.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libfreetype.so.6
/usr/lib64/libfreetype.so.6.13.0

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libfreetype.so.6
/usr/lib32/libfreetype.so.6.13.0
