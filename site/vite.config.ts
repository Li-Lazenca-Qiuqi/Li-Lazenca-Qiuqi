import react from '@vitejs/plugin-react'
import { defineConfig } from 'vite'

export default defineConfig(({ command, isPreview }) => ({
  base: command === 'build' || isPreview === true ? '/Li-Lazenca-Qiuqi/' : '/',
  plugins: [react()],
  server: {
    host: '0.0.0.0',
    port: 5180,
    strictPort: true,
  },
}))
