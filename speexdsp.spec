#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
#
# Source0 file verified with key 0x127B10EED8765B47 (tmatth@videolan.org)
#
Name     : speexdsp
Version  : 1.2.1
Release  : 27
URL      : https://ftp.osuosl.org/pub/xiph/releases/speex/speexdsp-1.2.1.tar.gz
Source0  : https://ftp.osuosl.org/pub/xiph/releases/speex/speexdsp-1.2.1.tar.gz
Source1  : https://ftp.osuosl.org/pub/xiph/releases/speex/speexdsp-1.2.1.tar.gz.asc
Summary  : An open-source, patent-free speech codec
Group    : Development/Tools
License  : BSD-3-Clause
Requires: speexdsp-lib = %{version}-%{release}
Requires: speexdsp-license = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : pkg-config
BuildRequires : pkgconfig(fftw3f)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Speex is a patent-free audio codec designed especially for voice (unlike 
Vorbis which targets general audio) signals and providing good narrowband 
and wideband quality. This project aims to be complementary to the Vorbis
codec.

%package dev
Summary: dev components for the speexdsp package.
Group: Development
Requires: speexdsp-lib = %{version}-%{release}
Provides: speexdsp-devel = %{version}-%{release}
Requires: speexdsp = %{version}-%{release}

%description dev
dev components for the speexdsp package.


%package dev32
Summary: dev32 components for the speexdsp package.
Group: Default
Requires: speexdsp-lib32 = %{version}-%{release}
Requires: speexdsp-dev = %{version}-%{release}

%description dev32
dev32 components for the speexdsp package.


%package doc
Summary: doc components for the speexdsp package.
Group: Documentation

%description doc
doc components for the speexdsp package.


%package lib
Summary: lib components for the speexdsp package.
Group: Libraries
Requires: speexdsp-license = %{version}-%{release}

%description lib
lib components for the speexdsp package.


%package lib32
Summary: lib32 components for the speexdsp package.
Group: Default
Requires: speexdsp-license = %{version}-%{release}

%description lib32
lib32 components for the speexdsp package.


%package license
Summary: license components for the speexdsp package.
Group: Default

%description license
license components for the speexdsp package.


%prep
%setup -q -n speexdsp-1.2.1
cd %{_builddir}/speexdsp-1.2.1
pushd ..
cp -a speexdsp-1.2.1 build32
popd
pushd ..
cp -a speexdsp-1.2.1 buildavx2
popd
pushd ..
cp -a speexdsp-1.2.1 buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1687231698
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%configure --disable-static
make  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig:/usr/share/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
%configure --disable-static    --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
unset PKG_CONFIG_PATH
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3"
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3"
%configure --disable-static
make  %{?_smp_mflags}
popd
unset PKG_CONFIG_PATH
pushd ../buildavx512/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v4 -mprefer-vector-width=512 -Wl,-z,x86-64-v4 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v4 -mprefer-vector-width=512 -Wl,-z,x86-64-v4 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v4 -mprefer-vector-width=512"
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v4 -mprefer-vector-width=512"
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v4"
%configure --disable-static
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../build32;
make %{?_smp_mflags} check || :
cd ../buildavx2;
make %{?_smp_mflags} check || :
cd ../buildavx512;
make %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1687231698
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/speexdsp
cp %{_builddir}/speexdsp-%{version}/COPYING %{buildroot}/usr/share/package-licenses/speexdsp/fc3b9b42abbb2f2b795ad9598708f3db0b3e9ae7 || :
pushd ../build32/
%make_install32
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
%make_install_v3
popd
pushd ../buildavx512/
%make_install_v4
popd
%make_install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/speex/speex_echo.h
/usr/include/speex/speex_jitter.h
/usr/include/speex/speex_preprocess.h
/usr/include/speex/speex_resampler.h
/usr/include/speex/speexdsp_config_types.h
/usr/include/speex/speexdsp_types.h
/usr/lib64/libspeexdsp.so
/usr/lib64/pkgconfig/speexdsp.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libspeexdsp.so
/usr/lib32/pkgconfig/32speexdsp.pc
/usr/lib32/pkgconfig/speexdsp.pc

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/speexdsp/*

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libspeexdsp.so.1.5.2
/V4/usr/lib64/libspeexdsp.so.1.5.2
/usr/lib64/libspeexdsp.so.1
/usr/lib64/libspeexdsp.so.1.5.2

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libspeexdsp.so.1
/usr/lib32/libspeexdsp.so.1.5.2

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/speexdsp/fc3b9b42abbb2f2b795ad9598708f3db0b3e9ae7
