#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xC1A60EACE707FDA5 (wl@gnu.org)
#
Name     : freetype
Version  : 2.9.1
Release  : 47
URL      : https://download-mirror.savannah.gnu.org/releases/freetype/freetype-2.9.1.tar.gz
Source0  : https://download-mirror.savannah.gnu.org/releases/freetype/freetype-2.9.1.tar.gz
Source99 : https://download-mirror.savannah.gnu.org/releases/freetype/freetype-2.9.1.tar.gz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : FTL GPL-2.0 GPL-2.0+ MIT Zlib
Requires: freetype-lib = %{version}-%{release}
Requires: freetype-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : bzip2
BuildRequires : bzip2-dev
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : harfbuzz-dev
BuildRequires : libpng-dev
BuildRequires : libpng-dev32
BuildRequires : pkgconfig(32harfbuzz)
BuildRequires : pkgconfig(harfbuzz)
BuildRequires : zlib-dev
BuildRequires : zlib-dev32
Patch1: debuginfo.patch

%description
FreeType 2.9.1
==============
Homepage: https://www.freetype.org
FreeType is a freely available software library to render fonts.

%package dev
Summary: dev components for the freetype package.
Group: Development
Requires: freetype-lib = %{version}-%{release}
Provides: freetype-devel = %{version}-%{release}

%description dev
dev components for the freetype package.


%package dev32
Summary: dev32 components for the freetype package.
Group: Default
Requires: freetype-lib32 = %{version}-%{release}
Requires: freetype-dev = %{version}-%{release}

%description dev32
dev32 components for the freetype package.


%package lib
Summary: lib components for the freetype package.
Group: Libraries
Requires: freetype-license = %{version}-%{release}

%description lib
lib components for the freetype package.


%package lib32
Summary: lib32 components for the freetype package.
Group: Default
Requires: freetype-license = %{version}-%{release}

%description lib32
lib32 components for the freetype package.


%package license
Summary: license components for the freetype package.
Group: Default

%description license
license components for the freetype package.


%prep
%setup -q -n freetype-2.9.1
%patch1 -p1
pushd ..
cp -a freetype-2.9.1 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1547103189
mkdir -p clr-build
pushd clr-build
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -mzero-caller-saved-regs=used "
%cmake ..
make  %{?_smp_mflags} VERBOSE=1
popd
mkdir -p clr-build32
pushd clr-build32
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -mzero-caller-saved-regs=used "
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32"
%cmake -DLIB_INSTALL_DIR:PATH=/usr/lib32 -DCMAKE_INSTALL_LIBDIR=/usr/lib32 -DLIB_SUFFIX=32 ..
make  %{?_smp_mflags} VERBOSE=1
unset PKG_CONFIG_PATH
popd

%install
export SOURCE_DATE_EPOCH=1547103189
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/freetype
cp docs/GPLv2.TXT %{buildroot}/usr/share/package-licenses/freetype/docs_GPLv2.TXT
cp docs/LICENSE.TXT %{buildroot}/usr/share/package-licenses/freetype/docs_LICENSE.TXT
pushd clr-build32
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/freetype2/freetype/config/ftconfig.h
/usr/include/freetype2/freetype/config/ftheader.h
/usr/include/freetype2/freetype/config/ftmodule.h
/usr/include/freetype2/freetype/config/ftoption.h
/usr/include/freetype2/freetype/config/ftstdlib.h
/usr/include/freetype2/freetype/freetype.h
/usr/include/freetype2/freetype/ftadvanc.h
/usr/include/freetype2/freetype/ftbbox.h
/usr/include/freetype2/freetype/ftbdf.h
/usr/include/freetype2/freetype/ftbitmap.h
/usr/include/freetype2/freetype/ftbzip2.h
/usr/include/freetype2/freetype/ftcache.h
/usr/include/freetype2/freetype/ftchapters.h
/usr/include/freetype2/freetype/ftcid.h
/usr/include/freetype2/freetype/ftdriver.h
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
/usr/include/freetype2/freetype/ftparams.h
/usr/include/freetype2/freetype/ftpfr.h
/usr/include/freetype2/freetype/ftrender.h
/usr/include/freetype2/freetype/ftsizes.h
/usr/include/freetype2/freetype/ftsnames.h
/usr/include/freetype2/freetype/ftstroke.h
/usr/include/freetype2/freetype/ftsynth.h
/usr/include/freetype2/freetype/ftsystem.h
/usr/include/freetype2/freetype/fttrigon.h
/usr/include/freetype2/freetype/fttypes.h
/usr/include/freetype2/freetype/ftwinfnt.h
/usr/include/freetype2/freetype/t1tables.h
/usr/include/freetype2/freetype/ttnameid.h
/usr/include/freetype2/freetype/tttables.h
/usr/include/freetype2/freetype/tttags.h
/usr/include/freetype2/ft2build.h
/usr/lib64/cmake/freetype/freetype-config-relwithdebinfo.cmake
/usr/lib64/cmake/freetype/freetype-config.cmake
/usr/lib64/libfreetype.so
/usr/lib64/pkgconfig/freetype2.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/cmake/freetype/freetype-config-relwithdebinfo.cmake
/usr/lib32/cmake/freetype/freetype-config.cmake
/usr/lib32/libfreetype.so
/usr/lib32/pkgconfig/32freetype2.pc
/usr/lib32/pkgconfig/freetype2.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libfreetype.so.6
/usr/lib64/libfreetype.so.6.16.0

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libfreetype.so.6
/usr/lib32/libfreetype.so.6.16.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/freetype/docs_GPLv2.TXT
/usr/share/package-licenses/freetype/docs_LICENSE.TXT
