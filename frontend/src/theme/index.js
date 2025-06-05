import { extendTheme } from '@chakra-ui/react'

// Add your color mode config
const config = {
  initialColorMode: 'light',
  useSystemColorMode: false,
}

// Extend the theme
const theme = extendTheme({ 
  config,
  colors: {
    brand: {
      50: '#e6f5ff',
      100: '#cce6ff',
      200: '#99ccff',
      300: '#66b2ff',
      400: '#3399ff',
      500: '#007fff',
      600: '#0066cc',
      700: '#004c99',
      800: '#003366',
      900: '#001933',
    },
  },
  fonts: {
    heading: `'Inter', sans-serif`,
    body: `'Inter', sans-serif`,
  },
})

export default theme 