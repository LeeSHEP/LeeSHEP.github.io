---
tags:
  - QFT
  - scalar field
---

# Scalar 장의 정준양자화

!!! info "이 페이지는 템플릿 예시입니다"
    수식 번호, 참조, 접는 블록 등 사이트에서 쓸 수 있는 문법을 보여주기 위한 노트입니다. 실제 내용으로 바꿔 쓰세요.

## Lagrangian

실수 scalar 장의 Lagrangian 밀도는

\begin{equation}
\Lag = \frac{1}{2}\partial_\mu\phi\,\partial^\mu\phi - \frac{1}{2}m^2\phi^2 .
\label{eq:lag}
\end{equation}

Euler–Lagrange 방정식을 $\eqref{eq:lag}$에 적용하면 Klein–Gordon 방정식 $(\partial^2 + m^2)\phi = 0$ 을 얻는다.

## 모드 전개

$$
\phi(x) = \int \frac{\dd^3 p}{(2\pi)^3}\frac{1}{\sqrt{2E_p}}
\left( a_{\mathbf p}\, e^{-\ii p\cdot x} + a^\dagger_{\mathbf p}\, e^{\ii p\cdot x} \right),
\qquad E_p = \sqrt{\mathbf p^2 + m^2}
$$

생성·소멸 연산자의 교환관계:

\begin{equation}
[a_{\mathbf p}, a^\dagger_{\mathbf q}] = (2\pi)^3\,\delta^{(3)}(\mathbf p - \mathbf q).
\label{eq:ccr}
\end{equation}

??? example "유도: $[\phi(\mathbf x), \pi(\mathbf y)] = \ii\delta^{(3)}(\mathbf x - \mathbf y)$ 확인 (클릭해서 펼치기)"
    $\eqref{eq:ccr}$를 대입하고 $\pi = \dot\phi$ 를 쓰면 …

    $$
    [\phi(\mathbf x), \pi(\mathbf y)]
    = \int \frac{\dd^3 p}{(2\pi)^3}\,\frac{-\ii}{2}\left( -e^{\ii \mathbf p\cdot(\mathbf x-\mathbf y)} - e^{-\ii \mathbf p\cdot(\mathbf x-\mathbf y)} \right)
    = \ii\,\delta^{(3)}(\mathbf x-\mathbf y).
    $$

!!! note "Convention"
    metric은 $(+,-,-,-)$, Peskin & Schroeder 관례를 따름.

!!! question "남은 질문"
    - 진공 에너지의 무한대는 normal ordering 외에 어떻게 이해할 수 있나?

## 참고문헌

- Peskin & Schroeder, *An Introduction to QFT*, Ch. 2
- Srednicki, *Quantum Field Theory*, Ch. 3
