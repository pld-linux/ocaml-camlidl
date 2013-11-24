# NOTE
# - duplicate of ocaml-idl.spec
Summary:	Camlidl - stub code generator for OCaml
Summary(pl.UTF-8):	Camlidl - generator kodu zaślepek dla OCamla
Name:		ocaml-camlidl
Version:	1.05
Release:	2
License:	QPL v1.0 (compiler), LGPL v2 (library)
Group:		Libraries
Source0:	http://caml.inria.fr/pub/old_caml_site/distrib/bazar-ocaml/camlidl-%{version}.tar.gz
# Source0-md5:	4cfb863bc3cbdc1af2502042c45cc675
URL:		http://caml.inria.fr/pub/old_caml_site/camlidl/
BuildRequires:	ocaml >= 3.08
%requires_eq	ocaml-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Camlidl is a stub code generator for Objective Caml. It generates stub
code for interfacing Caml with C from an IDL description of the C
functions. Thus, Camlidl automates the most tedious task in
interfacing C libraries with Caml programs. It can also be used to
interface Caml programs with other languages, as long as those
languages have a well-defined C interface.

%description -l pl.UTF-8
Camlidl to generator zaślepej dla języka Objective Caml. Generuje kod
zaślepek dla interfejsów między Camlem a C na podstawie opisu IDL
funkcji C. W ten sposób automatyzuje najbardziej nurzące zadanie przy
tworzeniu interfejsów camlowych do bibliotek C. Camlidl może być
używany także do osiągnięcia współpracy między programami w Camlu a
innymi językami, o ile te języki mają dobrze zdefiniowane interfejsy w
C.

%prep
%setup -q -n camlidl-%{version}

ln -s Makefile.unix config/Makefile

%build
%{__make} -j1 \
	CPP="%{__cc} -E -x c"  \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/ocaml,%{_includedir}/caml}
ln -sf ../../include/caml $RPM_BUILD_ROOT%{_libdir}/ocaml/caml

%{__make} install \
	BINDIR=$RPM_BUILD_ROOT%{_bindir} \
	OCAMLLIB=$RPM_BUILD_ROOT%{_libdir}/ocaml

# shut up check-files
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/caml

install -d $RPM_BUILD_ROOT%{_libdir}/ocaml/site-lib/camlidl
cat > $RPM_BUILD_ROOT%{_libdir}/ocaml/site-lib/camlidl/META <<EOF
requires = ""
version = "%{version}"
directory = "+camlidl"
archive(byte) = "camlidl.cma"
archive(native) = "camlidl.cmxa"
linkopts = ""
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes LICENSE README
%attr(755,root,root) %{_bindir}/camlidl
%{_libdir}/ocaml/libcamlidl.a
%{_libdir}/ocaml/com.a
%{_libdir}/ocaml/com.cma
%{_libdir}/ocaml/com.cmi
%{_libdir}/ocaml/com.cmxa
%{_libdir}/ocaml/site-lib/camlidl
%{_includedir}/caml/camlidlruntime.h
