---
tags:
  - QFT
  - scalar field
---

# Canonical Quantization of the Scalar Field

!!! info "This page is a template example"
    This note shows the syntax available on this site: equation numbering, references, collapsible blocks, and so on. Replace it with real content.

## Lagrangian

The Lagrangian density of a real scalar field is

\begin{equation}
\Lag = \frac{1}{2}\partial_\mu\phi\,\partial^\mu\phi - \frac{1}{2}m^2\phi^2 .
\label{eq:lag}
\end{equation}

Applying the Euler–Lagrange equation to $\eqref{eq:lag}$ gives the Klein–Gordon equation $(\partial^2 + m^2)\phi = 0$.

## Mode expansion

$$
\phi(x) = \int \frac{\dd^3 p}{(2\pi)^3}\frac{1}{\sqrt{2E_p}}
\left( a_{\mathbf p}\, e^{-\ii p\cdot x} + a^\dagger_{\mathbf p}\, e^{\ii p\cdot x} \right),
\qquad E_p = \sqrt{\mathbf p^2 + m^2}
$$

The creation and annihilation operators satisfy

\begin{equation}
[a_{\mathbf p}, a^\dagger_{\mathbf q}] = (2\pi)^3\,\delta^{(3)}(\mathbf p - \mathbf q).
\label{eq:ccr}
\end{equation}

??? example "Derivation: checking $[\phi(\mathbf x), \pi(\mathbf y)] = \ii\delta^{(3)}(\mathbf x - \mathbf y)$ (click to expand)"
    Substituting $\eqref{eq:ccr}$ and using $\pi = \dot\phi$, …

    $$
    [\phi(\mathbf x), \pi(\mathbf y)]
    = \int \frac{\dd^3 p}{(2\pi)^3}\,\frac{-\ii}{2}\left( -e^{\ii \mathbf p\cdot(\mathbf x-\mathbf y)} - e^{-\ii \mathbf p\cdot(\mathbf x-\mathbf y)} \right)
    = \ii\,\delta^{(3)}(\mathbf x-\mathbf y).
    $$

!!! note "Conventions"
    Metric signature $(+,-,-,-)$, following Peskin & Schroeder.

!!! question "Open questions"
    - Beyond normal ordering, how should we understand the infinite vacuum energy?

## References

- Peskin & Schroeder, *An Introduction to Quantum Field Theory*, Ch. 2
- Srednicki, *Quantum Field Theory*, Ch. 3
