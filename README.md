# Sonic and Visual Exploration of the Riemann Zeta Function
Ziji Zhou |
Professor Zhang, Math-345 Complex Analysis
## Introduction and Motivation
The Riemann Zeta function $\zeta(s)$ holds a place in mathematical lore. Most famously, the analytic continuation of the Riemann Zeta function holds the question to one of the Millennial questions: The Riemann Hypothesis, which we will prove...


...just kidding that will be left as an exercise for the reader :)


Instead I want to explore the magical properties of the function sonically, whilst supported by graphical information to hear and see exactly what is happening with this important function. One can easily imagine with the graph below that the Riemann Zeta function possesses some beautiful symmetries.

<p align="center">
  <img src='/final/Riemann%20Zeta%20Graph.png' width='500'>
</p>

The idea is to create something beautiful, representative, and generative. I have always been fascinated by systemically generative music (think modular systems) and I want to truly utilize the properties of the Riemann Zeta function within the soul of the system.

I will be utilizing a software called PureData (commonly abbreviated as pd) which is "an open source visual programming language for multimedia" made by Miller Puckett. pd provides for a more intuitive way of creating a sound system from scratch. Of course, for the more complex (pun intended) element of the project I will be using Python which I can send packets of information into pd in real time. I will also use the matplot library to show visualize what we're hearing. Lastly of course this site is written in MD on Github Pages. All of the code and snippets mentioned and written are all up on this repo (https://github.com/zijiamherst/complexFinal).

## The Function

There are a few things especially of the Riemann Zeta function that I was curious to explore. Let's try to understand them purely mathematically first (with a lot of handwaving involved).


Let's start with the function itself:
$$\zeta(s) = \sum_{n=1}^{\infty} \frac{1}{n^s}, \text{Re}(s) > 1$$

### Convergence

