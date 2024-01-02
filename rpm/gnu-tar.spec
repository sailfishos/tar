%define _name tar
Name:           gnu-%{_name}
Version:        1.35
Release:        1
Summary:        A GNU file archiving program
License:        GPLv3+
URL:            http://www.gnu.org/software/tar/
Source:         %{name}-%{version}.tar.bz2
Patch0:         0001-Stop-issuing-lone-zero-block-warnings-downstram.patch
Patch1:         0002-vfat-like-FS-sparse-still-downstream.patch
Patch2:         0003-wildcard-defaults-downstram-compatibility.patch
Patch3:         0004-Don-t-build-docs.patch
BuildRequires:  gettext
BuildRequires:  libacl-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
Provides:       %{_name} = 1.32+git2
Obsoletes:      %{_name} < 1.32+git2

%description
The GNU tar program saves many files together in one archive and can
restore individual files (or all of the files) from that archive. Tar
can also be used to add supplemental files to an archive and to update
or list files in the archive. Tar includes multivolume support,
automatic archive compression/decompression, the ability to perform
remote archives, and the ability to perform incremental and full
backups.

%prep
%autosetup -p1 -n %{name}-%{version}/tar

%build
./bootstrap --no-git --skip-po --gnulib-srcdir=gnulib
export tar_cv_path_RSH=no
%configure --bindir=%{_bindir} --disable-year2038

%install
%make_install
mkdir -p %{buildroot}/bin
ln -sf %{_bindir}/tar %{buildroot}/bin/tar
rm -rf %{buildroot}%{_prefix}/libexec/rmt

%files
%defattr(-,root,root,-)
/bin/tar
%{_bindir}/tar
%license COPYING
