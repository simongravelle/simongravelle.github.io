\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{concours}
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{article}}
\ProcessOptions
\LoadClass{article}

\RequirePackage{mathptmx} % defines Adobe Times Roman (or equivalent) as default text font
\RequirePackage[utf8]{inputenc} % translates various input into a LaTeX internal language
\RequirePackage{indentfirst} % minimalist package is part of the latex-tools bundle
\RequirePackage{csquotes} % advanced facilities for inline and display quotations
\RequirePackage[T1]{fontenc} % allows the user to select font encodings
\RequirePackage[cyr]{aeguill} % enables the user to add guillemets from several source
\RequirePackage{multicol} % defines a multicols environment which typesets text in multiple column
\RequirePackage{etoolbox} % toolbox of programming facilities 
\RequirePackage{relsize} % Set the font size relative to the current font size
\RequirePackage{amsmath,amssymb} % adapts most of the mathematical features 
\RequirePackage[language=english,style=numeric-comp,sorting=none,backref=false,maxnames=4,minnames=4,backrefstyle=three,giveninits=true,backend=biber]{biblatex}
\RequirePackage[table]{xcolor}
\RequirePackage[pdftex,colorlinks=true,linkcolor=new_gray0,citecolor=new_gray0,urlcolor=new_gray0]{hyperref}
\RequirePackage{anysize}
\RequirePackage{fancyhdr} %  for constructing headers and footers
\RequirePackage{lastpage}
\RequirePackage{titlesec}
\RequirePackage{titletoc}
%\RequirePackage[export]{adjustbox}
\RequirePackage{changepage}
\RequirePackage{abstract}
\RequirePackage[pdftex]{graphicx}\DeclareGraphicsExtensions{.jpg,.png,.pdf}
\RequirePackage{multirow}
\RequirePackage{tabularx}
\RequirePackage{longtable}
\RequirePackage{wasysym}
\RequirePackage{subfigure}
\RequirePackage[rightcaption]{sidecap} \sidecaptionvpos{figure}{c}
\RequirePackage[font=small,labelfont=bf,labelsep=endash]{caption}
\RequirePackage[subpreambles=false]{standalone}
\RequirePackage{wrapfig}
\RequirePackage{arydshln}
\RequirePackage{tikz}
\RequirePackage[french]{babel}
\RequirePackage{enumitem}
\RequirePackage{microtype}
\RequirePackage{colortbl}
%\RequirePackage{palatino} % good font
\RequirePackage{cmbright} % Computer Modern Bright fonts
%\RequirePackage[sfdefault]{libertine} % good font
\RequirePackage{cmbright}
\RequirePackage[normalem]{ulem}
\RequirePackage[most]{tcolorbox}

\renewcommand{\figurename}{Figure}
\newcommand*\rot{\rotatebox{90}}

\DeclareRobustCommand{\sm@ller}{%
    \dimen@\f@size\p@
    \ifdim \dimen@ > 12\p@
        \dimen@=0.83333\dimen@
    \else
        \advance \dimen@ -2\p@
    \fi
    \math@fontsfalse
    \fontsize{\the\dimen@}\z@
    \selectfont
}

\newcommand{\hzero}[1]{\textcolor{dark}{\textbf{#1}}}
\newcommand{\hone}[1]{\textcolor{new_gray0}{\textbf{#1}}}
\newcommand{\htwo}[1]{\textcolor{new_gray1}{\textbf{#1}}}
\newcommand{\hthr}[1]{\textcolor{new_gray2}{\textbf{#1}}}
\newcommand{\hblue}[1]{\textcolor{blue_1}{\textbf{#1}}}
\newcommand{\hbluebis}[1]{\textcolor{blue_2}{\textbf{#1}}}
\newcommand{\textc}[1]{{\sm@ller\uppercase{#1}}}
\newcommand{\cshape}[1]{{\sm@ller\uppercase{#1}}}
\newcommand{\s}[1]{\vspace{0.2cm} \noindent #1}
\newcommand{\newpara}[1]{\vspace{0.4cm}\noindent \hbluebis{\textbf{#1}}}
\newcommand{\firstpara}[1]{\noindent \hbluebis{\textbf{#1}}}
\newcommand{\h}[1]{\textcolor{new_gray0}{\textbf{#1}}}
\newcommand{\hi}[1]{\textcolor{new_gray0}{\textbf{#1}}}

\newcommand{\parasep}{
  \begin{center}
    \noindent\rule[\baselineskip]{.5\textwidth}{.7pt}
  \end{center}\vskip-1.2\baselineskip
}

\makeatletter
\renewcommand\tableofcontents{%
    \@starttoc{toc}%
}


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Page setting
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\marginsize{15mm}{15mm}{10mm}{10mm}
\setlength{\headheight}{14pt}



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Sections & subsections
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\titlecontents{section}[0em]{\vskip 0.0ex}{}{}{\titlerule*[1pc]{.}\contentspage \nobreak}
\titlecontents{subsection}[0em]{\vskip 0.0ex}{\hskip.03\linewidth}{}{\titlerule*[1pc]{.}\contentspage \nobreak}
%\titlecontents{subsubsection}[0em]{\vskip 0.0ex}{\hskip.06\linewidth}{}{\titlerule*[1pc]{.}\contentspage \nobreak}
%\titlecontents{paragraph}[0em]{\vskip 0.0ex}{}{}{\titlerule*[1pc]{.}\contentspage \nobreak}
%\titlecontents{subparagraph}[0em]{\vskip 0.0ex}{}{}{\titlerule*[1pc]{.}\contentspage \nobreak}

\titleformat{\section}
{\color{new_gray0}\normalfont\LARGE\bfseries}
{\color{new_gray0}}{0em}{}

\titleformat{\subsection}
{\color{new_gray0}\normalfont\Large\bfseries}
{\color{new_gray0}}{0em}{}

%\titleformat{\subsubsection}
%{\color{new_gray0}\large\bfseries}
%{\color{new_gray0}}{0em}{}

%\titleformat{\paragraph}
%{\normalfont\bfseries}
%{}{0em}{}

\titlespacing*{\section}
{0pt}{.5ex plus .5ex minus .2ex}{3ex plus .5ex minus .2ex}
\titlespacing*{\subsection}
{0pt}{3ex}{0ex}
\titlespacing*{\subsubsection}
{0pt}{2ex}{2ex}
\titlespacing*{\paragraph}
{0pt}{2ex}{2ex}



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Abstract
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%\renewcommand{\abstractnamefont}{\normalfont\bfseries\color{new_gray0}}
%\renewcommand{\abstracttextfont}{\normalfont\color{black}}
%\renewcommand{\abstractname}{Résumé}

\renewenvironment{@bstr@ctlist}{%
\list{}{%
\itemindent \listparindent
\leftmargin \absleftindent
\rightmargin \absrightindent
\parsep \absparsep}%
 \item \abstractnamefont\abstractname.~\relax}
{\endlist}

\renewenvironment{abstract}{
  \begin{@bstr@ctlist}\abstracttextfont}%
{\par\end{@bstr@ctlist}}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% My own bibliography style, with DOI or url links, and backreferences
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%\AtBeginBibliography{\small}
\AtBeginBibliography{\footnotesize}
%\AtBeginBibliography{\tiny}

\renewcommand{\bibfont}{\normalfont\small}
\renewcommand{\refname}{}

\renewcommand*{\mkbibnamegiven}[1]{{\ifgiveninits{\let~\,}{}#1}}
\DefineBibliographyStrings{english}{%
  backrefpage = {{\emph{cf.} }}{{p.}},%
  backrefpages = {{\emph{cf.} }}{{pp.}},%
}
\DeclareFieldFormat[article]{title}{``#1''}
\DeclareFieldFormat[article]{pages}{#1}
\DeclareFieldFormat[article]{volume}{\textbf{#1}}
\ExecuteBibliographyOptions{doi=false}
\DeclareFieldFormat{doilink}{%
\iffieldundef{doi}{#1}{\href{http://dx.doi.org/\thefield{doi}}{#1}}}
\DeclareFieldFormat{urllink}{%
\iffieldundef{url}{#1}{\href{\thefield{url}}{#1}}}

%\renewcommand*{\finalnamedelim}{~\emph{\&}~}
\renewcommand*{\finalnamedelim}{~\&~}
\renewcommand*{\newunitpunct}{\addcomma\space}
\renewbibmacro*{date}{\printtext{\printfield{year}}}
\renewbibmacro*{volume+number+eid}{\printfield{volume}}
\renewbibmacro*{journal+issuetitle}{%
  \emph{\usebibmacro{journal}}%
  \setunit*{\addspace}%
  \usebibmacro{volume+number+eid}
  \printtext[parens]{\printfield{year}}%
}

\DeclareBibliographyDriver{article}{%
  \usebibmacro{bibindex}%
  \usebibmacro{begentry}%
  \emph{\usebibmacro{title}}
  \usebibmacro{author/translator+others}%
  \setunit{\labelnamepunct}\newblock%
  \newunit
  \printlist{language}%
  \newunit\newblock
  \usebibmacro{byauthor}%
  \newunit\newblock
  \usebibmacro{bytranslator+others}%
  \newunit\newblock
  \printfield{version}%
  \newunit\newblock
  \iffieldundef{url}{
      \printtext[doilink]{%
      \usebibmacro{journal+issuetitle}%
      \newunit
      \usebibmacro{byeditor+others}%
      \newunit
      \usebibmacro{note+pages}}
    }%
    {\printtext[urllink]{%
      \usebibmacro{journal+issuetitle}%
      \newunit
      \usebibmacro{byeditor+others}%
      \newunit
      \usebibmacro{note+pages}}%
    }
  \newunit\newblock
  \usebibmacro{addendum+pubstate}%
  \setunit{\bibpagerefpunct}\newblock
  \usebibmacro{pageref}%
}

\DeclareBibliographyDriver{misc}{%
  \usebibmacro{bibindex}%
  \usebibmacro{begentry}%
  \usebibmacro{author/translator+others}%
  \setunit{\labelnamepunct}\newblock
  \emph{\usebibmacro{title}}%
  \setunit{\bibpagerefpunct}\newblock
  \usebibmacro{pageref}%
}

\DeclareFieldFormat[inbook]{chapter}{"#1"}
\DeclareFieldFormat[inbook]{title}{In: \mkbibemph{#1}}
\DeclareBibliographyDriver{inbook}{%
  \usebibmacro{bibindex}%
  \usebibmacro{begentry}%
  \usebibmacro{author/editor+others/translator+others}%
  \setunit{\labelnamepunct}\newblock
  \usebibmacro{chapter+pages}%
  \newunit\newblock
  \printtext[urllink]{\usebibmacro{maintitle+title}}%
  \newunit\newblock
  \usebibmacro{byauthor}%
  \newunit\newblock
  \usebibmacro{byeditor+others}%
  \newunit\newblock
  \usebibmacro{publisher+location+date}%
  \newunit
  \printfield{pagetotal}%
  \newunit\newblock
  \printfield{note}%
  \newunit\newblock
  \usebibmacro{addendum+pubstate}%
  \setunit{\bibpagerefpunct}\newblock
  \usebibmacro{pageref}%
}



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Macro for changing margin locally
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\newenvironment{changemargin}[2]{\begin{list}{}{%
\setlength{\topsep}{0pt}%
\setlength{\leftmargin}{0pt}%
\setlength{\rightmargin}{0pt}%
\setlength{\listparindent}{\parindent}%
\setlength{\itemindent}{\parindent}%
\setlength{\parsep}{0pt plus 1pt}%
\addtolength{\leftmargin}{#1}%
\addtolength{\rightmargin}{#2}%
}\item }{\end{list}}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\endinput
