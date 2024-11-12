import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
import WindiCSS from "vite-plugin-windicss";

const path = require("path");
const port = process.env.PORT || 8000;

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue(), WindiCSS()],
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "./src"),
    },
  },
  server: {
    open: true,
    port: 3000,
    proxy: {
      "/graphql": {
        target: `http://0.0.0.0:${port}`,
        changeOrigin: true,
        secure: false,
        ws: true,
      },
      // '/wsgraphql': {
      //   target: 'ws://127.0.0.1:8000',
      //   changeOrigin: true,
      //   secure: false,
      //   ws: true,
      //   rewrite: path => path.replace(/^\/wsgraphql/, "/graphql")
      // }
    },
  },
});
