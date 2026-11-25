# Physics Notes

PDF notes written in LaTeX, listed on <https://leeshep.github.io/>.

## Layout

```
notes/<section>/<name>.tex   one note = one .tex file → one PDF
tex/physnotes.sty            shared preamble (packages + macros)
site.toml                    page title, intro, links, section order
build.py                     compiles notes → _site/pdf/, writes _site/index.html
assets/style.css             list page style
```

## Writing a note

```latex
\documentclass[11pt]{article}
\usepackage{physnotes}

\title{One-Loop Self-Energy in $\phi^4$}
\author{LeeSHEP}
\date{November 2026}
% summary: One line shown under the title on the list page.
% draft      <- remove this line to publish

\begin{document}
\maketitle
...
\end{document}
```

- Files are listed in filename order — use `01-`, `02-` prefixes.
- `% draft` keeps a note out of the build and the list.
- New section: make a folder under `notes/` and add it to `[[sections]]` in `site.toml`.
- Macros from `physnotes.sty`: `\dd`, `\bra`, `\ket`, `\braket`, `\order`, `\tr`, `\Tr`, `\qty` (physics package), `\slashed`, `\ii`, `\Lag`.

## Build locally

```bash
python3 build.py              # needs latexmk (MacTeX)
open _site/index.html
```

`python3 build.py --no-pdf` rewrites only the list page.

## Deploy

Push to `main`. GitHub Actions installs TeX Live, runs `build.py`, and publishes `_site/` to Pages.
If a note fails to compile, the deploy fails and the log shows the LaTeX error.
