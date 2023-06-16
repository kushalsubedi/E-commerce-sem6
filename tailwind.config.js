// @type {import('tailwindcss').Config} 
module.exports = {
  content: [
    "./src/**/*.{html,js}",
    "./node_modules/flowbite/**/*.js",
    "./src/**/forms.py",
  ],
  theme: {
    extend: {
      fontFamily: {
        'fontawesome': ['Font Awesome 5 Free']
      }
    }
  },
  plugins: [
      require('flowbite/plugin')
  ]
}
