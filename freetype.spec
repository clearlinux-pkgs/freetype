#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xBE6C3AAC63AD8E3F (wl@gnu.org)
#
Name     : freetype
Version  : 2.12.1
Release  : 72
URL      : https://download-mirror.savannah.gnu.org/releases/freetype/freetype-2.12.1.tar.gz
Source0  : https://download-mirror.savannah.gnu.org/releases/freetype/freetype-2.12.1.tar.gz
Source1  : https://download-mirror.savannah.gnu.org/releases/freetype/freetype-2.12.1.tar.gz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : FTL GPL-2.0 GPL-2.0+ MIT Zlib
Requires: freetype-bin = %{version}-%{release}
Requires: freetype-lib = %{version}-%{release}
Requires: freetype-license = %{version}-%{release}
Requires: freetype-man = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-configure
BuildRequires : buildreq-meson
BuildRequires : bzip2-dev
BuildRequires : bzip2-dev32
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : harfbuzz-dev
BuildRequires : libpng-dev
BuildRequires : libpng-dev32
BuildRequires : pkg-config
BuildRequires : pkgconfig(librsvg-2.0)
BuildRequires : zlib-dev32
Patch1: debuginfo.patch

%description
FreeType 2.12.1
===============
Homepage: https://www.freetype.org
FreeType is a freely available software library to render fonts.

%package bin
Summary: bin components for the freetype package.
Group: Binaries
Requires: freetype-license = %{version}-%{release}

%description bin
bin components for the freetype package.


%package dev
Summary: dev components for the freetype package.
Group: Development
Requires: freetype-lib = %{version}-%{release}
Requires: freetype-bin = %{version}-%{release}
Provides: freetype-devel = %{version}-%{release}
Requires: freetype = %{version}-%{release}

%description dev
dev components for the freetype package.


%package dev32
Summary: dev32 components for the freetype package.
Group: Default
Requires: freetype-lib32 = %{version}-%{release}
Requires: freetype-bin = %{version}-%{release}
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


%package man
Summary: man components for the freetype package.
Group: Default

%description man
man components for the freetype package.


%prep
%setup -q -n freetype-2.12.1
cd %{_builddir}/freetype-2.12.1
%patch1 -p1
pushd ..
cp -a freetype-2.12.1 build32
popd
pushd ..
cp -a freetype-2.12.1 buildavx2
popd
pushd ..
cp -a freetype-2.12.1 buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656028848
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -mprefer-vector-width=256 "
export FCFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -mprefer-vector-width=256 "
export FFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -mprefer-vector-width=256 "
export CXXFLAGS="$CXXFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -mprefer-vector-width=256 "
%configure --disable-static --enable-freetype-config
make  %{?_smp_mflags}  RC=

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig:/usr/share/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
%configure --disable-static --enable-freetype-config --with-harfbuzz=no  --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}  RC=
popd
unset PKG_CONFIG_PATH
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3"
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3"
%configure --disable-static --enable-freetype-config
make  %{?_smp_mflags}  RC=
popd
unset PKG_CONFIG_PATH
pushd ../buildavx512/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v4 -mprefer-vector-width=256 -Wl,-z,x86-64-v4"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v4 -mprefer-vector-width=256 -Wl,-z,x86-64-v4"
export FFLAGS="$FFLAGS -m64 -march=x86-64-v4 -mprefer-vector-width=256"
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v4 -mprefer-vector-width=256"
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v4"
%configure --disable-static --enable-freetype-config
make  %{?_smp_mflags}  RC=
popd
%install
export SOURCE_DATE_EPOCH=1656028848
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/freetype
cp %{_builddir}/freetype-2.12.1/LICENSE.TXT %{buildroot}/usr/share/package-licenses/freetype/4ddaa192f25581d05cb4d3219d57c1edc76167b7
cp %{_builddir}/freetype-2.12.1/docs/GPLv2.TXT %{buildroot}/usr/share/package-licenses/freetype/dac7127c82749e3107b53530289e1cd548860868
pushd ../build32/
%make_install32 RC=
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
if [ -d %{buildroot}/usr/share/pkgconfig ]
then
pushd %{buildroot}/usr/share/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
pushd ../buildavx2/
%make_install_v3 RC=
popd
pushd ../buildavx512/
%make_install_v4 RC=
popd
%make_install RC=
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
/usr/include/freetype2/freetype/config/integer-types.h
/usr/include/freetype2/freetype/config/mac-support.h
/usr/include/freetype2/freetype/config/public-macros.h
/usr/include/freetype2/freetype/freetype.h
/usr/include/freetype2/freetype/ftadvanc.h
/usr/include/freetype2/freetype/ftbbox.h
/usr/include/freetype2/freetype/ftbdf.h
/usr/include/freetype2/freetype/ftbitmap.h
/usr/include/freetype2/freetype/ftbzip2.h
/usr/include/freetype2/freetype/ftcache.h
/usr/include/freetype2/freetype/ftchapters.h
/usr/include/freetype2/freetype/ftcid.h
/usr/include/freetype2/freetype/ftcolor.h
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
/usr/include/freetype2/freetype/ftlogging.h
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
/usr/include/freetype2/freetype/otsvg.h
/usr/include/freetype2/freetype/t1tables.h
/usr/include/freetype2/freetype/ttnameid.h
/usr/include/freetype2/freetype/tttables.h
/usr/include/freetype2/freetype/tttags.h
/usr/include/freetype2/ft2build.h
/usr/lib64/libfreetype.so
/usr/lib64/pkgconfig/freetype2.pc
/usr/share/aclocal/*.m4

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libfreetype.so
/usr/lib32/pkgconfig/32freetype2.pc
/usr/lib32/pkgconfig/freetype2.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/glibc-hwcaps/x86-64-v3/libfreetype.so
/usr/lib64/glibc-hwcaps/x86-64-v3/libfreetype.so.6
/usr/lib64/glibc-hwcaps/x86-64-v3/libfreetype.so.6.18.3
/usr/lib64/glibc-hwcaps/x86-64-v4/libfreetype.so
/usr/lib64/glibc-hwcaps/x86-64-v4/libfreetype.so.6
/usr/lib64/glibc-hwcaps/x86-64-v4/libfreetype.so.6.18.3
/usr/lib64/libfreetype.so.6
/usr/lib64/libfreetype.so.6.18.3

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libfreetype.so.6
/usr/lib32/libfreetype.so.6.18.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/freetype/4ddaa192f25581d05cb4d3219d57c1edc76167b7
/usr/share/package-licenses/freetype/dac7127c82749e3107b53530289e1cd548860868

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/freetype-config.1
