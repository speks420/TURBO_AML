import { Box, Container } from '@chakra-ui/react';
import Header from './Header';
import Footer from './Footer';

/**
 * Layout component for the application
 * 
 * @param {object} props - Component props
 * @param {React.ReactNode} props.children - Child components
 * @returns {JSX.Element} Layout component
 */
const Layout = ({ children }) => {
  return (
    <Box minH="100vh" display="flex" flexDirection="column">
      <Header />
      <Container maxW="1200px" flex="1" py={8}>
        {children}
      </Container>
      <Footer />
    </Box>
  );
};

export default Layout; 