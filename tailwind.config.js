/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "templates/auth/signup.html",
    "./node_modules/tw-elements/dist/js/**/*.js",
  ],
  theme: {
    extend: {},
  },
  darkMode: "class",
  plugins: [require("tw-elements/dist/plugin.cjs")],
};