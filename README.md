# Physics Notes

Study and research notes — from QFT calculations to the research frontier. Built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) and deployed to GitHub Pages at <https://leeshep.github.io/>.

## Preview locally

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
mkdocs serve   # http://127.0.0.1:8000/
```

## Writing

- Add a `.md` file under `docs/`, then list it under `nav:` in `mkdocs.yml` to place it in the sidebar/tabs.
- Math: inline `$...$`, display `$$...$$`, numbered `\begin{equation} ... \label{eq:x} \end{equation}`, and reference it in text with `$\eqref{eq:x}$` (wrap it in dollar signs).
- Physics macros (`\dd`, `\ket{}`, `\slashed{}`, …) live in `docs/javascripts/mathjax.js`.
- Collapsible blocks: `??? example "Title"`; callouts: `!!! note`, `!!! question`, etc.
- See `docs/qft/01-canonical-quantization.md` for an example.

## Deployment

Pushing to `main` triggers GitHub Actions (`.github/workflows/deploy.yml`), which builds the site and publishes it to Pages.
