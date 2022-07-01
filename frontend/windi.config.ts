import { defineConfig } from 'windicss/helpers'
import formsPlugin from 'windicss/plugin/forms'
import { transform } from 'windicss/helpers'

export default defineConfig({
  darkMode: 'class',
  safelist: 'p-3 p-4 p-5',
  theme: {
    extend: {
      colors: {
        teal: {
          100: '#096',
        },
      },
    },
  },
  plugins: [transform('daisyui'), formsPlugin],
})