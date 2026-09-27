import { defineConfig } from 'vite'

// Presentation folders share the template's dependency install through a local
// symlink. Allow Vite to serve font assets from that resolved dependency path.
export default defineConfig({
  server: {
    fs: {
      strict: false,
    },
  },
})
