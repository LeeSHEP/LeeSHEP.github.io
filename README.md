# Physics Notes

QFT 계산부터 연구 최전선까지 — 공부·연구 노트. [MkDocs Material](https://squidfunk.github.io/mkdocs-material/)로 빌드되어 GitHub Pages에 배포됩니다.

## 로컬에서 보기

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
mkdocs serve   # http://127.0.0.1:8000/
```

## 글 쓰기

- `docs/` 아래에 `.md` 파일을 추가하면 자동으로 사이드바에 나타납니다 (순서는 파일 이름순 → `01-`, `02-` 접두사 사용).
- 수식: 인라인 `$...$`, 디스플레이 `$$...$$`, 번호 매기기 `\begin{equation} ... \label{eq:x} \end{equation}` + 본문에서 `$\eqref{eq:x}$` (달러로 감싸기).
- 물리 매크로(`\dd`, `\ket{}`, `\slashed{}` 등)는 `docs/javascripts/mathjax.js`에서 추가/수정.
- 접는 블록: `??? example "제목"`, 강조 블록: `!!! note`, `!!! question` 등.
- 예시는 `docs/qft/01-canonical-quantization.md` 참고.

## 배포

`main`에 push하면 GitHub Actions(`.github/workflows/deploy.yml`)가 빌드해서 Pages에 올립니다.
최초 1회: repo의 **Settings → Pages → Source** 를 **GitHub Actions** 로 설정.
