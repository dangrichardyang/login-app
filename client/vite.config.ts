import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import dns from 'dns'

dns.setDefaultResultOrder('verbatim')

export default defineConfig({
  plugins: [react()],
  base: "/login/",
  server: {
    host: true,
    port: 3000,
    strictPort: true,
  }
})
