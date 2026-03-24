# TurtleSpace

Run Python turtle graphics in GitHub Codespaces using VNC.

## Quick Start

1. Click **Code → Codespaces → Create codespace on main**
2. Wait for the container to build (first time takes a couple minutes)
3. When port **6080** is forwarded, open it in your browser — that's your VNC desktop
   - Password: `vscode`
4. Run any example from the terminal:
   ```bash
   python examples/spiral.py
   ```
   The turtle window appears on the VNC desktop.

## Examples

| Script | Description |
|---|---|
| `examples/spiral.py` | Colorful spiral pattern |
| `examples/tree.py` | Recursive fractal tree |
| `examples/star.py` | Simple five-pointed star |

## How It Works

The devcontainer uses the [`desktop-lite`](https://github.com/devcontainers/features/tree/main/src/desktop-lite) feature to run a lightweight Fluxbox desktop with TigerVNC + noVNC. The `DISPLAY` environment variable is set to `:1`, so any GUI application launched from the terminal renders on the virtual desktop, which you view through your browser on port 6080.

## Tips

- The VNC server may take a few seconds to start — if you get a blank page, refresh after a moment.
- `turtle.done()` keeps the window open. Close it or Ctrl+C in the terminal to exit.
- Write your own scripts in the root or `examples/` directory and run them the same way.
