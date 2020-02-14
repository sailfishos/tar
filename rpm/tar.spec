Name:           tar
Version:        1.32
Release:        1
Summary:        A GNU file archiving program
License:        GPLv3+
URL:            http://www.gnu.org/software/tar/
Source:         %{name}-%{version}.tar.bz2
Patch0:         tar-1.28-loneZeroWarning.patch
Patch1:         tar-1.28-vfatTruncate.patch
Patch2:         tar-1.29-wildcards.patch
BuildRequires:  gettext
BuildRequires:  libacl-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
Provides:       gnu-tar

%description
The GNU tar program saves many files together in one archive and can
restore individual files (or all of the files) from that archive. Tar
can also be used to add supplemental files to an archive and to update
or list files in the archive. Tar includes multivolume support,
automatic archive compression/decompression, the ability to perform
remote archives, and the ability to perform incremental and full
backups.

If you want to use tar for remote backups, you also need to install
the rmt package.

%prep
%autosetup -p1 -n %{name}-%{version}/%{name}

%build
sed -i 's/doc //' Makefile.am
./bootstrap --no-git --skip-po --gnulib-srcdir=gnulib
export tar_cv_path_RSH=no
%configure --bindir=%{_bindir}

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
