# Development

For Tailwind to Rebuild the Output CSS, a watcher must be run to compile the new styling as pages are edited.

To do this run:

```bash
tailwindcss -i static/style/input.css -o static/style/output.css --watch
```

You must be in the `app` directory