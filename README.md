# Wordsmith

Wordsmith is a responsive browser-based five-letter word game. It grows the original console exercise into a polished portfolio project while retaining the core challenge: find a hidden five-letter word in six guesses.

## Features

- Daily and random puzzle modes
- Six-attempt visual board with duplicate-letter-aware scoring
- On-screen and physical keyboard support
- Colour feedback for correct, present and absent letters
- Local browser statistics for games played, win rate and streak
- Accessible focus styles, labelled board cells and a how-to-play dialog
- No build step or external runtime dependencies

## Run

Open `index.html` in a modern browser, or host the folder with any static web server.

## Original project

`Secrete word game.Nhlanhla.py` is retained as the original Python console exercise that inspired this browser remake.

## Quality and deployment

[![Validate and deploy site](https://github.com/Fakude/Word-game/actions/workflows/pages.yml/badge.svg)](https://github.com/Fakude/Word-game/actions/workflows/pages.yml)

The GitHub Actions workflow checks browser JavaScript on pushes and pull requests, then deploys successful `main` branch changes to GitHub Pages.

Key files: `index.html` (structure), `style.css` (responsive UI), `game.js` (game logic), and `.github/workflows/pages.yml` (CI/CD).
